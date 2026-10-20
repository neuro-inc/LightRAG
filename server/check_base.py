import inspect
import sys

import lightrag.api.utils_api as utils_api
import lightrag.llm.openai as llm_openai
import lightrag.operate as operate

import lightrag_sentry

problems = [
    f"lightrag.llm.openai has no {name}"
    for name in lightrag_sentry._RETRY_HELPERS
    if not hasattr(llm_openai, name)
]
operate_source = inspect.getsource(operate)
problems += [
    f"lightrag.operate no longer logs {template!r}"
    for template in lightrag_sentry._LAST_ARG_FILTERED_TEMPLATES
    if template not in operate_source
]
if (
    f"{utils_api._INTERNAL_SERVER_ERROR_MESSAGE} (error_id:"
    != lightrag_sentry._INTERNAL_SERVER_ERROR_PREFIX
    or '(error_id: {error_id})"' not in inspect.getsource(utils_api)
):
    problems.append("internal_server_error detail changed")
if problems:
    sys.exit("lightrag_sentry does not match the base image: " + "; ".join(problems))
print("lightrag_sentry matches the base image")
