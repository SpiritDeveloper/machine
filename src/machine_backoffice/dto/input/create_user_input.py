from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Optional

class CreateUserInputSchema(BaseModel):
    name: Optional[str] = Field(description="name", min_length=1, max_length=255, example="John Doe", default=None)
    email: Optional[str] = Field(description="email", min_length=1, max_length=255, example="test@test.com", default=None)
    password: Optional[str] = Field(description="password", min_length=1, max_length=255, example="123456", default=None)
    description: Optional[str] = Field(description="description", min_length=1, max_length=255, example="this is a user", default=None)
    role_id: Optional[str] = Field(description="role", min_length=1, max_length=255, example="admin", default=None)

class CreateUserRoot(BaseModel):
    __root__: CreateUserInputSchema


class CreateUserInput:
    def create(input: CreateUserInputSchema):
        return jsonable_encoder(CreateUserRoot(__root__=input))
