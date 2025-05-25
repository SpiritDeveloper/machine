from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from ...exceptions.user_exception import UserException

import uuid

class UserSchema(BaseModel):
    name: str = Field(description="user name", example="user name", required=True)
    email: str = Field(description="user email", example="user@example.com", required=True)
    password: str = Field(description="user password", example="1234567890", required=True)
    description: str = Field(
        description="user description", example="this is a user", required=True
    )
    role_id: str = Field(description="role id", example="1234567890", required=True)
    enable: bool = Field(description="machine enable", example=True, default=True)
    created_at: datetime = Field(description="machine created at", example=datetime.now(), default=datetime.now())
    updated_at: datetime = Field(description="machine updated at", example=datetime.now(), default=datetime.now())
    deleted_at: datetime = Field(description="machine deleted at", example=datetime.now(), default=None)


class CreateUserSchemaInput:
    def create(input: UserSchema):
        try:
            return jsonable_encoder(UserSchema(**input))
        except ValidationError as e:
            missing_fields = [error["loc"][0] for error in e.errors()]
            raise UserException.missing_fields(missing_fields)