from fastapi import Request
from ..utils.jwt_service import Jwt
from ..exceptions.jwt_exceptions import JwtErrors


class Auth:
    async def __new__(cls, token):
        decrypt: object = Jwt().decode(token.credentials)

        if not decrypt:
            JwtErrors.dont_permission_access("")

        decrypt["original_token"] = token.credentials
        Request.user = decrypt

        return True