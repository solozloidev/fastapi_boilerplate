from fastapi import APIRouter
from config.config import config

router = APIRouter(
    prefix=config.api.prefix
)
