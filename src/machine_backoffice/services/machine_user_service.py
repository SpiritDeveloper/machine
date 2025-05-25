from ..models import MachineUserModel
from ..exceptions.machine_user_exception import MachineUserException
import logging


class MachineUserService:
    def __init__(self):
        self.machine_user_repository = MachineUserModel()

    def get(self, id: str):
        logging.info("Find machine user by id with id: %s", id)
        try:
            return self.machine_user_repository.get_by_id(id)
        except Exception:
            logging.error("Error getting machine user by id")
            raise MachineUserException.machine_user_not_found()

    def get_all(self):
        logging.info("Find all machine users")
        try:
            return self.machine_user_repository.get_all()
        except Exception:
            logging.error("Error getting all users")
            raise MachineUserException.machine_user_not_found()

    def create(self, create: dict):
        logging.info("Create machine user with data: %s", create)
        try:
            return self.machine_user_repository.save(create)
        except Exception:
            logging.error("Error creating machine user")
            raise MachineUserException.machine_user_not_found()

    def update(self, id: str, update: dict):
        logging.info("Update user with id: %s", id)
        try:
            return self.machine_user_repository.update(id, update)
        except Exception:
            logging.error("Error updating machine user")
            raise MachineUserException.machine_user_not_found()

    def delete(self, id: str):
        logging.info("Delete machine user with id: %s", id)
        try:
            return self.machine_user_repository.delete(id)
        except Exception:
            logging.error("Error deleting machine user")
            raise MachineUserException.machine_user_not_found()