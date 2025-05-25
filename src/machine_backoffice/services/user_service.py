from ..models import UserModel, RoleModel
from ..exceptions.user_exception import UserException
from ..exceptions.role_exception import RoleException
from ..dto import CreateUserSchemaInput, CreateUserInputSchema, UserSchema, RoleSchema, UpdateUserInputSchema, UpdateUserInput
import logging


class UserService:
    def __init__(self):
        self.user_repository = UserModel()
        self.role_repository = RoleModel()

    def get(self, id: str):
        logging.info("Find psp by id with id: %s", id)
        
        user: UserSchema = self.user_repository.find_one(id=id, enable=True)

        if not user:
            raise UserException.user_not_found(['USER_NOT_FOUND'])
        
        role: RoleSchema = self.role_repository.find_one(id=user['role_id'])

        if not role:
            raise RoleException.role_not_found(['ROLE_NOT_FOUND'])

        user_response: UserSchema = {}
        user_response['id'] = str(user['_id'])
        user_response['name'] = user['name']
        user_response['email'] = user['email']
        user_response['description'] = user['description']
        user_response['enable'] = user['enable']
        user_response['created_at'] = user['created_at']
        user_response['updated_at'] = user['updated_at']
        user_response['deleted_at'] = user['deleted_at']
        user_response['role'] = {}
        user_response['role']['id'] = str(role['_id'])
        user_response['role']['name'] = role['name']
        user_response['role']['description'] = role['description']
        user_response['role']['enable'] = role['enable']
        user_response['role']['created_at'] = role['created_at']
        user_response['role']['updated_at'] = role['updated_at']
        user_response['role']['deleted_at'] = role['deleted_at']

        response = {}
        response['success'] = True
        response['message'] = "User found"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['user'] = user_response
        return response

    def get_all(self):
        logging.info("Find all users")
        list_users: list[UserSchema] = []
        find: list[UserSchema] = self.user_repository.get_all()
        
        if not find:
            raise UserException.user_not_found(['USER_NOT_FOUND'])
        
        for user in find:
            role: RoleSchema = self.role_repository.find_one(id=user['role_id'])

            if not role:
                raise RoleException.role_not_found(['ROLE_NOT_FOUND'])
            
            list_users.append({
                'id': str(user['_id']),
                'name': user['name'],
                'email': user['email'],
                'description': user['description'],
                'enable': user['enable'],
                'created_at': user['created_at'],
                'updated_at': user['updated_at'],
                'deleted_at': user['deleted_at'],
                'role': {
                    'id': str(role['_id']),
                    'name': role['name'],
                    'description': role['description'],
                    'enable': role['enable'],
                    'created_at': role['created_at'],
                    'updated_at': role['updated_at'],
                    'deleted_at': role['deleted_at']
                }
            })
        
        response = {}
        response['success'] = True
        response['message'] = "Users found"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['users'] = list_users
        return response

    def create(self, create: CreateUserInputSchema):
        logging.info("Create user with data: %s", create)

        role = self.role_repository.find_one(id=create['role_id'], enable=True)

        if not role:
            raise RoleException.role_not_found(['ROLE_NOT_FOUND'])

        user: UserSchema = CreateUserSchemaInput.create(create)

        if not user:
            raise UserException.user_not_found(['INTERNAL_ERROR_JSON_NOT_CREATED'])
        
        exist_user: UserSchema = self.user_repository.find_one(email=user['email'])

        if exist_user:
            raise UserException.user_already_exists(['USER_ALREADY_EXISTS'])
        
        new_user: UserSchema = self.user_repository.save(**user)

        if not new_user:
            raise UserException.user_not_found(['USER_NOT_CREATED_IN_DATABASE'])
        
        user_response: UserSchema = {}
        user_response['id'] = str(new_user['_id'])
        user_response['name'] = new_user['name']
        user_response['email'] = new_user['email']
        user_response['description'] = new_user['description']
        user_response['enable'] = new_user['enable']
        user_response['created_at'] = new_user['created_at']
        user_response['updated_at'] = new_user['updated_at']
        user_response['deleted_at'] = new_user['deleted_at']
        user_response['role'] = {
            'id': str(role['_id']),
            'name': role['name'],
            'description': role['description'],
            'enable': role['enable'],
            'created_at': role['created_at'],
            'updated_at': role['updated_at'],
            'deleted_at': role['deleted_at']
        }


        response = {}
        response['success'] = True
        response['message'] = "User created"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['user'] = user_response
        return response

    def update(self, id: str, update: UpdateUserInputSchema):
        logging.info("Update user with id: %s", id)
        
        if update.get('role_id'):
            role = self.role_repository.find_one(id=update['role_id'], enable=True)
            if not role:
                raise RoleException.role_not_found(['ROLE_NOT_FOUND'])
            
            update['role_id'] = str(role['_id'])

        if update.get('email'):
            exist_user: UserSchema = self.user_repository.find_one(email=update['email'], enable=True)
            if exist_user:
                raise UserException.user_already_exists(['USER_ALREADY_EXISTS'])
            
        user: UserSchema = self.user_repository.update(id, **update)

        if not user:
            raise UserException.user_not_found(['USER_NOT_UPDATED_IN_DATABASE'])
        
        role: RoleSchema = self.role_repository.find_one(id=user['role_id'], enable=True)

        if not role:
            raise RoleException.role_not_found(['ROLE_NOT_FOUND'])
        
        update_user: UserSchema = {}
        update_user['id'] = str(user['_id'])
        update_user['name'] = user['name']
        update_user['email'] = user['email']
        update_user['description'] = user['description']
        update_user['enable'] = user['enable']
        update_user['created_at'] = user['created_at']
        update_user['updated_at'] = user['updated_at']
        update_user['deleted_at'] = user['deleted_at']
        update_user['role'] = {
            'id': str(role['_id']),
            'name': role['name'],
            'description': role['description'],
            'enable': role['enable'],
            'created_at': role['created_at'],
            'updated_at': role['updated_at'],
            'deleted_at': role['deleted_at']
        }

        response = {}
        response['success'] = True
        response['message'] = "User updated"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['user'] = update_user
        return response

    def delete(self, id: str):
        logging.info("Delete psp with id: %s", id)

        exist_user: UserSchema = self.user_repository.find_one(id=id, enable=True)

        if not exist_user:
            raise UserException.user_not_found(['USER_NOT_FOUND'])
        
        user: UserSchema = self.user_repository.delete(id)

        if not user:
            raise UserException.user_not_found(['USER_NOT_DELETED_IN_DATABASE'])
        
        role: RoleSchema = self.role_repository.find_one(id=user['role_id'], enable=True)

        if not role:
            raise RoleException.role_not_found(['ROLE_NOT_FOUND'])
        
        user_response: UserSchema = {}
        user_response['id'] = str(user['_id'])
        user_response['name'] = user['name']
        user_response['email'] = user['email']
        user_response['description'] = user['description']
        user_response['enable'] = user['enable']
        user_response['created_at'] = user['created_at']
        user_response['updated_at'] = user['updated_at']
        user_response['deleted_at'] = user['deleted_at']
        user_response['role'] = {
            'id': str(role['_id']),
            'name': role['name'],
            'description': role['description'],
            'enable': role['enable'],
            'created_at': role['created_at'],
            'updated_at': role['updated_at'],
            'deleted_at': role['deleted_at']
        }

        response = {}
        response['success'] = True
        response['message'] = "User deleted"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['user'] = user_response
        return response
