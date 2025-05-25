from ..models import UserModel
from ..dto import SecurityLoginInputSchema, SecurityLoginInput, UserSchema
from ..exceptions.security_exception import SecurityException
from ..utils.jwt_service import Jwt
import logging


class SecurityService:
    def __init__(self):
        self.user_repository = UserModel()

    def login(self, login: SecurityLoginInputSchema):
        logging.info("Login with data: %s", login)

        signin: SecurityLoginInputSchema = SecurityLoginInput.create(login)

        if not signin:
            raise SecurityException.credentials_not_found(['INTERNAL_ERROR_JSON_NOT_CREATED'])
                
        user: UserSchema = self.user_repository.find_one(email=signin['email'])

        if not user:
            raise SecurityException.credentials_not_found(['USER_NOT_FOUND'])
    
        token = Jwt().encode(signin)

        if not token:
            raise SecurityException.credentials_not_found(['TOKEN_NOT_GENERATED'])
        
        response = {}
        response['success'] = True
        response['message'] = "Sign in successful"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['token'] = token
        
        return response
        
        
        
