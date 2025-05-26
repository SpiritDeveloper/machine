from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Optional


class UpdateMachineInputSchema(BaseModel):
    name: Optional[str] = Field(description="machine name", example="machine name", default=None)
    ip: Optional[str] = Field(description="machine ip", example="192.168.1.1", default=None)
    hash: Optional[str] = Field(description="machine hash", example="1234567890", default=None)
    description: Optional[str] = Field(
        description="machine description", example="this is a machine", default=None
    )
class UpdateMachineInput:
    @staticmethod
    def create(input: UpdateMachineInputSchema):
        return jsonable_encoder(input, exclude_none=True)
