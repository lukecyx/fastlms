from typing import Type

from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase

from app.config.settings import DatabaseSettings
from app.logger import get_logger


class AsyncMongoManager:
    """Asynchronous Database Manager for a MongoDB connection.

    Required settings such as db path/name are required when
    instantiating an instance of the class.

    Sets up a logger to logout when connection is opened/closed.
    """

    def __init__(self, settings: DatabaseSettings) -> None:
        self.settings = settings
        self.log = get_logger()

    async def open_db_connection(self) -> AsyncIOMotorClient:
        """Open the connection to the database."""

        self.log.info("Connecting to database...")

        self.client = AsyncIOMotorClient(self.settings.MONGO_DETAILS)
        self.db = self.client.get_database(self.settings.DB_NAME)
        self.is_connected = True

        self.log.info("Database connection established.")

    async def close_db_connection(self) -> None:
        """Close the database connection."""

        self.log.info("Terminating database connection...")

        self.client.close()
        self.is_connected = False

        self.log.info("Database connection terminated.")

        return None

    @property
    def is_connected(self) -> bool:
        """Whether there is an active db connection.

        :returns: Whether there is an active db  connection.
        """

        return self._is_connected

    @is_connected.setter
    def is_connected(self, connected: bool) -> None:
        """Sets the is_connected property

        :param connected: Whether there is an activate connection.
        """

        self._is_connected = connected

        return None

    @property
    def client(self) -> AsyncIOMotorClient:
        """Access to the db connection's client.

        :returns: Initialised AsyncIOMotorClient.
        """

        return self._client

    @client.setter
    def client(self, client: AsyncIOMotorClient) -> None:
        """Sets the database client.

        :param client: AsyncIOMotorClient to be instantiated.
        """

        self._client = client

        return None

    @property
    def db(self) -> AsyncIOMotorDatabase:
        """Access specific database from app db settings.

        :returns: Asynchronous Mongo DB.
        """

        return self._db

    @db.setter
    def db(self, db: AsyncIOMotorDatabase) -> None:
        """Sets the database to be used.

        :param db: AsyncIOMotorDatabase to be instantiated.
        """

        self._db = db

        return None

    @property
    def collection(self) -> Type:
        """Returns the MongoDB collection to be used.

        :returns: MongoDB Collection Manager class from __call__.
        """

        return self._collection

    @collection.setter
    def collection(self, klass) -> None:
        """Sets the MongoDB collection to be used.

        :param klass: A MongoDB collection manager class.
        """

        self._collection = klass(self)

        return None

    def __call__(self, klass) -> Type:
        """Provides the ability to call class with MongoDB collection class.

        :param klass: A MongoDB collection manager class.
        :returns: Collection manager class.
        """

        setattr(self, "collection", klass)

        return self.collection

    def __str__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"client=({self.client!r}), "
            f"db=({self.db!r}), "
            f"is_connected=({self.is_connected!r})"
            f")"
        )

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}("
            f"settings=({self.settings!r}), "
            f"logger=({self.log!r})"
        )
