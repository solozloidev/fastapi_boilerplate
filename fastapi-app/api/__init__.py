from fastapi import APIRouter
from config.config import settings

router = APIRouter(prefix=settings.api.prefix)
