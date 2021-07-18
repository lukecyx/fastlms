from typing import Any, Dict

from app.db.db import AsyncMongoManager


class UserDBManager:
    """A collection of common methods for interacting with users and the db."""

    def __init__(self, manager: AsyncMongoManager) -> None:
        self.db = manager.db

        return None

    async def create_user(self, user_dict: Dict[str, Any]) -> None:
        """Inserts a new user record into the db.


        :param user_dict: User dict from incoming request.
        """

        await self.db.users.insert_one(user_dict)

        return None
