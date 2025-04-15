from fastapi import APIRouter
from config.config import settings
from .api_v1 import users_router

router = APIRouter(prefix=f"{settings.api.prefix}{settings.api.v1.prefix}")
router.include_router(users_router)
