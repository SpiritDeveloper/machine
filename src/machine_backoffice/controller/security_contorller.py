from fastapi import APIRouter
from ..services.security_service import SecurityService
from ..utils.documentation import Documentation
from ..config.dto.types import RequestMethodEnum
from ..dto import SecurityLoginInput, SecurityLoginInputSchema

security = APIRouter(prefix="/security", tags=["security"])


class SecurityController:
    login_documentation = Documentation.create(
        message="Login",
        method=RequestMethodEnum.POST,
        payload=SecurityLoginInputSchema,
        authorization=True,
    )

    @security.post(
        "/login",
        description="Login",
        responses=login_documentation,
    )
    def login(login: SecurityLoginInputSchema):
        login: SecurityLoginInputSchema = SecurityLoginInput.create(login)
        return SecurityService().login(login)
