from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class CreateMachineReportInputSchema(BaseModel):
    date_failure: Optional[datetime] = Field(description="machine report date failure", example=datetime.now(), default=None)
    date_start: Optional[datetime] = Field(description="machine report date start", example=datetime.now(), default=None)
    date_end: Optional[datetime] = Field(description="machine report date end", example=datetime.now(), default=None)
    time_failure: Optional[int] = Field(description="machine report time failure", example=75, default=None)
    time_start: Optional[datetime] = Field(description="machine report start time", example=datetime.now(), default=None)
    time_end: Optional[datetime] = Field(description="machine report end time", example=datetime.now(), default=None)
    machine_id: Optional[str] = Field(description="machine id", example="1234567890", default=None)
    user_report_id: Optional[str] = Field(description="user report id", example="1234567890", default=None)
    description: Optional[str] = Field(description="machine report description", example="machine report description", default=None)


class CreateMachineReportInput:
    def create(input: CreateMachineReportInputSchema):
        return jsonable_encoder(input, exclude_none=True)
