
import pytest


@pytest.mark.asyncio
async def test_2_3_dbonly(async_client):
    response = await async_client.get("/api/v1/krew?name=ethan.1q&dbonly=true")
    assert response.status_code == 404

    response = await async_client.get("/api/v1/krew?name=ethan.1q&dbonly=false")
    assert response.status_code == 200
    assert response.json()["ldap_id"] == 'ethan.1q'

    response = await async_client.get("/api/v1/krew?name=ethan.1q&dbonly=true")
    assert response.status_code == 200
    assert response.json()["ldap_id"] == 'ethan.1q'


@pytest.mark.asyncio
async def test_2_3_normal(async_client):
    response = await async_client.get("/api/v1/krew?name=ethan.1q")
    assert response.status_code == 200
    assert response.json()["ldap_id"] == 'ethan.1q'


@pytest.mark.asyncio
async def test_2_3_abnormal(async_client):
    response = await async_client.get("/api/v1/krew?name=ethan.1q2")
    assert response.status_code == 400
    assert response.json() == {"error": {"detail_code": "BadRequest", "detail": "Bad Request"}}
