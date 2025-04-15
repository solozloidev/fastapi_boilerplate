from fastapi import APIRouter

from config.config import settings

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("")
async def get_users():
    pass
