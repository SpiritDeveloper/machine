from . import Error


class SecurityException:
    @staticmethod
    def missing_fields(exception: list[str] = []):
        Error(422, "Missing fields", exception)

    @staticmethod
    def credentials_not_found(exception: list[str] = []):
        Error(404, "User or password wrong, please try again", exception)