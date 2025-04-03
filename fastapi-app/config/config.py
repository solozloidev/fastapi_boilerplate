from pydantic import BaseModel
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings

class RunConfig(BaseModel):
    host: str = "localhost"
    port: int = 8000

class APIConfig(BaseModel):
    prefix: str = "/api"

class DBConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10
    # "postgresql+asyncpg://{tmpPostgres.username}:{tmpPostgres.password}@{tmpPostgres.hostname}{tmpPostgres.path}?ssl=require"

class Config(BaseSettings):
    run: RunConfig = RunConfig()
    api: APIConfig = APIConfig()
    db: DBConfig

config = Config()
