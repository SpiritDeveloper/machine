from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, ValidationError
from ...exceptions.machine_user_exception import MachineUserException
from datetime import datetime
import uuid

class MachineUserSchema(BaseModel):
    machine_id: str = Field(description="machine id", example="1234567890", required=True)
    user_id: str = Field(description="user id", example="1234567890", required=True)
    enable: bool = Field(description="machine enable", example=True, default=True)
    created_at: datetime = Field(description="machine created at", example=datetime.now(), default=datetime.now())
    updated_at: datetime = Field(description="machine updated at", example=datetime.now(), default=datetime.now())
    deleted_at: datetime = Field(description="machine deleted at", example=datetime.now(), default=None)


class CreateMachineUserSchemaInput:
    def create(input: MachineUserSchema):
        try:
            return jsonable_encoder(MachineUserSchema(**input))
        except ValidationError as e:
            missing_fields = [error["loc"][0] for error in e.errors()]
            raise MachineUserException.missing_fields(missing_fields)