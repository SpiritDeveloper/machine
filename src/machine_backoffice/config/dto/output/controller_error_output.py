from pydantic import BaseModel


class ControlledErrorSchema(BaseModel):
    success: bool
    message: str
    payload: dict

    class Config:
        schema_extra = {
            "example": {
                "success": False,
                "message": "Generic message error",
                "payload": {},
            },
        }