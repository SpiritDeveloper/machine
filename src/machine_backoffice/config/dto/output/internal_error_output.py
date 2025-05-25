from pydantic import BaseModel


class InternalErrorSchema(BaseModel):
    success: bool
    message: str
    errors: list

    class Config:
        schema_extra = {
            "example": {
                "success": False,
                "message": "Contact the administrator of this error",
                "errors": [],
            },
        }