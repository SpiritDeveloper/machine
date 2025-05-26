from fastapi import APIRouter
from ..services.machine_report_service import MachineReportService
from ..utils.documentation import Documentation
from ..config.dto.types import RequestMethodEnum
from ..dto import CreateMachineReportInputSchema, CreateMachineReportInput, UpdateMachineReportInputSchema, UpdateMachineReportInput
machine_report = APIRouter(prefix="/machine-report", tags=["machine-report"])

class MachineReportController:
    get_machine_report_by_id_documentation = Documentation.create(
        message="Get information of machine report by id",
        method=RequestMethodEnum.GET,
        payload={},
        authorization=True,
    )

    @machine_report.get(
        "/get/{id}",
        description="Returns a machine report by id",
        responses=get_machine_report_by_id_documentation,
    )
    def get_machine_report(id: str):
        return MachineReportService().get(id)

    get_all_machine_reports_documentation = Documentation.create(
        message="Get all machine reports",
        method=RequestMethodEnum.GET,
        payload={},
        authorization=True,
    )

    @machine_report.get(
        "/get",
        description="Returns all users",
        responses=get_all_machine_reports_documentation,
    )
    def get_all_machine_reports():
        return MachineReportService().get_all()

    create_machine_report_documentation = Documentation.create(
        message="Create a new machine report",
        method=RequestMethodEnum.POST,
        payload={},
        authorization=True,
    )

    @machine_report.post(
        "/create",
        description="Creates a new machine report",
        responses=create_machine_report_documentation,
    )
    def create_new_machine_report(create: CreateMachineReportInputSchema):
        create: CreateMachineReportInputSchema = CreateMachineReportInput.create(create)
        return MachineReportService().create(create)

    update_machine_report_documentation = Documentation.create(
        message="Update a machine report",
        method=RequestMethodEnum.PUT,
        payload={},
        authorization=True,
    )

    @machine_report.put(
        "/update/{id}",
        description="Updates a user",
        responses=update_machine_report_documentation,
    )
    def update_machine_report(id: str, update: UpdateMachineReportInputSchema):
        update: UpdateMachineReportInputSchema = UpdateMachineReportInput.create(update)
        return MachineReportService().update(id, update)

    delete_machine_report_documentation = Documentation.create(
        message="Delete a machine report",
        method=RequestMethodEnum.DELETE,
        payload={},
        authorization=True,
    )

    @machine_report.delete(
        "/delete/{id}",
        description="Deletes a machine report",
        responses=delete_machine_report_documentation,
    )
    def delete_machine_report(id: str):
        return MachineReportService().delete(id)