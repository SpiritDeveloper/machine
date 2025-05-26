from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, ValidationError
from datetime import datetime
from ...exceptions.user_exception import UserException
from typing import Optional

class MachineStatusCacheSchema(BaseModel):
    status: int = Field(description="machine status", example=1, required=True)
    start_time: Optional[datetime] = Field(description="machine start time", example=datetime.now())
    date_failure: Optional[datetime] = Field(description="machine date failure", example=datetime.now())
    machine_id: str = Field(description="machine id", example="1234567890", required=True)
    enable: bool = Field(description="machine enable", example=True, default=True)
    created_at: datetime = Field(description="machine created at", example=datetime.now(), default=datetime.now())
    updated_at: datetime = Field(description="machine updated at", example=datetime.now(), default=datetime.now())
    deleted_at: datetime = Field(description="machine deleted at", example=datetime.now(), default=None)


class CreateMachineStatusCacheSchemaInput:
    def create(input: MachineStatusCacheSchema):
        try:
            return jsonable_encoder(MachineStatusCacheSchema(**input))
        except ValidationError as e:
            missing_fields = [error["loc"][0] for error in e.errors()]
            raise UserException.missing_fields(missing_fields)