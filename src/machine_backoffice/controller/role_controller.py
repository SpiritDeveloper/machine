from fastapi import APIRouter
from ..services.role_service import RoleService
from ..utils.documentation import Documentation
from ..config.dto.types import RequestMethodEnum
from ..dto import CreateRoleInput, CreateRoleInputSchema, UpdateRoleInput, UpdateRoleInputSchema

role = APIRouter(prefix="/role", tags=["role"])


class RoleController:
    get_role_by_id_documentation = Documentation.create(
        message="Get information of role by id",
        method=RequestMethodEnum.GET,
        payload={},
        authorization=True,
    )

    @role.get(
        "/get/{id}",
        description="Returns a role by id",
        responses=get_role_by_id_documentation,
    )
    def get_role(id: str):
        return RoleService().get(id)

    get_all_roles_documentation = Documentation.create(
        message="Get all roles",
        method=RequestMethodEnum.GET,
        payload={},
        authorization=True,
    )

    @role.get(
        "/get",
        description="Returns all roles",
        responses=get_all_roles_documentation,
    )
    def get_all_roles():
        return RoleService().get_all()

    create_role_documentation = Documentation.create(
        message="Create a new role",
        method=RequestMethodEnum.POST,
        payload={},
        authorization=True,
    )

    @role.post(
        "/create",
        description="Creates a new role",
        responses=create_role_documentation,
    )
    def create_new_role(create: CreateRoleInputSchema):
        create: CreateRoleInputSchema = CreateRoleInput.create(create)
        return RoleService().create(create)

    update_role_documentation = Documentation.create(
        message="Update a role",
        method=RequestMethodEnum.PUT,
        payload={},
        authorization=True,
    )

    @role.put(
        "/update/{id}",
        description="Updates a role",
        responses=update_role_documentation,
    )
    def update_role(id: str, update: UpdateRoleInputSchema):
        update: UpdateRoleInputSchema = UpdateRoleInput.create(update)
        return RoleService().update(id, update)

    delete_role_documentation = Documentation.create(
        message="Delete a role",
        method=RequestMethodEnum.DELETE,
        payload={},
        authorization=True,
    )

    @role.delete(
        "/delete/{id}",
        description="Deletes a role",
        responses=delete_role_documentation,
    )
    def delete_role(id: str):
        return RoleService().delete(id)