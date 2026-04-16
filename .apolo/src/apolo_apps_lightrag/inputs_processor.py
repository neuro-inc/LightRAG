import logging
import typing as t
from urllib.parse import urlparse

from apolo_app_types.app_types import AppType
from apolo_app_types.helm.apps.base import BaseChartValueProcessor
from apolo_app_types.helm.apps.common import gen_extra_values
from apolo_app_types.helm.utils.deep_merging import merge_list_of_dicts
from apolo_app_types.protocols.common.networking import RestAPI
from apolo_app_types.protocols.common.secrets_ import ApoloSecret

from .types import (
    LightRAGAppInputs,
    LightRAGLLMConfig,
    LightRAGEmbeddingConfig,
    OpenAIAPICloudProvider,
    OpenAICompatChatAPI,
    OpenAICompatEmbeddingsAPI,
    OpenAIEmbeddingCloudProvider,
)


logger = logging.getLogger(__name__)


def _normalise_complete_url(api: RestAPI) -> str:
    """Return a best-effort fully qualified URL for a RestAPI definition."""
    raw_host = getattr(api, "host", "")
    protocol = getattr(api, "protocol", "https")
    port = getattr(api, "port", None)
    base_path = getattr(api, "base_path", None)
    api_base_path = getattr(api, "api_base_path", None)

    if raw_host.startswith(("http://", "https://")):
        parsed = urlparse(raw_host)
        host = parsed.hostname or ""
        if parsed.scheme:
            protocol = parsed.scheme
        if parsed.port:
            port = parsed.port
        else:
            port = None
        if parsed.path:
            base_path = parsed.path
    else:
        host = raw_host

    if not base_path or base_path == "/":
        base_path = api_base_path or "/"

    if not base_path.startswith("/"):
        base_path = f"/{base_path}"

    if not host:
        # Nothing better to do; fall back to raw host string.
        host = raw_host

    default_port = 443 if protocol == "https" else 80
    port_segment = ""
    if port and port != default_port:
        port_segment = f":{port}"

    return f"{protocol}://{host}{port_segment}{base_path}"


class LightRAGInputsProcessor(BaseChartValueProcessor[LightRAGAppInputs]):
    async def _extract_llm_config(
        self, llm_config: LightRAGLLMConfig
    ) -> dict[str, t.Any]:
        """Extract LLM configuration from provider-specific config."""

        if isinstance(llm_config.api_key, ApoloSecret):
            api_key = (await self.client.secrets.get(llm_config.api_key.key)).decode()
        elif isinstance(llm_config.api_key, str):
            api_key = llm_config.api_key
        else:
            api_key = "no-auth"

        if isinstance(llm_config, OpenAIAPICloudProvider):
            host = _normalise_complete_url(llm_config)
            return {
                "binding": "openai",
                "model": llm_config.model,
                "host": host,
                "api_key": api_key,
            }

        elif isinstance(llm_config, OpenAICompatChatAPI):
            logger.debug("Processing OpenAI-compatible LLM config: %r", llm_config)
            if llm_config.hf_model is None:
                msg = (
                    "OpenAI-compatible LLM configuration requires a Hugging Face model"
                )
                raise ValueError(msg)
            model = llm_config.hf_model.model_hf_name
            host = _normalise_complete_url(llm_config)
            return {
                "binding": "openai",
                "model": model,
                "host": host,
                "api_key": api_key,
            }

        msg = f"Unsupported LLM configuration type: {type(llm_config)!r}"
        raise ValueError(msg)

    async def _extract_embedding_config(
        self, embedding_config: LightRAGEmbeddingConfig
    ) -> dict[str, t.Any]:
        """Extract embedding configuration from provider-specific config."""

        if isinstance(embedding_config.api_key, ApoloSecret):
            api_key = (
                await self.client.secrets.get(embedding_config.api_key.key)
            ).decode()
        elif isinstance(embedding_config.api_key, str):
            api_key = embedding_config.api_key
        else:
            api_key = "no-auth"

        if isinstance(embedding_config, OpenAIEmbeddingCloudProvider):
            host = _normalise_complete_url(embedding_config)
            dimensions = embedding_config.dimensions
            return {
                "binding": "openai",
                "model": embedding_config.model,
                "api_key": api_key,
                "dimensions": dimensions,
                "host": host,
            }
        elif isinstance(embedding_config, OpenAICompatEmbeddingsAPI):
            if embedding_config.hf_model is None:
                msg = "OpenAI-compatible embedding configuration requires a Hugging Face model"
                raise ValueError(msg)
            model = embedding_config.hf_model.model_hf_name
            host = _normalise_complete_url(embedding_config)
            dimensions = getattr(embedding_config, "dimensions", None)
            if dimensions is None:
                msg = "Embedding configuration must specify dimensions"
                raise ValueError(msg)
            return {
                "binding": "openai",
                "model": model,
                "api_key": api_key,
                "dimensions": dimensions,
                "host": host,
            }

        msg = f"Unsupported embedding configuration type: {type(embedding_config)!r}"
        raise ValueError(msg)

    async def _get_environment_values(
        self,
        input_: LightRAGAppInputs,
    ) -> dict[str, t.Any]:
        llm_config = await self._extract_llm_config(input_.llm_config)
        embedding_config = await self._extract_embedding_config(input_.embedding_config)

        pguser = input_.pgvector_user
        pg_password = (await self.client.secrets.get(pguser.password.key)).decode()
        pg_host = pguser.pgbouncer_host or pguser.host
        pg_port = pguser.pgbouncer_port if pguser.pgbouncer_host else pguser.port

        env_config = {
            "HOST": "0.0.0.0",
            "PORT": 9621,
            "WEBUI_TITLE": "Graph RAG Engine",
            "WEBUI_DESCRIPTION": "Simple and Fast Graph Based RAG System",
            "LLM_BINDING": llm_config["binding"],
            "LLM_MODEL": llm_config["model"],
            "LLM_BINDING_HOST": llm_config["host"],
            "LLM_BINDING_API_KEY": llm_config["api_key"],
            "OPENAI_API_KEY": llm_config["api_key"],
            "EMBEDDING_BINDING": embedding_config["binding"],
            "EMBEDDING_MODEL": embedding_config["model"],
            "EMBEDDING_DIM": embedding_config["dimensions"],
            "EMBEDDING_BINDING_HOST": embedding_config["host"],
            "EMBEDDING_BINDING_API_KEY": embedding_config["api_key"],
            "LIGHTRAG_KV_STORAGE": "PGKVStorage",
            "LIGHTRAG_VECTOR_STORAGE": "PGVectorStorage",
            "LIGHTRAG_DOC_STATUS_STORAGE": "PGDocStatusStorage",
            "LIGHTRAG_GRAPH_STORAGE": "NetworkXStorage",
            "POSTGRES_HOST": pg_host,
            "POSTGRES_PORT": pg_port,
            "POSTGRES_USER": pguser.user,
            "POSTGRES_PASSWORD": pg_password,
            "POSTGRES_DATABASE": pguser.dbname,
            "POSTGRES_WORKSPACE": "default",
        }

        return {"env": env_config}

    async def _get_persistence_values(
        self,
        input_: LightRAGAppInputs,
    ) -> dict[str, t.Any]:
        return {
            "persistence": {
                "enabled": True,
                "ragStorage": {
                    "size": f"{input_.persistence.rag_storage_size}Gi",
                },
                "inputs": {
                    "size": f"{input_.persistence.inputs_storage_size}Gi",
                },
            }
        }

    async def gen_extra_values(
        self,
        input_: LightRAGAppInputs,
        app_name: str,
        namespace: str,
        app_id: str,
        app_secrets_name: str,
        *_: t.Any,
        **kwargs: t.Any,
    ) -> dict[str, t.Any]:
        env_values = await self._get_environment_values(input_)
        persistence_values = await self._get_persistence_values(input_)
        platform_values = await gen_extra_values(
            apolo_client=self.client,
            preset_type=input_.preset,
            ingress_http=input_.ingress_http,
            ingress_grpc=None,
            namespace=namespace,
            app_id=app_id,
            app_type=AppType.LightRAG,
        )
        base_values = {
            "replicaCount": 1,
            "image": {
                "repository": "ghcr.io/hkuds/lightrag",
                "tag": "v1.4.9.7",
                "pullPolicy": "IfNotPresent",
            },
            "service": {
                "type": "ClusterIP",
                "port": 9621,
            },
            "nameOverride": "",
            "fullnameOverride": app_name,
        }
        logger.debug("Generated LightRAG values for app %s", app_name)
        return merge_list_of_dicts(
            [
                base_values,
                env_values,
                persistence_values,
                platform_values,
            ]
        )


__all__ = ["LightRAGInputsProcessor"]
