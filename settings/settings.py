from functools import lru_cache
from os import getenv

from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    app_name: Optional[str] = getenv("APP_NAME")
    secret_key: Optional[str] = getenv("SECRET_KEY")
    debug: bool = True


@lru_cache()
def get_settings() -> Settings:
    return Settings()
