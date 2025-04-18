from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from api import router as api_router
from config.config import settings
from utils import db_helper


@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    yield
    # shutdown
    print("dispose database engine")
    await db_helper.dispose()


main_app = FastAPI(lifespan=lifespan)
main_app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(
        app="main:main_app", host=settings.run.host, port=settings.run.port, reload=True
    )
