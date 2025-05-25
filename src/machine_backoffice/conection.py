import os
import logging
from dotenv import load_dotenv
from pymongo import MongoClient
from .dto import ConnectionByIdentifierEnum
from .exceptions.conection_database_exceptions import ConectionDatabaseErrors

load_dotenv()


class database:
    def __init__(self):
        self.db = "mongodb://{}:{}@{}:{}/{}".format(
            os.getenv("DB_USER"),
            os.getenv("DB_PASSWORD"),
            os.getenv("DB_HOST"),
            os.getenv("DB_PORT"),
            os.getenv("DB_SCHEMA"),
        )

    def ping(self, identifier: ConnectionByIdentifierEnum) -> bool | None:
        client = None
        try:
            client = MongoClient(self.db)
            client.admin.command("ping")
            logging.info(f"✅ MongoDB connection successful for {identifier}")
            return True
        except Exception as e:
            logging.error(f"❌ MongoDB connection failed for {identifier}: {str(e)}")
        finally:
            if client:
                client.close()
            return client

    def get_conexion_by_identifier(
        self, identifier: ConnectionByIdentifierEnum
    ) -> MongoClient | None:
        logging.info(f"🔍 Getting connection for {identifier} database")
        client: MongoClient | None = None
        ping = self.ping(identifier)
        if not ping:
            logging.critical("❌ MongoDB connection failed for machine backoffice")
            ConectionDatabaseErrors.not_connection_database_by_identifier(
               "ups, hubo un error al conectar con la base de datos de machine backoffice, revisa tus variables de entorno"
            )

        client = MongoClient(self.db)
        client = client[os.getenv("DB_SCHEMA")]

        return client