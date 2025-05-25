from . import Error


class MachineUserException:
    @staticmethod
    def missing_fields(exception: list[str] = []):
        Error(422, "Missing fields", exception)


    @staticmethod
    def machine_user_not_found():
        Error(404, "Machine user not found")
