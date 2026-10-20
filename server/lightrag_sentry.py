import ast
import functools
import logging
import os
import re
import runpy
import sys
from functools import partial
from importlib.metadata import PackageNotFoundError, version
from types import FrameType
from typing import Any

_LOGGER = logging.getLogger("lightrag_sentry")
_REPORTED_ATTR = "__lightrag_sentry_reported__"
_INTERNAL_SERVER_ERROR_PREFIX = "Internal server error (error_id:"
_TRACEBACK_DUMP_PREFIX = "Traceback (most recent call last)"
_FILTERED = "[Filtered]"
_TRIVIAL_TEXTS = frozenset({"None", "True", "False", "null", "none"})
_GENERIC_TYPE_NAMES = frozenset({"Exception", "BaseException", "Error"})
_LAST_ARG_FILTERED_TEMPLATES = frozenset(
    {
        "JSON parsing error: %s; repair failed: %s; response: %r",
        "Keyword extraction response required JSON repair: %s; response: %r",
    }
)
_RETRY_HELPERS = (
    "InvalidResponseError",
    "TransientBadRequestError",
    "_is_retryable_rate_limit_error",
    "_is_transient_status_error",
)


def _is_lightrag_logger(name: str) -> bool:
    return name == "lightrag" or name.startswith("lightrag.")


def _is_retried_llm_error(record: logging.LogRecord, exc: BaseException) -> bool:
    module = sys.modules.get("lightrag.llm.openai")
    if module is None or record.pathname != module.__file__:
        return False
    import openai

    retryable_types: tuple[type[BaseException], ...] = (
        openai.APIConnectionError,
        openai.InternalServerError,
        module.InvalidResponseError,
        module.TransientBadRequestError,
    )
    return (
        isinstance(exc, retryable_types)
        or module._is_retryable_rate_limit_error(exc)
        or module._is_transient_status_error(exc)
    )


@functools.cache
def _except_handler_lines(filename: str) -> tuple[tuple[int, int], ...]:
    try:
        with open(filename, encoding="utf-8") as source:
            tree = ast.parse(source.read())
    except (OSError, SyntaxError, ValueError):
        return ()
    return tuple(
        (node.lineno, node.end_lineno or node.lineno)
        for node in ast.walk(tree)
        if isinstance(node, ast.ExceptHandler)
    )


def _logging_frame(record: logging.LogRecord) -> FrameType | None:
    frame = sys._getframe()
    while frame is not None:
        if (
            frame.f_lineno == record.lineno
            and frame.f_code.co_filename == record.pathname
        ):
            return frame
        frame = frame.f_back
    return None


def _caught_here(record: logging.LogRecord, exc: BaseException) -> bool:
    traceback = exc.__traceback__
    if traceback is None or traceback.tb_frame is not _logging_frame(record):
        return False
    return any(
        start <= record.lineno <= end
        for start, end in _except_handler_lines(record.pathname)
    )


def _mentions(message: str, exc: BaseException) -> bool:
    text = str(exc).strip()
    if len(text) >= 4 and text not in _TRIVIAL_TEXTS and not text.isdigit():
        if re.search(rf"(?<!\w){re.escape(text)}(?!\w)", message):
            return True
    name = type(exc).__name__
    return name not in _GENERIC_TYPE_NAMES and bool(
        re.search(rf"(?<!\w){re.escape(name)}(?!\w)", message)
    )


def _root_exception(exc: BaseException) -> BaseException:
    seen = {id(exc)}
    while True:
        cause = exc.__cause__ or (None if exc.__suppress_context__ else exc.__context__)
        if cause is None or id(cause) in seen:
            return exc
        seen.add(id(cause))
        exc = cause


def _fingerprint(exc: BaseException) -> list[str]:
    root = _root_exception(exc)
    innermost = in_app = ""
    traceback = root.__traceback__
    while traceback is not None:
        frame = traceback.tb_frame
        module = frame.f_globals.get("__name__", "")
        innermost = f"{module}.{frame.f_code.co_name}"
        if _is_lightrag_logger(module):
            in_app = innermost
        traceback = traceback.tb_next
    root_type = type(root)
    return [f"{root_type.__module__}.{root_type.__qualname__}", in_app or innermost]


def _filter_logentry(event: dict[str, Any], record: logging.LogRecord) -> None:
    if record.msg not in _LAST_ARG_FILTERED_TEMPLATES or not isinstance(
        record.args, tuple
    ):
        return
    params = record.args[:-1] + (_FILTERED,)
    logentry = event.get("logentry") or {}
    logentry["params"] = params
    logentry["formatted"] = record.msg.replace("%r", "%s") % params
    event["logentry"] = logentry


def _mark_reported(exc: BaseException, key: str | None) -> bool:
    reported = getattr(exc, _REPORTED_ATTR, None)
    if reported is None:
        reported = set()
        setattr(exc, _REPORTED_ATTR, reported)
    if key in reported:
        return False
    reported.add(key)
    return True


def _process_event(
    event: dict[str, Any], hint: dict[str, Any]
) -> dict[str, Any] | None:
    from sentry_sdk.utils import event_from_exception

    exc_info = hint.get("exc_info")
    if exc_info is not None and _is_logged_internal_server_error(exc_info[1]):
        return None
    record = hint.get("log_record")
    if record is None:
        if exc_info is None or exc_info[1] is None:
            return event
        if getattr(exc_info[1], _REPORTED_ATTR, None):
            return None
        _mark_reported(exc_info[1], None)
        event["fingerprint"] = _fingerprint(exc_info[1])
        return event
    _filter_logentry(event, record)
    message = record.getMessage()
    is_dump = message.lstrip().startswith(_TRACEBACK_DUMP_PREFIX)
    if exc_info is None and "exception" not in event:
        current = sys.exc_info()
        if current[1] is not None and (
            is_dump
            or _caught_here(record, current[1])
            or _mentions(message, current[1])
        ):
            exc_info = current
            exc_event, _ = event_from_exception(
                exc_info,
                client_options=_client_options(),
                mechanism={"type": "logging", "handled": True},
            )
            event["exception"] = exc_event["exception"]
            event.pop("threads", None)
            hint["exc_info"] = exc_info
    if exc_info is None or exc_info[1] is None:
        return None if is_dump else event
    exc = exc_info[1]
    if _is_retried_llm_error(record, exc):
        return None
    if is_dump and getattr(exc, _REPORTED_ATTR, None):
        return None
    if not _mark_reported(exc, message):
        return None
    event["fingerprint"] = _fingerprint(exc)
    return event


def _before_breadcrumb(
    crumb: dict[str, Any], hint: dict[str, Any]
) -> dict[str, Any] | None:
    record = hint.get("log_record")
    if record is not None and _is_lightrag_logger(record.name):
        return None
    return crumb


def _is_logged_internal_server_error(exc: BaseException | None) -> bool:
    from starlette.exceptions import HTTPException

    return (
        isinstance(exc, HTTPException)
        and isinstance(exc.detail, str)
        and exc.detail.startswith(_INTERNAL_SERVER_ERROR_PREFIX)
    )


def _client_options() -> dict[str, Any]:
    import sentry_sdk

    return sentry_sdk.get_client().options


def _traces_sampler(
    sampling_context: dict[str, Any],
    *,
    ignored_paths: frozenset[str],
    sample_rate: float,
) -> float:
    if sampling_context.get("asgi_scope", {}).get("path") in ignored_paths:
        return 0.0
    parent_sampled = sampling_context.get("parent_sampled")
    if parent_sampled is not None:
        return float(parent_sampled)
    return sample_rate


def _float_env(name: str, default: float) -> float:
    try:
        return float(os.environ.get(name) or default)
    except ValueError:
        _LOGGER.warning("Sentry: %s is not a number, using %s", name, default)
        return default


def _release() -> str | None:
    try:
        return f"lightrag@{version('lightrag-hku')}"
    except PackageNotFoundError:
        return None


def setup_sentry() -> None:
    dsn = os.environ.get("SENTRY_DSN")
    if not dsn:
        return
    import sentry_sdk
    from sentry_sdk.integrations.logging import LoggingIntegration

    cluster_name = os.environ.get("SENTRY_CLUSTER_NAME") or "unknown"
    ignored_paths = frozenset(
        path for path in os.environ.get("SENTRY_IGNORED_PATHS", "").split(",") if path
    )
    sentry_sdk.init(
        dsn=dsn,
        environment=cluster_name,
        release=_release(),
        integrations=[
            LoggingIntegration(level=logging.WARNING, event_level=logging.ERROR)
        ],
        traces_sampler=partial(
            _traces_sampler,
            ignored_paths=ignored_paths,
            sample_rate=_float_env("SENTRY_SAMPLE_RATE", 0.0),
        ),
        before_breadcrumb=_before_breadcrumb,
        attach_stacktrace=True,
        in_app_include=["lightrag"],
        send_default_pii=False,
        include_local_variables=False,
        max_request_body_size="never",
    )
    sentry_sdk.get_global_scope().add_event_processor(_process_event)
    sentry_sdk.set_tag("app", os.environ.get("SENTRY_APP_NAME") or "lightrag")
    sentry_sdk.set_tag("cluster", cluster_name)


def main() -> None:
    try:
        setup_sentry()
    except Exception as error:
        _LOGGER.warning(
            "Sentry setup failed (%s), starting LightRAG without it",
            type(error).__name__,
        )
    runpy.run_module(
        "lightrag.api.lightrag_server", run_name="__main__", alter_sys=True
    )


if __name__ == "__main__":
    main()
