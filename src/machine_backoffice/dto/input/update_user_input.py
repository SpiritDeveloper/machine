from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Optional


class UpdateUserInputSchema(BaseModel):
    name: Optional[str] = Field(default=None, description="name", min_length=1, max_length=255, example="John Doe")
    email: Optional[str] = Field(default=None, description="email", min_length=1, max_length=255, example="test@test.com")
    password: Optional[str] = Field(default=None, description="password", min_length=1, max_length=255, example="123456")
    description: Optional[str] = Field(default=None, description="description", min_length=1, max_length=255, example="this is a user")
    role_id: Optional[str] = Field(default=None, description="role", min_length=1, max_length=255, example="admin")


class UpdateUserInput:
    @staticmethod
    def create(input: UpdateUserInputSchema):
        return jsonable_encoder(input, exclude_none=True)
