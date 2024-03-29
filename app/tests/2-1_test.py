import pytest
from datetime import datetime
from tortoise import run_async

from ..app.models.member import Member


def test_2_1_normal_sync(member_client):
    data_count = 10

    async def init_data():
        for i in range(1, data_count + 1):
            await Member.create(
                id=i,
                kakao_email='test@kakaocorp.com',
                name='테스트',
                created_at=datetime.now(),
                modified_at=datetime.now(),
                kakao_account_id=i,
                dsp_account_id=i,
                state=i
            )
    run_async(init_data())

    response = member_client.get("/api/v1/members?name=테스트")
    assert response.status_code == 200
    assert len(response.json()) == data_count
    for data in response.json():
        assert data['name'] == '테스트'


@pytest.mark.asyncio
async def test_2_1_normal(async_client):
    data_count = 10
    for i in range(1, data_count + 1):
        await Member.create(
            id=i,
            kakao_email='test@kakaocorp.com',
            name='test',
            created_at=datetime.now(),
            modified_at=datetime.now(),
            kakao_account_id=i,
            dsp_account_id=i,
            state=i
        )

    response = await async_client.get("/api/v1/members?name=test")
    assert response.status_code == 200
    assert len(response.json()) == data_count
    for data in response.json():
        assert data['name'] == 'test'


@pytest.mark.asyncio
async def test_2_1_abnormal(async_client):
    response = await async_client.get("/api/v1/members?name=한")
    assert response.status_code == 400
    assert response.json() == {"error": {"detail_code": "BadRequest", "detail": "Bad Request"}}
