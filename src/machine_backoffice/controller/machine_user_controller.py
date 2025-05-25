from fastapi import APIRouter
from ..services.machine_user_service import MachineUserService
from ..utils.documentation import Documentation
from ..config.dto.types import RequestMethodEnum

machine_user = APIRouter(prefix="/machine-user", tags=["machine-user"])


class MachineUserController:
    get_machine_user_by_id_documentation = Documentation.create(
        message="Get information of machine user by id",
        method=RequestMethodEnum.GET,
        payload={},
        authorization=True,
    )

    @machine_user.get(
        "/get/{id}",
        description="Returns a machine user by id",
        responses=get_machine_user_by_id_documentation,
    )
    def get_machine_user(id: str):
        return MachineUserService().get(id)

    get_all_machine_users_documentation = Documentation.create(
        message="Get all machine users",
        method=RequestMethodEnum.GET,
        payload={},
        authorization=True,
    )

    @machine_user.get(
        "/get",
        description="Returns all machine users",
        responses=get_all_machine_users_documentation,
    )
    def get_all_machine_users():
        return MachineUserService().get_all()

    create_machine_user_documentation = Documentation.create(
        message="Create a new machine user",
        method=RequestMethodEnum.POST,
        payload={},
        authorization=True,
    )

    @machine_user.post(
        "/create",
        description="Creates a new machine user",
        responses=create_machine_user_documentation,
    )
    def create_new_machine_user(create: dict):
        return MachineUserService().create(create)

    update_machine_user_documentation = Documentation.create(
        message="Update a machine user",
        method=RequestMethodEnum.PUT,
        payload={},
        authorization=True,
    )

    @machine_user.put(
        "/update/{id}",
        description="Updates a machine user",
        responses=update_machine_user_documentation,
    )
    def update_machine_user(id: str, update: dict):
        return MachineUserService().update(id, update)

    delete_machine_user_documentation = Documentation.create(
        message="Delete a machine user",
        method=RequestMethodEnum.DELETE,
        payload={},
        authorization=True,
    )

    @machine_user.delete(
        "/delete/{id}",
        description="Deletes a machine user",
        responses=delete_machine_user_documentation,
    )
    def delete_machine_user(id: str):
        return MachineUserService().delete(id)