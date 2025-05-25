from pydantic import BaseModel
from typing import List


class ControlledErrorCheckedSchema(BaseModel):
    success: bool
    message: str
    errors: List[str]


class ControlledErrorCheckedSchemaRoot(BaseModel):
    __root__: ControlledErrorCheckedSchema