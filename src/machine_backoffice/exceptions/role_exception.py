from . import Error


class RoleException:
    @staticmethod
    def missing_fields(exception: list[str] = []):
        Error(422, "Missing fields", exception)

    @staticmethod
    def role_not_found(exception: list[str] = []):
        Error(404, "Role not found", exception)

    @staticmethod
    def role_already_exists(exception: list[str] = []):
        Error(400, "Role already exists", exception)