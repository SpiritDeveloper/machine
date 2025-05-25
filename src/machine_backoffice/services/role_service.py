from ..models import RoleModel
from ..dto import CreateRoleSchemaInput, CreateRoleInputSchema, RoleSchema, UpdateRoleInputSchema, UpdateRoleInput
from ..exceptions.role_exception import RoleException
import logging


class RoleService:
    def __init__(self):
        self.role_repository = RoleModel()

    def get(self, id: str):
        logging.info("Find role by id with id: %s", id)
        
        role: RoleSchema = self.role_repository.find_one(id=id, enable=True)

        if not role:
            raise RoleException.role_not_found(['ROLE_NOT_FOUND'])
        
        response_role: RoleSchema = {}
        response_role['id'] = str(role['_id'])
        response_role['name'] = role['name']
        response_role['description'] = role['description']
        response_role['enable'] = role['enable']
        response_role['created_at'] = role['created_at']
        response_role['updated_at'] = role['updated_at']
        response_role['deleted_at'] = role['deleted_at']

        response = {}
        response['success'] = True
        response['message'] = "Role found"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['role'] = response_role
        return response

    def get_all(self):
        logging.info("Find all roles")
        list_roles: list[RoleSchema] = self.role_repository.get_all()
        
        if not list_roles:
            raise RoleException.role_not_found(['ROLE_NOT_FOUND'])
        
        response_roles: list[RoleSchema] = []

        for role in list_roles:
            rol = {}
            rol['id'] = str(role['_id'])
            rol['name'] = role['name']
            rol['description'] = role['description']
            rol['enable'] = role['enable']
            rol['created_at'] = role['created_at']
            rol['updated_at'] = role['updated_at']
            rol['deleted_at'] = role['deleted_at']
            response_roles.append(rol)
        
        response = {}
        response['success'] = True
        response['message'] = "Roles found"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['roles'] = response_roles
        return response

    def create(self, create: CreateRoleInputSchema):
        logging.info("Create role with data: %s", create)

        new_role = CreateRoleSchemaInput.create(create)

        find: RoleSchema = self.role_repository.find_one(name=new_role['name'])

        if find:
            raise RoleException.role_already_exists(['ROLE_ALREADY_EXISTS'])
        
        new_role: RoleSchema = self.role_repository.save(**new_role)

        if not new_role:
            raise RoleException.role_not_found()
        
        logging.info("Create role with data: %s", new_role)

        response: RoleSchema = {}
        response['id'] = str(new_role['_id'])
        response['name'] = new_role['name']
        response['description'] = new_role['description']
        response['enable'] = new_role['enable']
        response['created_at'] = new_role['created_at']
        response['updated_at'] = new_role['updated_at']
        response['deleted_at'] = new_role['deleted_at']

        return response

    def update(self, id: str, update: UpdateRoleInputSchema):
        logging.info("Update role with id: %s", id)
        
        exist_role: RoleSchema = self.role_repository.find_one(id=id, enable=True)

        if not exist_role:
            raise RoleException.role_not_found(['ROLE_NOT_FOUND'])
        
        if update.get('name'):
            exist_role_name: RoleSchema = self.role_repository.find_one(name=update['name'], enable=True)

            if exist_role_name:
                raise RoleException.role_already_exists(['ROLE_ALREADY_EXISTS'])
        
        update_role: RoleSchema = self.role_repository.update(id, **update)

        if not update_role:
            raise RoleException.role_not_found(['ROLE_NOT_UPDATED_IN_DATABASE'])
        
        response_role: RoleSchema = {}
        response_role['id'] = str(update_role['_id'])
        response_role['name'] = update_role['name']
        response_role['description'] = update_role['description']
        response_role['enable'] = update_role['enable']
        response_role['created_at'] = update_role['created_at']
        response_role['updated_at'] = update_role['updated_at']
        response_role['deleted_at'] = update_role['deleted_at']
        
        response = {}
        response['success'] = True
        response['message'] = "Role updated"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['role'] = response_role
        return response
    
    def delete(self, id: str):
        logging.info("Delete role with id: %s", id)
        
        exist_role: RoleSchema = self.role_repository.find_one(id=id, enable=True)

        if not exist_role:
            raise RoleException.role_not_found(['ROLE_NOT_FOUND'])
        
        delete_role: RoleSchema = self.role_repository.delete(id)
        
        if not delete_role:
            raise RoleException.role_not_found(['ROLE_NOT_DELETED_IN_DATABASE'])
        
        response_role: RoleSchema = {}
        response_role['id'] = str(delete_role['_id'])
        response_role['name'] = delete_role['name']
        response_role['description'] = delete_role['description']
        response_role['enable'] = delete_role['enable']
        response_role['created_at'] = delete_role['created_at']
        response_role['updated_at'] = delete_role['updated_at']
        response_role['deleted_at'] = delete_role['deleted_at']

        response = {}
        response['success'] = True
        response['message'] = "Role deleted"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['role'] = response_role
        return response