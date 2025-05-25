from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, ValidationError
from ...exceptions.role_exception import RoleException
from datetime import datetime
import uuid

class RoleSchema(BaseModel):
    name: str = Field(description="role name", example="role name", required=True)
    description: str = Field(
        description="machine description", example="this is a machine", required=True
    )
    enable: bool = Field(description="machine enable", example=True, default=True)
    created_at: datetime = Field(description="machine created at", example=datetime.now(), default=datetime.now())
    updated_at: datetime = Field(description="machine updated at", example=datetime.now(), default=datetime.now())
    deleted_at: datetime = Field(description="machine deleted at", example=datetime.now(), default=None)



class CreateRoleSchemaInput:
    def create(input: RoleSchema):
        try:
            return jsonable_encoder(RoleSchema(**input))
        except ValidationError as e:
            missing_fields = [error["loc"][0] for error in e.errors()]
            raise RoleException.missing_fields(missing_fields)