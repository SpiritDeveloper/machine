from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, ValidationError
from ...exceptions.machine_exception import MachineException
from datetime import datetime
import uuid

class MachineSchema(BaseModel):
    name: str = Field(description="machine name", example="machine name", required=True)
    ip: str = Field(description="machine ip", example="192.168.1.1", required=True)
    hash: str = Field(description="machine hash", example="1234567890", required=True)
    description: str = Field(
        description="machine description", example="this is a machine", required=True
    )
    enable: bool = Field(description="machine enable", example=True, default=True)
    created_at: datetime = Field(description="machine created at", example=datetime.now(), default=datetime.now())
    updated_at: datetime = Field(description="machine updated at", example=datetime.now(), default=datetime.now())
    deleted_at: datetime = Field(description="machine deleted at", example=datetime.now(), default=None)


class CreateMachineSchemaInput:
    def create(input: MachineSchema):
        try:
            return jsonable_encoder(MachineSchema(**input))
        except ValidationError as e:
            missing_fields = [error["loc"][0] for error in e.errors()]
            raise MachineException.missing_fields(missing_fields)