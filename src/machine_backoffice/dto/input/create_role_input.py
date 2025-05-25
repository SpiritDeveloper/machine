from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Optional


class CreateRoleInputSchema(BaseModel):
    name: Optional[str] = Field(description="name",  example="admin", default=None)
    description: Optional[str] = Field(description="description", example="this is a admin role", default=None)

class CreateRoleInput:
    def create(input: CreateRoleInputSchema):
        return jsonable_encoder(input, exclude_none=True)
