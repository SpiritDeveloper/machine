from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, ValidationError
from ...exceptions.machine_report_exception import MachineReportException
from datetime import datetime
import uuid

class MachineReportSchema(BaseModel):
    date_failure: datetime = Field(description="machine report date failure", example=datetime.now(), required=True)
    date_start: datetime = Field(description="machine report date start", example=datetime.now(), required=True)
    date_end: datetime = Field(description="machine report date end", example=datetime.now(), required=True)
    time_failure: int = Field(description="machine report time failure", example=75, required=True)
    time_start: datetime = Field(description="machine report start time", example=datetime.now(), required=True)
    time_end: datetime = Field(description="machine report end time", example=datetime.now(), required=True)
    machine_id: str = Field(description="machine id", example="1234567890", required=True)
    user_report_id: str = Field(description="user report id", example="1234567890", required=True)
    description: str = Field(description="machine report description", example="machine report description", required=True)
    enable: bool = Field(description="machine report enable", example=True, default=True)
    created_at: datetime = Field(description="machine report created at", example=datetime.now(), default=datetime.now())
    updated_at: datetime = Field(description="machine report updated at", example=datetime.now(), default=datetime.now())
    deleted_at: datetime = Field(description="machine report deleted at", example=datetime.now(), default=None)

class CreateMachineReportSchemaInput:
    def create(input: MachineReportSchema):
        try:
            return jsonable_encoder(MachineReportSchema(**input))
        except ValidationError as e:
            missing_fields = [error["loc"][0] for error in e.errors()]
            raise MachineReportException.missing_fields(missing_fields)