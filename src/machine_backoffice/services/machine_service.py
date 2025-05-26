from ..models import MachineModel, MachineUserModel, UserModel
from ..dto import MachineSchema, CreateMachineSchemaInput, CreateMachineInputSchema
from ..services.machine_report_service import MachineReportService
from ..exceptions.machine_exception import MachineException
import logging
from datetime import datetime


class MachineService:
    def __init__(self):
        self.machine_repository = MachineModel()
        self.machine_report_service = MachineReportService()
        self.machine_user_repository = MachineUserModel()
        self.user_repository = UserModel()

    def get(self, id: str):
        logging.info("Find machine by id with id: %s", id)
        
        machine: MachineSchema = self.machine_repository.find_one(id=id, enable=True)

        if not machine:
            raise MachineException.machine_not_found(['MACHINE_NOT_FOUND'])
        
        reports = self.machine_report_service.get_report_by_machine_id(machine['_id'])

        machine_user = self.machine_user_repository.find_one(machine_id=str(machine['_id']), enable=True)

        user = {}

        if not machine_user:
            user = {}
        else:
            user = self.user_repository.find_one(id=str(machine_user['user_id']), enable=True)
            user['id'] = str(user['_id'])
            del user['_id']

        machine_response: MachineSchema = {}
        machine_response['id'] = str(machine['_id'])
        machine_response['name'] = machine['name']
        machine_response['ip'] = machine['ip']
        machine_response['hash'] = machine['hash']
        machine_response['description'] = machine['description']
        machine_response['status'] = machine['status']
        machine_response['last_status_change'] = machine['last_status_change']
        try:
            now = datetime.now()
            seconds_diff = (now - machine['last_status_change']).total_seconds()
            machine_response['seconds_since_last_change'] = f"{int(seconds_diff)} segundos"
        except:
            machine_response['seconds_since_last_change'] = "0 segundos"
        machine_response['reports'] = reports
        machine_response['user'] = user
        machine_response['enable'] = machine['enable']
        machine_response['created_at'] = machine['created_at']
        machine_response['updated_at'] = machine['updated_at']
        machine_response['deleted_at'] = machine['deleted_at']

        print(machine_response)
       
        response = {}
        response['success'] = True
        response['message'] = "Machine found"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['machine'] = machine_response
        return response

    def get_all(self):
        logging.info("Find all machines")

        list_machines: list[MachineSchema] = []
        find: list[MachineSchema] = self.machine_repository.get_all()
        
        if not find:
            raise MachineException.machine_not_found(['MACHINE_NOT_FOUND'])
        
        for machine in find:
            machine: MachineSchema = self.machine_repository.find_one(id=machine['_id'], enable=True)

            reports = self.machine_report_service.get_report_by_machine_id(machine['_id'])

            machine_users = self.machine_user_repository.find_one(machine_id=str(machine['_id']), enable=True)

            user = {}
            if not machine_users:
                user = {}
            else:
                user = self.user_repository.find_one(id=str(machine_users['user_id']), enable=True)
                user['id'] = str(user['_id'])
                del user['_id']

            machine_response: MachineSchema = {}
            machine_response['id'] = str(machine['_id'])
            machine_response['name'] = machine['name']
            machine_response['ip'] = machine['ip']
            machine_response['hash'] = machine['hash']
            machine_response['description'] = machine['description']
            machine_response['status'] = machine['status']
            machine_response['last_status_change'] = machine['last_status_change']
            try:
                now = datetime.now()
                seconds_diff = (now - machine['last_status_change']).total_seconds()
                machine_response['seconds_since_last_change'] = f"{int(seconds_diff)} segundos"
            except:
                machine_response['seconds_since_last_change'] = "0 segundos"
            machine_response['reports'] = reports
            machine_response['user'] = user
            machine_response['enable'] = machine['enable']
            machine_response['created_at'] = machine['created_at']
            machine_response['updated_at'] = machine['updated_at']
            machine_response['deleted_at'] = machine['deleted_at']

            list_machines.append(machine_response)

        
        response = {}
        response['success'] = True
        response['message'] = "Machines found"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['machines'] = list_machines
        return response

    def create(self, create: CreateMachineInputSchema):
        logging.info("Create machine with data: %s", create)
        
        machine: MachineSchema = CreateMachineSchemaInput.create(create)

        if not machine:
            raise MachineException.machine_not_found(['INTERNAL_ERROR_JSON_NOT_CREATED'])
        
        exist_machine: MachineSchema = self.machine_repository.find_one(hash=machine['hash'])

        if exist_machine:
            raise MachineException.machine_already_exists(['MACHINE_ALREADY_EXISTS'])
        
        new_machine: MachineSchema = self.machine_repository.save(**machine)

        if not new_machine:
            raise MachineException.machine_not_found(['MACHINE_NOT_CREATED_IN_DATABASE'])
        
        machine_response: MachineSchema = {}
        machine_response['id'] = str(new_machine['_id'])
        machine_response['name'] = new_machine['name']
        machine_response['ip'] = new_machine['ip']
        machine_response['hash'] = new_machine['hash']
        machine_response['description'] = new_machine['description']
        machine_response['enable'] = new_machine['enable']
        machine_response['created_at'] = new_machine['created_at']
        machine_response['updated_at'] = new_machine['updated_at']
        machine_response['deleted_at'] = new_machine['deleted_at']
       
        response = {}
        response['success'] = True
        response['message'] = "Machine created"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['machine'] = machine_response
        return response

    def update(self, id: str, update: dict):
        logging.info("Update machine with id: %s", id)

        if update.get('hash'):
            exist_machine: MachineSchema = self.machine_repository.find_one(hash=update['hash'], enable=True)
            if exist_machine:
                raise MachineException.machine_already_exists(['MACHINE_ALREADY_EXISTS'])
            
        machine: MachineSchema = self.machine_repository.update(id, **update)

        if not machine:
            raise MachineException.machine_not_found(['MACHINE_NOT_UPDATED_IN_DATABASE'])
        
        machine_response: MachineSchema = {}
        machine_response['id'] = str(machine['_id'])
        machine_response['name'] = machine['name']
        machine_response['ip'] = machine['ip']
        machine_response['hash'] = machine['hash']
        machine_response['description'] = machine['description']
        machine_response['enable'] = machine['enable']
        machine_response['created_at'] = machine['created_at']
        machine_response['updated_at'] = machine['updated_at']
        machine_response['deleted_at'] = machine['deleted_at']

        response = {}
        response['success'] = True
        response['message'] = "Machine updated"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['machine'] = machine_response
        return response

    def delete(self, id: str):
        logging.info("Delete machine with id: %s", id)
        
        exist_machine: MachineSchema = self.machine_repository.find_one(id=id, enable=True)

        if not exist_machine:
            raise MachineException.machine_not_found(['MACHINE_NOT_FOUND'])
        
        machine: MachineSchema = self.machine_repository.delete(id)

        if not machine:
            raise MachineException.machine_not_found(['MACHINE_NOT_DELETED_IN_DATABASE'])
        

        machine_response: MachineSchema = {}
        machine_response['id'] = str(machine['_id'])
        machine_response['name'] = machine['name']
        machine_response['ip'] = machine['ip']
        machine_response['hash'] = machine['hash']
        machine_response['description'] = machine['description']
        machine_response['enable'] = machine['enable']
        machine_response['created_at'] = machine['created_at']
        machine_response['updated_at'] = machine['updated_at']
        machine_response['deleted_at'] = machine['deleted_at']


        response = {}
        response['success'] = True
        response['message'] = "User deleted"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['machine'] = machine_response
        return response