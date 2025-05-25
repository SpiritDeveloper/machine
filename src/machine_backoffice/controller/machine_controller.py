from fastapi import APIRouter
from ..services.machine_service import MachineService
from ..utils.documentation import Documentation
from ..config.dto.types import RequestMethodEnum

machine = APIRouter(prefix="/machine", tags=["machine"])


class MachineController:
    get_machine_by_id_documentation = Documentation.create(
        message="Get information of machine by id",
        method=RequestMethodEnum.GET,
        payload={},
        authorization=True,
    )

    @machine.get(
        "/get/{id}",
        description="Returns a machine by id",
        responses=get_machine_by_id_documentation,
    )
    def get_machine(id: str):
        return MachineService().get(id)

    get_all_machines_documentation = Documentation.create(
        message="Get all machines",
        method=RequestMethodEnum.GET,
        payload={},
        authorization=True,
    )

    @machine.get(
        "/get",
        description="Returns all machines",
        responses=get_all_machines_documentation,
    )
    def get_all_machines():
        return MachineService().get_all()

    create_machine_documentation = Documentation.create(
        message="Create a new machine",
        method=RequestMethodEnum.POST,
        payload={},
        authorization=True,
    )

    @machine.post(
        "/create",
        description="Creates a new country",
        responses=create_machine_documentation,
    )
    def create_new_machine(create: dict):
        return MachineService().create(create)

    update_machine_documentation = Documentation.create(
        message="Update a machine",
        method=RequestMethodEnum.PUT,
        payload={},
        authorization=True,
    )

    @machine.put(
        "/update/{id}",
        description="Updates a machine",
        responses=update_machine_documentation,
    )
    def update_machine(id: str, update: dict):
        return MachineService().update(id, update)

    delete_machine_documentation = Documentation.create(
        message="Delete a machine",
        method=RequestMethodEnum.DELETE,
        payload={},
        authorization=True,
    )

    @machine.delete(
        "/delete/{id}",
        description="Deletes a machine",
        responses=delete_machine_documentation,
    )
    def delete_machine(id: str):
        return MachineService().delete(id)