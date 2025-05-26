from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Optional


class UpdateMachineUserInputSchema(BaseModel):
    machine_id: Optional[str] = Field(description="machine id", example="1234567890", default=None)
    user_id: Optional[str] = Field(description="user id", example="1234567890", default=None)


class UpdateMachineUserInput:
    @staticmethod
    def create(input: UpdateMachineUserInputSchema):
        return jsonable_encoder(input, exclude_none=True)
