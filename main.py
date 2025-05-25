import os
import logging
import uvicorn
from dotenv import load_dotenv
from src.machine_backoffice.utils.logging_configuration import setup_logging

setup_logging()
load_dotenv()

if __name__ == "__main__":
    logging.info("🚀 Iniciando aplicación machine backoffice 🚀")
    logging.info(f"🍻 Se ejecutara el modulo: {str(os.getenv('APP_MODULE'))}")
    try:
        uvicorn.run(
            str(os.getenv("APP_MODULE")) + ":create_app",
            host=str(os.getenv("HOST", "0.0.0.0")),
            port=int(os.getenv("PORT", "4000")),
            reload=bool(os.getenv("RELOAD", False)),
            workers=int(os.getenv("WORKERS", 3)),
            factory=True,
            log_config=None,
        )
    except Exception as e:
        logging.critical(f"Ups, hubo un error al iniciar la aplicación: {e}")
        raise e
