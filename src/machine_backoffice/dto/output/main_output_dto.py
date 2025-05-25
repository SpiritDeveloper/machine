from abc import abstractmethod
from os import getenv
from pydantic import BaseModel, Field

class MainOutputSchema(BaseModel):
    message: str = Field(
        description="Displays the server status",
        example="Server running correctly",
    )
    version: str  = Field(
        description="Displays the running version of the server",
        example="1.0.0",
    )

class MainOutput():
    @abstractmethod
    def create() -> MainOutputSchema:

        response: MainOutputSchema = {}
        response['success'] = True
        response['message'] = 'Running ...'
        response['version'] = getenv("VERSION")

        return response