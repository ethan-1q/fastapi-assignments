import pytest

from typing import Generator
from fastapi.testclient import TestClient
from httpx import AsyncClient

from tortoise import Tortoise
from tortoise.contrib.test import finalizer, initializer, _init_db

from ..core.settings import Settings
from ..core.fastapi import get_application
from ..core.database import setup_database
from ..app.models import krew, member


@pytest.fixture(scope="function")
def settings():
    settings = Settings(
        ICP_DATABASE_URL="sqlite://icp.db",
        MY_DATABASE_URL="sqlite://my.db",
        GENERATE_SCHEMAS=True
    )
    settings.Config.env_file = None
    return settings


# TODO: 다중 DB 연결?
# @pytest.fixture(scope="function")
# def client(request, settings) -> Generator:
#     initializer([member], db_url=settings.ICP_DATABASE_URL, app_label="member")
#
#     app = get_application(settings)
#
#     with TestClient(app) as client:
#         yield client
#
#     request.addfinalizer(finalizer)


@pytest.fixture(scope="function")
async def async_client(settings) -> Generator:
    await _init_db({
        "connections": {
            "icp_db": settings.ICP_DATABASE_URL,
            "my_db": settings.MY_DATABASE_URL,
        },
        "apps": {
            "member": {"models": [member], "default_connection": "icp_db"},
            "krew": {"models": [krew], "default_connection": "my_db"},
        },
    })

    app = get_application(settings)

    async with AsyncClient(app=app, base_url="http://test") as async_client:
        yield async_client

    await Tortoise.close_connections()
