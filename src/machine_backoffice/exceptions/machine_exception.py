from . import Error


class MachineException:
    @staticmethod
    def missing_fields(exception: list[str] = []):
        Error(422, "Missing fields", exception)

    @staticmethod
    def machine_not_found(exception: list[str] = []):
        Error(404, "Machine not found", exception)
