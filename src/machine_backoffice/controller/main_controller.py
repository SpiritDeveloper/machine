from fastapi import APIRouter
from ..dto import (
    MainOutput
)
from ..services.main_service import MainService

main = APIRouter(prefix="/main", tags=["Main"])

@main.get(
    "/",
    description="The main endpoint that triggers the start method in the mainService and returns a MainOutput object",
)
async def start():
    MainService.start()
    return MainOutput.create()
