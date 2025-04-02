from pydantic import BaseModel

from pydantic_settings import BaseSettings

class RunConfig(BaseModel):
    host: str = "localhost"
    port: int = 8000

class APIConfig(BaseModel):
    prefix: str = "/api"

class Config(BaseSettings):
    run: RunConfig = RunConfig()
    api: APIConfig = APIConfig()

config = Config()
