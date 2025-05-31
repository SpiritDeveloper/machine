from ..models.machine_model import MachineModel
from ..models.machine_report_model import MachineReportModel
from ..models.machine_state_cache import MachineStateCacheModel
from ..dto import MachineSchema, MachineStatusCacheSchema
from pylogix import PLC
import logging
from datetime import datetime
from typing import Optional


class Cron:
    def __init__(self):
        self.machine_model = MachineModel()
        self.machine_report_model = MachineReportModel()
        self.machine_state_cache_model = MachineStateCacheModel()

    def get_status_machine_by_hash(self, machine: MachineSchema) -> Optional[int]:
        ip = machine.get('ip')
        tag = machine.get('hash')

        if not ip or not tag:
            logging.error("⚠️  IP o hash no definidos")
            return None
        print(ip)
        try:
            with PLC() as plc:
                plc.IPAddress = ip
                response = plc.Read(tag)
                return int(response.Value)
        except Exception as e:
            logging.info(f"🔥 Excepción con PLC en {ip}: {e}")
            return 0

    def review_status_machine(self):
        machines: list[MachineSchema] = self.machine_model.get_all()
        now = datetime.now()

        for machine in machines:
            machine_id = str(machine["_id"])
            status = self.get_status_machine_by_hash(machine)

            prev_state = self.machine_state_cache_model.find_one(machine_id=machine_id)

            print(f"prev_state: {prev_state}")

            if prev_state is None and status == 1:
                machine_state_cache_model: MachineStatusCacheSchema = {
                    "machine_id": machine_id,
                    "status": status,
                    "start_time": now if status == 1 else None,
                    "date_failure": now if status == 0 else None
                }
                self.machine_state_cache_model.save(**machine_state_cache_model)

                update_machine: MachineSchema = {
                    "status": 'ENABLED',
                    "last_status_change": now
                }

                self.machine_model.update(machine_id, **update_machine)
                continue

            logging.info(f"prev_state: {prev_state}")
            logging.info(f"status: {status}")

            prev_status = prev_state and prev_state['status'] or 0

            if prev_status == 1 and status == 0:
                start_time = prev_state["start_time"]
                time_active = (now - start_time).total_seconds() if start_time else 0

                self.machine_report_model.save(**{
                    "machine_id": machine_id,
                    "user_report_id": machine["hash"],
                    "date_start": start_time,
                    "date_end": now,
                    "time_failure": 0,
                    "time_start": start_time,
                    "time_end": now,
                    "description": f"🔴 Máquina '{machine['name']}' operó {time_active:.2f} segundos antes de apagarse.",
                    "date_failure": now,
                    "status": "ENABLED",
                    "enable": True,
                    "created_at": now,
                    "updated_at": now,
                    "deleted_at": None,
                })

                machine_state_cache_model: MachineStatusCacheSchema = {
                    "machine_id": machine_id,
                    "status": 0,
                    "start_time": None,
                    "date_failure": now
                }

                self.machine_state_cache_model.update(str(prev_state["_id"]), **machine_state_cache_model)

                update_machine: MachineSchema = {
                    "status": 'ENABLED',
                    "last_status_change": now
                }

                self.machine_model.update(machine_id, **update_machine)


            elif prev_status == 0 and status == 1:
                date_failure = prev_state["date_failure"]
                time_down = (now - date_failure).total_seconds() if date_failure else 0

                self.machine_report_model.save(**{
                    "machine_id": machine_id,
                    "user_report_id": machine["hash"],
                    "date_failure": date_failure,
                    "date_start": date_failure,
                    "date_end": now,
                    "time_failure": time_down,
                    "status": "DISABLED",
                    "time_start": date_failure,
                    "time_end": now,
                    "description": f"🟢 Máquina '{machine['name']}' estuvo apagada {time_down:.2f} segundos y volvió a operar.",
                    "enable": True,
                    "created_at": now,
                    "updated_at": now,
                    "deleted_at": None,
                })

                machine_state_cache_model: MachineStatusCacheSchema = {
                    "machine_id": machine_id,
                    "status": 1,
                    "start_time": now,
                    "date_failure": None
                }

                self.machine_state_cache_model.update(str(prev_state["_id"]), **machine_state_cache_model)

                update_machine: MachineSchema = {
                    "status": 'DISABLED',
                    "last_status_change": now
                }

                self.machine_model.update(machine_id, **update_machine)


            else:
                continue
