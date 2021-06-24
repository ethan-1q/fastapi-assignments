from app.app.models.member import Member
from ...core.exceptions import BadRequest


async def select_members_from_name(name):
    members = await Member.get_pydantic().from_queryset(Member.filter(name=name))
    if members:
        return members
    else:
        raise BadRequest()


async def select_members_from_nick(nick):
    return await Member.get_pydantic().from_queryset(Member.filter(kakao_email__startswith=nick))

