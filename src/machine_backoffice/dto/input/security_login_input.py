from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Optional

class SecurityLoginInputSchema(BaseModel):
    email: Optional[str] = Field(description="email", min_length=1, max_length=255, example="test@test.com", default=None)
    password: Optional[str] = Field(description="password", min_length=1, max_length=255, example="123456", default=None)

class SecurityLoginInput:
    def create(input: SecurityLoginInputSchema):
        return jsonable_encoder(input, exclude_none=True)
