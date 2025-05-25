from . import Error


class UserException:
    @staticmethod
    def missing_fields(exception: list[str] = []):
        Error(422, "Missing fields", exception)

    @staticmethod
    def user_not_found(exception: list[str] = []):
        Error(404, "User not found", exception)

    @staticmethod
    def user_already_exists(exception: list[str] = []):
        Error(400, "User already exists", exception)