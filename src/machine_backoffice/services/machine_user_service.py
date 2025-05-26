from ..models import MachineUserModel, MachineModel, UserModel
from ..dto import MachineUserSchema, MachineSchema, UserSchema, CreateMachineUserInputSchema, UpdateMachineUserInputSchema
from ..exceptions.machine_user_exception import MachineUserException
from ..exceptions.machine_exception import MachineException
from ..exceptions.user_exception import UserException
import logging


class MachineUserService:
    def __init__(self):
        self.machine_user_repository = MachineUserModel()
        self.machine_repository = MachineModel()
        self.user_repository = UserModel()

    def get(self, id: str):
        logging.info("Find machine user by id with id: %s", id)

        machine_user: MachineUserSchema = self.machine_user_repository.find_one(id=id, enable=True)

        if not machine_user:
            raise MachineUserException.machine_user_not_found(['MACHINE_USER_NOT_FOUND'])
        
        machine: MachineSchema = self.machine_repository.find_one(id=machine_user['machine_id'])

        if not machine:
            raise MachineException.machine_not_found(['MACHINE_NOT_FOUND'])

        user: UserSchema = self.user_repository.find_one(id=machine_user['user_id'])

        if not user:
            raise UserException.user_not_found(['USER_NOT_FOUND'])

        machine_response: MachineSchema = {}
        machine_response['id'] = str(machine['_id'])
        machine_response['name'] = machine['name']
        machine_response['ip'] = machine['ip']
        machine_response['hash'] = machine['hash']
        machine_response['description'] = machine['description']
        machine_response['status'] = machine['status']
        machine_response['last_status_change'] = machine['last_status_change']

        user_response: UserSchema = {}
        user_response['id'] = str(user['_id'])
        user_response['name'] = user['name']
        user_response['email'] = user['email']
        user_response['description'] = user['description']
        user_response['enable'] = user['enable']
        user_response['created_at'] = user['created_at']
        user_response['updated_at'] = user['updated_at']
        user_response['deleted_at'] = user['deleted_at']

        machine_user_response: MachineUserSchema = {}
        machine_user_response['id'] = str(machine_user['_id'])
        machine_user_response['machine'] = machine_response
        machine_user_response['user'] = user_response

        response = {}
        response['success'] = True
        response['message'] = "Machine user found"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['machine_user'] = machine_user_response
        return response
    
    def get_all(self):
        logging.info("Find all machine users")

        list_machine_users: list[MachineUserSchema] = []
        find: list[MachineUserSchema] = self.machine_user_repository.get_all()
        
        if not find:
            raise UserException.user_not_found(['USER_NOT_FOUND'])
        
        for machine_user in find:
            machine: MachineSchema = self.machine_repository.find_one(id=machine_user['machine_id'])

            if not machine:
                raise MachineException.machine_not_found(['MACHINE_NOT_FOUND'])
            
            user: UserSchema = self.user_repository.find_one(id=machine_user['user_id'])

            if not user:
                raise UserException.user_not_found(['USER_NOT_FOUND'])
            
            machine_response: MachineSchema = {}
            machine_response['id'] = str(machine['_id'])
            machine_response['name'] = machine['name']
            machine_response['ip'] = machine['ip']
            machine_response['hash'] = machine['hash']
            machine_response['description'] = machine['description']
            machine_response['status'] = machine['status']
            machine_response['last_status_change'] = machine['last_status_change']
            machine_response['enable'] = machine['enable']
            machine_response['created_at'] = machine['created_at']
            machine_response['updated_at'] = machine['updated_at']
            machine_response['deleted_at'] = machine['deleted_at']

            user_response: UserSchema = {}
            user_response['id'] = str(user['_id'])
            user_response['name'] = user['name']
            user_response['email'] = user['email']
            user_response['description'] = user['description']
            user_response['enable'] = user['enable']
            user_response['created_at'] = user['created_at']
            user_response['updated_at'] = user['updated_at']
            user_response['deleted_at'] = user['deleted_at']

            machine_user_response: MachineUserSchema = {}
            machine_user_response['id'] = str(machine_user['_id'])
            machine_user_response['machine'] = machine_response
            machine_user_response['user'] = user_response
            
            list_machine_users.append(machine_user_response)
        
        response = {}
        response['success'] = True
        response['message'] = "Machine users found"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['machine_users'] = list_machine_users
        return response
    
    def create(self, create: CreateMachineUserInputSchema):
        logging.info("Create machine user with data: %s", create)

        machine = self.machine_repository.find_one(id=create['machine_id'], enable=True)

        if not machine:
            raise MachineException.machine_not_found(['MACHINE_NOT_FOUND'])

        user: UserSchema = self.user_repository.find_one(id=create['user_id'], enable=True)

        if not user:
            raise UserException.user_not_found(['INTERNAL_ERROR_JSON_NOT_CREATED'])
        
        find_machine_user = self.machine_user_repository.find_one(machine_id=create['machine_id'], user_id=create['user_id'], enable=True)

        if find_machine_user:
            raise MachineUserException.machine_user_already_exists(['MACHINE_USER_ALREADY_EXISTS'])
        
        machine_user: MachineUserSchema = self.machine_user_repository.save(**create)

        if not machine_user:
            raise MachineUserException.machine_user_not_found(['MACHINE_USER_NOT_CREATED_IN_DATABASE'])
        

        machine_response: MachineSchema = {}
        machine_response['id'] = str(machine['_id'])
        machine_response['name'] = machine['name']
        machine_response['ip'] = machine['ip']
        machine_response['hash'] = machine['hash']
        machine_response['description'] = machine['description']
        machine_response['status'] = machine['status']
        machine_response['last_status_change'] = machine['last_status_change']
        machine_response['enable'] = machine['enable']
        machine_response['created_at'] = machine['created_at']
        machine_response['updated_at'] = machine['updated_at']
        machine_response['deleted_at'] = machine['deleted_at']
        
        user_response: UserSchema = {}
        user_response['id'] = str(user['_id'])
        user_response['name'] = user['name']
        user_response['email'] = user['email']
        user_response['description'] = user['description']
        user_response['enable'] = user['enable']
        user_response['created_at'] = user['created_at']
        user_response['updated_at'] = user['updated_at']
        user_response['deleted_at'] = user['deleted_at']

        machine_user_response: MachineUserSchema = {}
        machine_user_response['id'] = str(machine_user['_id'])
        machine_user_response['machine'] = machine_response
        machine_user_response['user'] = user_response

        response = {}
        response['success'] = True
        response['message'] = "Machine user created"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['machine_user'] = machine_user_response
        return response

    def update(self, id: str, update: UpdateMachineUserInputSchema):
        logging.info("Update user with id: %s", id)

        find_machine_user = self.machine_user_repository.find_one(id=id, enable=True)

        if not find_machine_user:
            raise MachineUserException.machine_user_not_found(['MACHINE_USER_NOT_FOUND'])
        
        if update.get('machine_id'):
            machine = self.machine_repository.find_one(id=update['machine_id'], enable=True)
            if not machine:
                raise MachineException.machine_not_found(['MACHINE_NOT_FOUND'])
                        
            update['machine_id'] = str(machine['_id'])

        if update.get('user_id'):
            user = self.user_repository.find_one(id=update['user_id'], enable=True)
            if not user:
                raise UserException.user_not_found(['USER_NOT_FOUND'])
            
            
            update['user_id'] = str(user['_id'])

        update_machine_user = self.machine_user_repository.update(id, **update)

        if not update_machine_user:
            raise MachineUserException.machine_user_not_found(['MACHINE_USER_NOT_UPDATED_IN_DATABASE'])
        
        machine_response: MachineSchema = {}
        machine_response['id'] = str(machine['_id'])
        machine_response['name'] = machine['name']
        machine_response['ip'] = machine['ip']
        machine_response['hash'] = machine['hash']
        machine_response['description'] = machine['description']
        machine_response['status'] = machine['status']
        machine_response['last_status_change'] = machine['last_status_change']
        machine_response['enable'] = machine['enable']
        machine_response['created_at'] = machine['created_at']
        machine_response['updated_at'] = machine['updated_at']
        machine_response['deleted_at'] = machine['deleted_at']

        user_response: UserSchema = {}
        user_response['id'] = str(user['_id'])
        user_response['name'] = user['name']
        user_response['email'] = user['email']
        user_response['description'] = user['description']
        user_response['enable'] = user['enable']
        user_response['created_at'] = user['created_at']
        user_response['updated_at'] = user['updated_at']
        user_response['deleted_at'] = user['deleted_at']

        machine_user_response: MachineUserSchema = {}
        machine_user_response['id'] = str(update_machine_user['_id'])
        machine_user_response['machine'] = machine_response
        machine_user_response['user'] = user_response

        response = {}
        response['success'] = True
        response['message'] = "Machine user updated"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['machine_user'] = machine_user_response
        return response

    def delete(self, id: str):
        logging.info("Delete machine user with id: %s", id)
        exist_machine_user: MachineUserSchema = self.machine_user_repository.find_one(id=id, enable=True)

        if not exist_machine_user:
            raise MachineUserException.machine_user_not_found(['MACHINE_USER_NOT_FOUND'])
        
        machine_user: MachineUserSchema = self.machine_user_repository.delete(id)

        if not machine_user:
            raise MachineUserException.machine_user_not_found(['MACHINE_USER_NOT_DELETED_IN_DATABASE'])
        
        user: UserSchema = self.user_repository.find_one(id=machine_user['user_id'], enable=True)

        if not user:
            raise UserException.user_not_found(['USER_NOT_FOUND'])
        
        machine: MachineSchema = self.machine_repository.find_one(id=machine_user['machine_id'], enable=True)

        if not machine:
            raise MachineException.machine_not_found(['MACHINE_NOT_FOUND'])
        
        machine_response: MachineSchema = {}
        machine_response['id'] = str(machine['_id'])
        machine_response['name'] = machine['name']
        machine_response['ip'] = machine['ip']
        machine_response['hash'] = machine['hash']
        machine_response['description'] = machine['description']
        machine_response['status'] = machine['status']
        machine_response['last_status_change'] = machine['last_status_change']
        machine_response['enable'] = machine['enable']
        machine_response['created_at'] = machine['created_at']
        machine_response['updated_at'] = machine['updated_at']
        machine_response['deleted_at'] = machine['deleted_at']

        user_response: UserSchema = {}
        user_response['id'] = str(user['_id'])
        user_response['name'] = user['name']
        user_response['email'] = user['email']
        user_response['description'] = user['description']
        user_response['enable'] = user['enable']
        user_response['created_at'] = user['created_at']
        user_response['updated_at'] = user['updated_at']
        user_response['deleted_at'] = user['deleted_at']

        machine_user_response: MachineUserSchema = {}
        machine_user_response['id'] = str(machine_user['_id'])
        machine_user_response['machine'] = machine_response
        machine_user_response['user'] = user_response

        response = {}
        response['success'] = True
        response['message'] = "Machine user deleted"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['machine_user'] = machine_user_response
        return response