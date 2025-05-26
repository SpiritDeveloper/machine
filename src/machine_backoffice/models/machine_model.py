from bson.objectid import ObjectId
from ..conection import database
from ..dto import ConnectionByIdentifierEnum
import logging


class MachineModel:
    def __init__(self):
        self.client = database().get_conexion_by_identifier(
            ConnectionByIdentifierEnum.MACHINE_BACKOFFICE
        )
        self.collection = self.client["machine"]

    def save(self, **request):
        logging.info(f"🔍 Saving machine with data: {request}")
        try:
            request["enable"] = True
            result = self.collection.insert_one(request)
            return self.get_by_id(str(result.inserted_id))
        except Exception as err:
            logging.error(f"❌ Error saving machine: {err}")
            return None

    def get_all(self):
        logging.info(f"🔍 Getting all machines")
        try:
            return list(self.collection.find({"enable": True}))
        except Exception as err:
            print(str(err))
            return None

    def get_by_id(self, id: str):
        logging.info(f"🔍 Getting machine by id: {id}")
        try:
            id = ObjectId(id)
            return self.collection.find_one({"_id": id})
        except Exception:
            logging.error(f"❌ Error getting machine by id: {id}")
            return None

    def find_one(self, **request):
        logging.info(f"🔍 Getting machine by request: {request}")
        try:
            if request.get('id'):
                request['_id'] = ObjectId(request['id'])
                del request['id']

            return self.collection.find_one(request)
        except Exception:
            logging.error(f"❌ Error getting machine by request: {request}")
            return None

    def update(self, id: str, **request):
        logging.info(f"🔍 Updating machine with data: {request}")
        try:
            id = ObjectId(id) if id else None

            self.collection.update_one(
                {"_id": id},
                {"$set": request},
                upsert=True,
            )

            return self.get_by_id(id)
        except Exception:
            return None

    def delete(self, id: str):
        logging.info(f"🔍 Deleting machine with id: {id}")
        try:
            id = ObjectId(id)
            return self.collection.update_one(
                {"_id": id},
                {"$set": {"enable": False}},
                upsert=True,
            )
        except Exception:
            return None