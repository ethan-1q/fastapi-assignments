
import pytest
from unittest import TestCase, mock

from app.app.externals import krew


# class TestRequest(TestCase):
#     @mock.patch("krew.request_krew_info_from_ldap_id")
#     async def test_request(self, mock_request):
#         mock_request.return_value = {
#             "ldap_id": "ethan.1q",
#             "profile_image": "https: //tree.kakaocorp.com/main/public/krew-image?accountId=ethan.1q",
#             "identityDisplayName": "ethan.1q(한원규)/kakao",
#             "deptName": "CCaaS TF",
#             "deptCode": "014579",
#             "deptMainYn": "Y",
#             "displayName": "ethan(한원규)",
#             "personName": "한원규(테스트)",
#             "emailId": "ethan.1q@kakaocorp.com",
#             "deptPathCode": "01;014576;014578;014579;",
#             "deptPathName": "카카오;CTO;선행기술팀;CCaaS TF;",
#             "parentDeptCode": "014578",
#             "parentDeptName": "선행기술팀",
#             "companyCodeAccount": "dk",
#             "concurrentOffice": [],
#             "employeeNo": "D100679",
#             "gradeName": "팀원",
#             "gradeLevel":"67"
#         }
#
#         krew_info = await krew.request_krew_info_from_ldap_id('ethan.1q')
#
#         self.assertEqual(krew_info["personName"], "한원규")
#         mock_request.assert_called_once_with(
#             "https://jsonplaceholder.typicode.com/users",
#             data={"name": "Test User", "email": "user@test.com",},
#         )


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


def test_2_3_normal_sync(krew_client):
    response = krew_client.get("/api/v1/krew?name=ethan.1q")
    assert response.status_code == 200
    assert response.json()["ldap_id"] == 'ethan.1q'
