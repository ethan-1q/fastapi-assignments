from fastapi import APIRouter

from app.app.api.v1.member import router as members_router
from app.app.api.v1.krew import router as krew_router

router = APIRouter(prefix="/v1")

router.include_router(members_router, tags=["members"])
router.include_router(krew_router, tags=["krew"])
