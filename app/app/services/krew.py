
from ..crud import krew as krew_crud
from ..externals.krew import request_krew_info_from_ldap_id
from ...core.exceptions import NotFoundKrew


async def get_krew_info_from_ldap_id(ldap_id, dbonly=False):
    krew = await krew_crud.select_krew_from_ldap_id(ldap_id)
    if not krew:
        if dbonly:
            raise NotFoundKrew(ldap_id)

        krew_info = await request_krew_info_from_ldap_id(ldap_id)

        krew = await krew_crud.insert_krew(krew_info)

    return krew
