from ..models import MachineReportModel
from ..exceptions.machine_report_exception import MachineReportException
import logging


class MachineReportService:
    def __init__(self):
        self.machine_report_repository = MachineReportModel()

    def get(self, id: str):
        logging.info("Find machine report by id with id: %s", id)
        try:
            return self.machine_report_repository.get_by_id(id)
        except Exception:
            logging.error("Error getting machine report by id")
            raise MachineReportException.machine_report_not_found()

    def get_all(self):
        logging.info("Find all machine reports")
        try:
            return self.machine_report_repository.get_all()
        except Exception:
            logging.error("Error getting all machine reports")
            raise MachineReportException.machine_report_not_found()

    def create(self, create: dict):
        logging.info("Create machine report with data: %s", create)
        try:
            return self.machine_report_repository.save(create)
        except Exception:
            logging.error("Error creating machine report")
            raise MachineReportException.machine_report_not_found()

    def update(self, id: str, update: dict):
        logging.info("Update machine report with id: %s", id)
        try:
            return self.machine_report_repository.update(id, update)
        except Exception:
            logging.error("Error updating machine report")
            raise MachineReportException.machine_report_not_found()

    def delete(self, id: str):
        logging.info("Delete psp with id: %s", id)
        try:
            return self.machine_report_repository.delete(id)
        except Exception:
            logging.error("Error deleting machine report")
            raise MachineReportException.machine_report_not_found()