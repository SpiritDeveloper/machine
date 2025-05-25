from . import Error

class JwtErrors:

    @staticmethod
    def token_not_found():
        Error(401, "no valid token was found in the request")

    @staticmethod
    def invalid_token():
        Error(401, "your token is invalid, please log in again")

    @staticmethod
    def bearer_not_found():
        Error(400, "it is necessary to send the word bearer before the token")

    @staticmethod
    def environment_variables_not_found():
        Error(500, "no environment variables were set, contact your administrator")

    @staticmethod
    def missing_params():
        Error(400, "missing parameters in request body")

    @staticmethod
    def dont_permission_access(ip: str):
        Error(403, "the ip %s is not whitelisted" % (ip))

    @staticmethod
    def not_exist_configuration():
        Error(404, "the configuration is enable")