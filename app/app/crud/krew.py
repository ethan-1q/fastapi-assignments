from tortoise.exceptions import DoesNotExist

from app.app.models.krew import Krew


async def select_krew_from_ldap_id(ldap_id):
    try:
        return await Krew.get(ldap_id=ldap_id)
    except DoesNotExist as e:
        return None


async def insert_krew(krew_info):
    krew = await Krew(**krew_info)
    await krew.save()
    return krew
