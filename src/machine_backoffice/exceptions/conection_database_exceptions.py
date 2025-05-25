from . import Error


class ConectionDatabaseErrors:
    @staticmethod
    def not_connection_database_by_identifier(errors: list[str] | str = ""):
        Error(404, "error al conectar con la base de datos", errors)