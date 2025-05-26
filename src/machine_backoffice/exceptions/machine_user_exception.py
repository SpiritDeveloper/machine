from . import Error


class MachineUserException:
    @staticmethod
    def missing_fields(exception: list[str] = []):
        Error(422, "Missing fields", exception)


    @staticmethod
    def machine_user_not_found(exception: list[str] = []):
        Error(404, "Machine user not found")

    @staticmethod
    def machine_user_already_exists(exception: list[str] = []):
        Error(400, "Machine user already exists")
