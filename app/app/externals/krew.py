# import requests
import aiohttp

from ...core.exceptions import BadRequest

INTERNAL_API_URL = 'https://sandbox-con.kakao.com/admin/internal-api/hello-mis/'


async def request_krew_info_from_ldap_id(ldap_id):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=INTERNAL_API_URL, params={'name': ldap_id}) as response:
            response_json = await response.json()

    if 'error' in response_json:
        raise BadRequest()

    return response_json
