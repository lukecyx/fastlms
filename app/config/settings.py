from functools import lru_cache
from os import getenv, environ

from dotenv import load_dotenv
from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Controls the general app settings on the app."""

    load_dotenv()

    class Config:
        """Controls any additional settings."""

        env_file = ".env"

    app_name: str = getenv("APP_NAME", "MISSING APP_NAME")
    app_title: str = getenv("APP_TITLE", "MISSING APP_TITLE")
    secret_key: str = environ["SECRET_KEY"]
    debug: bool = True


class DatabaseSettings(BaseSettings):
    """Controls the apps database settings."""

    class Config:
        """Controls any additional settings."""

        env_file = ".env"

    MONGO_DETAILS: Optional[str] = getenv("MONGO_DETAILS")
    DB_NAME: Optional[str] = getenv("DB_NAME")


@lru_cache()
def get_settings() -> Settings:
    """Instantiates and returns the App Settings class.

    :returns: Instantiated Settings.
    """

    return Settings()


@lru_cache()
def get_db_settings() -> DatabaseSettings:
    """Instantiates and returns the apps DatabaseSettings


    :returns Instantiated DatabaseSettings.
    """

    return DatabaseSettings()
