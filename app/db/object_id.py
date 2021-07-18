from bson import ObjectId
from typing import Dict


class PyObjectId(ObjectId):
    """Convert MongoDB '_id' to a string prior to storing them as the '_id' of
    the document.

    MongoDb's ObjectId for '_id' cannot be directly encoded as JSON.
    Therefore requires to be converted to a string to be JSON-encodeable.
    """

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v: ObjectId) -> ObjectId:
        """Validate the ObjectId of the document.

        :param v: ObjectId to validate.
        :raises: ValueError if invalid ObjectId.
        :returns: Valid ObjectId.
        """

        if not ObjectId.is_valid(v):
            raise ValueError("Invalid objectid")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema: Dict) -> None:
        """Updates the field schema used a Pydantic Model for ObjectId to be
        a string.

        :param field_schema: Pydantic Model Field Schema e.g.:
                             id: PyObjectID = Field(
                                     default_factory=PyObjectId, alias="_id"
                                 )
        """

        field_schema.update(type="string")

        return None
