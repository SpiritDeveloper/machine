from ..models import MachineModel
from ..exceptions.machine_exception import MachineException
import logging


class MachineService:
    def __init__(self):
        self.machine_repository = MachineModel()

    def get(self, id: str):
        logging.info("Find machine by id with id: %s", id)
        try:
            return self.machine_repository.get_by_id(id)
        except Exception:
            logging.error("Error getting machine by id")
            raise MachineException.machine_not_found()

    def get_all(self):
        logging.info("Find all machines")
        try:
            return self.machine_repository.get_all()
        except Exception:
            logging.error("Error getting all machines")
            raise MachineException.machine_not_found()

    def create(self, create: dict):
        logging.info("Create machine with data: %s", create)
        try:
            return self.machine_repository.save(create)
        except Exception:
            logging.error("Error creating machine")
            raise MachineException.machine_not_found()

    def update(self, id: str, update: dict):
        logging.info("Update machine with id: %s", id)
        try:
            return self.machine_repository.update(id, update)
        except Exception:
            logging.error("Error updating machine")
            raise MachineException.machine_not_found()

    def delete(self, id: str):
        logging.info("Delete machine with id: %s", id)
        try:
            return self.machine_repository.delete(id)
        except Exception:
            logging.error("Error deleting machine")
            raise MachineException.machine_not_found()