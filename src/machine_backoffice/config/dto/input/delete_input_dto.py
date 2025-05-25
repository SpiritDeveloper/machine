from pydantic import BaseModel, Field
from fastapi.encoders import jsonable_encoder


class DeleteInputSchema(BaseModel):
    id: str = Field(description="Identifier of object to delete", example="1234567890")


class CreateDeleteInputSchemaRoot(BaseModel):
    __root__: DeleteInputSchema


class CreateDeleteInput:
    @staticmethod
    def create(input: DeleteInputSchema) -> dict:
        return jsonable_encoder(CreateDeleteInputSchemaRoot(__root__=input))