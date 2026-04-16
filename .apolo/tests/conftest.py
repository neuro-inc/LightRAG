pytest_plugins = [
    "apolo_app_types_fixtures.apolo_clients",
]

import pytest
import apolo_sdk


@pytest.fixture
def apolo_client(setup_clients: apolo_sdk.Client):
    apolo_sdk_client = setup_clients

    async def _get_secret(key: str) -> bytes:
        return f"{key}-value".encode()

    apolo_sdk_client.secrets.get = _get_secret
    return apolo_sdk_client
