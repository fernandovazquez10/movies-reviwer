from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool | None = False
    HOST: str | None = "0.0.0.0"
    MASTER_URL: str | None = "mater_url://"
    PORT : int | None = 8000
    RELOAD: bool | None = False
    TZ: str | None = "UTC"

    class Config:
        env_file = './.env'


settings = Settings()