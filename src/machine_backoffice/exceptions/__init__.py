from fastapi import HTTPException

class Error(HTTPException):
    def __init__(self, code, message, errors: str = '') -> HTTPException:
        response = {}
        response["success"] = False
        response["message"] = str(message)
        response["errors"] = errors
        response["payload"] = {}
        raise HTTPException(status_code=code, detail=response)