from fastapi import APIRouter

from ...services import krew as krew_service
from ...schemas import KrewOut

router = APIRouter(prefix="/krew")


@router.get("", response_model=KrewOut)
async def get_krew_info(name: str, dbonly: bool = False):
    ldap_id = name
    return await krew_service.get_krew_info_from_ldap_id(ldap_id, dbonly)

