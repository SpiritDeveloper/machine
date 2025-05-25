from jwt import encode, decode, exceptions
from os import getenv
from ..exceptions.jwt_exceptions import JwtErrors
import logging


class Jwt:
    def __init__(self):
        self.secret = getenv("SECRET_KEY")
        self.algorith = getenv("ALGORITHM")

    def encode(self, user):
        try:
            if not self.secret or not self.algorith:
                JwtErrors.environment_variables_not_found()
            return encode(user, self.secret, algorithm=self.algorith)
        except exceptions.InvalidTokenError as error:
            logging.warning(str(error))

    def decode(self, token: str):
        try:
            if not self.secret or not self.algorith:
                JwtErrors.environment_variables_not_found()
            return decode(token, self.secret, algorithms=[self.algorith])
        except exceptions.DecodeError as error:
            logging.warning(str(error))