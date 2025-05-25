from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Optional


class UpdateRoleInputSchema(BaseModel):
    name: Optional[str] = Field(default=None, description="name", min_length=1, max_length=255, example="John Doe")
    description: Optional[str] = Field(default=None, description="description", min_length=1, max_length=255, example="this is a user")
   
class UpdateRoleInput:
    @staticmethod
    def create(input: UpdateRoleInputSchema):
        return jsonable_encoder(input, exclude_none=True)
