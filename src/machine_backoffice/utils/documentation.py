from abc import ABC
from ..config.dto import ResponseSchema, ResponseOutput
from ..config.dto import RequestMethodEnum
from pydantic import BaseModel
from typing import List, Any
from ..utils.validate_properties import validate


class Documentation(ABC):
    @classmethod
    def document_status_code(
        cls, success: bool, description: str, errors: list[str] = [], payload: Any = {}
    ) -> dict:
        documentation = {}
        documentation["model"] = ResponseSchema
        documentation["description"] = description
        documentation["content"] = {}
        documentation["content"]["application/json"] = {}
        documentation["content"]["application/json"]["example"] = ResponseOutput.create(
            success=success, message=description, errors=errors, payload=payload
        )
        return documentation

    @classmethod
    def create(
        cls,
        method: RequestMethodEnum = RequestMethodEnum.GET,
        message: str = "ok",
        payload: BaseModel | List[BaseModel] = None,
        authorization: bool = False,
    ) -> dict:
        if isinstance(payload, type) and issubclass(payload, BaseModel):
            if not validate(payload.__fields__, "payload"):
                payload = payload().__dict__
            else:
                payload = payload().__dict__
                items = []
                for item in payload["payload"]:
                    items.append(item.__dict__)
                payload = items

        documentation = {}
        documentation[200] = cls.document_status_code(
            success=True, description=message, payload=payload
        )

        if method in [
            RequestMethodEnum.POST,
            RequestMethodEnum.PUT,
            RequestMethodEnum.DELETE,
        ]:
            documentation[400] = cls.document_status_code(
                success=False, description="Body Error", errors=["Template not found"]
            )

        if authorization:
            documentation[401] = cls.document_status_code(
                success=False,
                description="Unauthorized Error",
                errors=["No token provider"],
            )
            documentation[403] = cls.document_status_code(
                success=False,
                description="Unauthorized Error",
                errors=["Permission not accept"],
            )

        documentation[500] = cls.document_status_code(
            success=False,
            description="Internal Error",
            errors=["Contact to support team"],
        )

        return documentation