from os import getenv
from dotenv import load_dotenv
load_dotenv()

from ..dto import MainOutputSchema

class MainService:

    @staticmethod
    def start() -> MainOutputSchema:
        response: MainOutputSchema = {}
        response["success"] = True
        response["message"] = "Server running correctly"
        response["version"] = str(getenv("VERSION"))
        return response