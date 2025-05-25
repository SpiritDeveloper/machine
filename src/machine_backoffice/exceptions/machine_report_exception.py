from . import Error


class MachineReportException:
    @staticmethod
    def missing_fields(exception: list[str] = []):
        Error(422, "Missing fields", exception)


    @staticmethod
    def machine_report_not_found():
        Error(404, "Machine report not found")