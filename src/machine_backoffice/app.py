import importlib
import logging
from os import getenv
from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from .controller import __all__ as controllers
from .conection import database
from .dto import ConnectionByIdentifierEnum
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from .cron.cron import Cron

load_dotenv()

scheduler = BackgroundScheduler()

def app() -> FastAPI:
    if not database().ping(ConnectionByIdentifierEnum.MACHINE_BACKOFFICE):
        logging.critical(
            "❌  Ups, hubo un error al conectar con la base de datos de machine backoffice, revisa tus variables de entorno"
        )

    app = FastAPI(
        redoc_url=None,
        title="Microservice machine backoffice",
        description="The documentation is from machine backoffice. ",
        version=getenv("VERSION"),
        openapi_url="/openapi.json",
        docs_url="/",
        root_path="/",
    )

    # Middlewares
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(GZipMiddleware, minimum_size=500)

    for controller_name in controllers:
        try:
            module = importlib.import_module("src.machine_backoffice.controller")
            router = getattr(module, controller_name)
            app.include_router(router)
            logging.info(f"✅ Importado y registrado router: {controller_name}")
        except Exception as e:
            logging.critical(f"❌ Error importando {controller_name}: {str(e)}")

    @app.on_event("startup")
    def start_scheduler():
        scheduler.add_job(Cron().review_status_machine, CronTrigger(second="*/1"))
        scheduler.start()
        logging.info("🕒 Scheduler iniciado")

    @app.on_event("shutdown")
    def shutdown_scheduler():
        scheduler.shutdown()
        logging.info("🛑 Scheduler detenido")

    return app


def create_app() -> FastAPI:
    return app()


app_instance = create_app() if __name__ == "__main__" else None

__all__ = ["app_instance"]
