from app.db.db import AsyncMongoManager
from app.config.settings import get_db_settings

db_settings = get_db_settings()

db = AsyncMongoManager(db_settings)


async def get_db() -> AsyncMongoManager:
    return db


# db_name = get_db_settings().DB_NAME
# client = AsyncIOMotorClient(get_db_settings().MONGO_DETAILS)
# db = client.get_database(name=db_name)
