from bson import ObjectId
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


from app.db.object_id import PyObjectId


class UserModel(BaseModel):
    """Represents how a base user will be stored in the db."""

    class Config:
        """Scehma config."""

        allow_populated_by_field_name = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "email": "email@domain.com",
                "username": "username",
                "password": "secretpassword",
                # "hashed_password": "hashedpassword",
                # "salt": "salt",
                "first_name": "john",
                "last_name": "doe",
            },
        }

    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    email: EmailStr = Field(...)
    username: str = Field()
    password: str = Field(..., min_length=8, max_length=64)
    first_name: str = Field(...)
    last_name: str = Field(...)
    full_name: Optional[str]
    # _id: ObjectId = Field(...)
    # hashed_password = Field(...)
    # salt = Field(...)
    # other_names: str = Field(...)

    def __str__(self) -> str:
        return (
            f"UserModel("
            f"id=({self.id!r}), "
            f"email=({self.email!r}), "
            f"full_name=({self.full_name!r})"
            f")"
        )
