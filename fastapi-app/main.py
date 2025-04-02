import uvicorn
from fastapi import FastAPI
from api import router as api_router
from config.config import config

app = FastAPI()
app.include_router(api_router)


if __name__ == "__main__":
    uvicorn.run(app="main:app", host=config.run.host, port=config.run.port, reload=True)