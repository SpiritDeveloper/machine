from pydantic import BaseModel, Field
from typing import Any
from abc import ABC


class ResponseSchema(BaseModel):
    success: bool = Field(description="Status of service", default=True)
    message: str = Field(description="Message to service", default="ok")
    errors: list[str] = Field(description="Errors of service", default=[])
    payload: Any = Field(description="Data of service to return", default={})


class ResponseOutput(ABC):
    @classmethod
    def create(
        cls, success: bool = True, message: str = "", errors: list[str] = [], payload: Any = {}
    ) -> ResponseSchema:
        return ResponseSchema(success=success, message=message, errors=errors, payload=payload)