import pytest


@pytest.mark.asyncio
async def test_root(async_client):
    response = await async_client.get("/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
