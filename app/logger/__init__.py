from logging import getLogger, Logger
from logging.config import dictConfig

from app.config.logging_config import LogConfig
from app.config.settings import get_settings

app_settings = get_settings()
dictConfig(LogConfig().dict())

logger = getLogger(app_settings.app_name)


def get_logger() -> Logger:
    """Returns configred logger."""

    return logger
