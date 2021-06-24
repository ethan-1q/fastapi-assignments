# from fastapi_pagination.ext.tortoise import paginate

from ..crud import member as member_crud


async def list_members_from_name(name):
    return await member_crud.select_members_from_name(name)


async def list_members_from_nick(nick):
    return await member_crud.select_members_from_nick(nick)
