from pydantic import BaseModel
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings, SettingsConfigDict

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

class Config(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="FASTAPI__"
    )
    run: RunConfig = RunConfig()
    api: APIConfig = APIConfig()
    db: DBConfig

config = Config()
print(config.db.url)
