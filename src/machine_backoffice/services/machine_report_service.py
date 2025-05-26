from ..models import MachineReportModel, MachineModel
from ..dto import MachineReportSchema, MachineSchema, CreateMachineReportSchemaInput, UpdateMachineReportInputSchema
from ..exceptions.machine_report_exception import MachineReportException
from ..exceptions.machine_exception import MachineException
import logging


class MachineReportService:
    def __init__(self):
        self.machine_report_repository = MachineReportModel()
        self.machine_repository = MachineModel()

    def get(self, id: str):
        logging.info("Find machine report by id with id: %s", id)

        machine_report: MachineReportSchema = self.machine_report_repository.find_one(id=id, enable=True)

        if not machine_report:
            raise MachineReportException.machine_report_not_found(['MACHINE_REPORT_NOT_FOUND'])
        
        machine: MachineSchema = self.machine_repository.find_one(id=machine_report['machine_id'])

        if not machine:
            raise MachineException.machine_not_found(['MACHINE_NOT_FOUND'])

        machine_report_response: MachineReportSchema = {}
        machine_report_response['id'] = str(machine_report['_id'])
        machine_report_response['date_failure'] = machine_report['date_failure']
        machine_report_response['date_start'] = machine_report['date_start']
        machine_report_response['date_end'] = machine_report['date_end']
        machine_report_response['time_failure'] = machine_report['time_failure']
        machine_report_response['time_start'] = machine_report['time_start']
        machine_report_response['time_end'] = machine_report['time_end']
        machine_report_response['description'] = machine_report['description']
        machine_report_response['enable'] = machine_report['enable']
        machine_report_response['created_at'] = machine_report['created_at']
        machine_report_response['updated_at'] = machine_report['updated_at']
        machine_report_response['deleted_at'] = machine_report['deleted_at']
        machine_report_response['machine'] = {}
        machine_report_response['machine']['id'] = str(machine['_id'])
        machine_report_response['machine']['name'] = machine['name']
        machine_report_response['machine']['ip'] = machine['ip']
        machine_report_response['machine']['hash'] = machine['hash']
        machine_report_response['machine']['description'] = machine['description']
        machine_report_response['machine']['enable'] = machine['enable']
        machine_report_response['machine']['created_at'] = machine['created_at']
        machine_report_response['machine']['updated_at'] = machine['updated_at']
        machine_report_response['machine']['deleted_at'] = machine['deleted_at']

        response = {}
        response['success'] = True
        response['message'] = "Machine report found"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['machine_report'] = machine_report_response
        return response

    def get_all(self):
        logging.info("Find all machine reports")

        list_machine_reports: list[MachineReportSchema] = []

        find: list[MachineReportSchema] = self.machine_report_repository.get_all()
        
        if not find:
            raise MachineReportException.machine_report_not_found(['MACHINE_REPORT_NOT_FOUND'])
        
        for machine_report in find:
            machine: MachineSchema = self.machine_repository.find_one(id=machine_report['machine_id'])

            if not machine:
                raise MachineException.machine_not_found(['MACHINE_NOT_FOUND'])
            
            list_machine_reports.append({
                'id': str(machine_report['_id']),
                'date_failure': machine_report['date_failure'],
                'date_start': machine_report['date_start'],
                'date_end': machine_report['date_end'],
                'time_failure': machine_report['time_failure'],
                'time_start': machine_report['time_start'],
                'time_end': machine_report['time_end'],
                'description': machine_report['description'],
                'enable': machine_report['enable'],
                'created_at': machine_report['created_at'],
                'updated_at': machine_report['updated_at'],
                'deleted_at': machine_report['deleted_at'],
                'machine': {
                    'id': str(machine['_id']),
                    'name': machine['name'],
                    'ip': machine['ip'],
                    'hash': machine['hash'],
                    'description': machine['description'],
                    'enable': machine['enable'],
                    'created_at': machine['created_at'],
                    'updated_at': machine['updated_at'],
                    'deleted_at': machine['deleted_at']
                }
            })
        
        response = {}
        response['success'] = True
        response['message'] = "Machine reports found"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['machine_reports'] = list_machine_reports
        return response

    def create(self, create: CreateMachineReportSchemaInput):
        logging.info("Create machine report with data: %s", create)
        
        machine = self.machine_repository.find_one(id=create['machine_id'], enable=True)

        if not machine:
            raise MachineException.machine_not_found(['MACHINE_NOT_FOUND'])

        machine_report: MachineReportSchema = CreateMachineReportSchemaInput.create(create)

        if not machine_report:
            raise MachineReportException.machine_report_not_found(['INTERNAL_ERROR_JSON_NOT_CREATED'])
        
        new_machine_report: MachineReportSchema = self.machine_report_repository.save(**machine_report)

        if not new_machine_report:
            raise MachineReportException.machine_report_not_found(['MACHINE_REPORT_NOT_CREATED_IN_DATABASE'])
        
        machine_report_response: MachineReportSchema = {}
        machine_report_response['id'] = str(new_machine_report['_id'])
        machine_report_response['date_failure'] = new_machine_report['date_failure']
        machine_report_response['date_start'] = new_machine_report['date_start']
        machine_report_response['date_end'] = new_machine_report['date_end']
        machine_report_response['time_failure'] = new_machine_report['time_failure']
        machine_report_response['time_start'] = new_machine_report['time_start']
        machine_report_response['time_end'] = new_machine_report['time_end']
        machine_report_response['description'] = new_machine_report['description']
        machine_report_response['enable'] = new_machine_report['enable']
        machine_report_response['created_at'] = new_machine_report['created_at']
        machine_report_response['updated_at'] = new_machine_report['updated_at']
        machine_report_response['deleted_at'] = new_machine_report['deleted_at']
        machine_report_response['machine'] = {
            'id': str(machine['_id']),
            'name': machine['name'],
            'ip': machine['ip'],
            'hash': machine['hash'],
            'description': machine['description'],
            'enable': machine['enable'],
            'created_at': machine['created_at'],
            'updated_at': machine['updated_at'],
            'deleted_at': machine['deleted_at']
        }


        response = {}
        response['success'] = True
        response['message'] = "Machine report created"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['machine_report'] = machine_report_response
        return response

    def update(self, id: str, update: UpdateMachineReportInputSchema):
        logging.info("Update machine report with id: %s", id)

        if update.get('machine_id'):
            exist_machine: MachineSchema = self.machine_repository.find_one(id=update['machine_id'], enable=True)
            if exist_machine:
                raise MachineException.machine_already_exists(['MACHINE_ALREADY_EXISTS'])
            
        machine_report: MachineReportSchema = self.machine_report_repository.update(id, **update)

        if not machine_report:
            raise MachineReportException.machine_report_not_found(['MACHINE_REPORT_NOT_UPDATED_IN_DATABASE'])
        
        machine: MachineSchema = self.machine_repository.find_one(id=machine_report['machine_id'], enable=True)

        if not machine:
            raise MachineException.machine_not_found(['MACHINE_NOT_FOUND'])
        
        update_machine_report: MachineReportSchema = {}
        update_machine_report['id'] = str(machine_report['_id'])
        update_machine_report['name'] = machine_report['name']
        update_machine_report['date_failure'] = machine_report['date_failure']
        update_machine_report['date_start'] = machine_report['date_start']
        update_machine_report['date_end'] = machine_report['date_end']
        update_machine_report['time_failure'] = machine_report['time_failure']
        update_machine_report['time_start'] = machine_report['time_start']
        update_machine_report['time_end'] = machine_report['time_end']
        update_machine_report['description'] = machine_report['description']
        update_machine_report['enable'] = machine_report['enable']
        update_machine_report['created_at'] = machine_report['created_at']
        update_machine_report['updated_at'] = machine_report['updated_at']
        update_machine_report['deleted_at'] = machine_report['deleted_at']
        update_machine_report['machine'] = {
            'id': str(machine['_id']),
            'name': machine['name'],
            'ip': machine['ip'],
            'hash': machine['hash'],
            'description': machine['description'],
            'enable': machine['enable'],
            'created_at': machine['created_at'],
            'updated_at': machine['updated_at'],
            'deleted_at': machine['deleted_at']
        }

        response = {}
        response['success'] = True
        response['message'] = "Machine report updated"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['machine_report'] = update_machine_report
        return response

    def delete(self, id: str):
        logging.info("Delete machine report with id: %s", id)

        exist_machine_report: MachineReportSchema = self.machine_report_repository.find_one(id=id, enable=True)

        if not exist_machine_report:
            raise MachineReportException.machine_report_not_found(['MACHINE_REPORT_NOT_FOUND'])
        
        machine_report: MachineReportSchema = self.machine_report_repository.delete(id)

        if not machine_report:
            raise MachineReportException.machine_report_not_found(['MACHINE_REPORT_NOT_DELETED_IN_DATABASE'])
        
        machine: MachineSchema = self.machine_repository.find_one(id=machine_report['machine_id'], enable=True)

        if not machine:
            raise MachineException.machine_not_found(['MACHINE_NOT_FOUND'])
        
        machine_report_response: MachineReportSchema = {}
        machine_report_response['id'] = str(machine_report['_id'])
        machine_report_response['date_failure'] = machine_report['date_failure']
        machine_report_response['date_start'] = machine_report['date_start']
        machine_report_response['date_end'] = machine_report['date_end']
        machine_report_response['time_failure'] = machine_report['time_failure']
        machine_report_response['time_start'] = machine_report['time_start']
        machine_report_response['time_end'] = machine_report['time_end']
        machine_report_response['description'] = machine_report['description']
        machine_report_response['enable'] = machine_report['enable']
        machine_report_response['created_at'] = machine_report['created_at']
        machine_report_response['updated_at'] = machine_report['updated_at']
        machine_report_response['deleted_at'] = machine_report['deleted_at']
        machine_report_response['machine'] = {
            'id': str(machine['_id']),
            'name': machine['name'],
            'ip': machine['ip'],
            'hash': machine['hash'],
            'description': machine['description'],
            'enable': machine['enable'],
            'created_at': machine['created_at'],
            'updated_at': machine['updated_at'],
            'deleted_at': machine['deleted_at']
        }

        response = {}
        response['success'] = True
        response['message'] = "User deleted"
        response['errors'] = []
        response['payload'] = {}
        response['payload']['machine_report'] = machine_report_response
        return response

    def get_report_by_machine_id(self, machine_id: str):
        logging.info("Get report by machine id: %s", machine_id)

        reports = self.machine_report_repository.get_all()

        list_reports = []

        for report in reports:
            if str(report['machine_id']) == str(machine_id):
                list_reports.append({
                    'id': str(report['_id']),
                    'date_failure': report['date_failure'],
                    'date_start': report['date_start'],
                    'date_end': report['date_end'],
                    'time_failure': report['time_failure'],
                    'time_start': report['time_start'],
                    'time_end': report['time_end'],
                    'description': report['description'],
                    'enable': report['enable'],
                    'created_at': report['created_at'],
                    'updated_at': report['updated_at'],
                    'deleted_at': report['deleted_at'],
                })

        return list_reports