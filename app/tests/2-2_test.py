
import pytest
from datetime import datetime

from ..app.models.member import Member


@pytest.mark.asyncio
async def test_2_2_normal(async_client):
    data_count = 10
    for i in range(1, data_count + 1):
        await Member.create(
            id=i,
            kakao_email=f'{"t" * i}@kakaocorp.com',
            name='테스트',
            created_at=datetime.now(),
            modified_at=datetime.now(),
            kakao_account_id=i,
            dsp_account_id=i,
            state=i
        )

    response = await async_client.get("/api/v1/members?nick=tt")
    assert response.status_code == 200
    assert len(response.json()) == data_count - 1
    for data in response.json():
        assert data['kakao_email'].startswith('tt')


@pytest.mark.asyncio
async def test_2_2_emtpy(async_client):
    response = await async_client.get("/api/v1/members?nick=abcdefg")
    assert response.status_code == 200
    assert response.json() == []
