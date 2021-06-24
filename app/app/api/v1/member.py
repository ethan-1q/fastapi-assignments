from typing import List
from fastapi import APIRouter

from ...services import member as member_service
from ...schemas import MemberOut
from ....core.exceptions import BadRequest

router = APIRouter(prefix="/members")


@router.get("", response_model=List[MemberOut])
async def members_from_name(name: str = None, nick: str = None):
    if name and not nick:
        return await member_service.list_members_from_name(name)
    elif not name and nick:
        return await member_service.list_members_from_nick(nick)
    else:
        raise BadRequest()
