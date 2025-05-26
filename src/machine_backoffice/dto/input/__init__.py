from .create_user_input import CreateUserInput, CreateUserInputSchema
from .security_login_input import SecurityLoginInput, SecurityLoginInputSchema
from .create_role_input import CreateRoleInput, CreateRoleInputSchema
from .create_machine_input import CreateMachineInput, CreateMachineInputSchema
from .create_machine_report_input import CreateMachineReportInput, CreateMachineReportInputSchema
from .create_machine_user_input import CreateMachineUserInput, CreateMachineUserInputSchema
from .update_user_input import UpdateUserInput, UpdateUserInputSchema
from .update_rol_input import UpdateRoleInput, UpdateRoleInputSchema
from .update_machine_input import UpdateMachineInput, UpdateMachineInputSchema
from .update_machine_report_input import UpdateMachineReportInput, UpdateMachineReportInputSchema
from .update_machine_user_input import UpdateMachineUserInput, UpdateMachineUserInputSchema


from .role_schema import RoleSchema, CreateRoleSchemaInput
from .user_schema import UserSchema, CreateUserSchemaInput
from .machine_schema import MachineSchema, CreateMachineSchemaInput
from .machine_user_schema import MachineUserSchema, CreateMachineUserSchemaInput
from .machine_report_schema import MachineReportSchema, CreateMachineReportSchemaInput
from .machine_status_cache_schema import MachineStatusCacheSchema, CreateMachineStatusCacheSchemaInput

inputs = [
    "CreateUserInput",
    "CreateUserInputSchema",
    "SecurityLoginInput",
    "SecurityLoginInputSchema",
    "CreateRoleInput",
    "CreateRoleInputSchema",
    "UpdateUserInput",
    "UpdateUserInputSchema",
    "UpdateRoleInput",
    "UpdateRoleInputSchema",
    "CreateMachineInput",
    "CreateMachineInputSchema",
    "CreateMachineReportInput",
    "CreateMachineReportInputSchema",
    "CreateMachineUserInput",
    "CreateMachineUserInputSchema",
    "UpdateMachineInput",
    "UpdateMachineInputSchema",
    "UpdateMachineReportInput",
    "UpdateMachineReportInputSchema",
    "UpdateMachineUserInput",
    "UpdateMachineUserInputSchema"
]

schemas = [
    "RoleSchema",
    "CreateRoleSchemaInput",
    "UserSchema",
    "CreateUserSchemaInput",
    "MachineSchema",
    "CreateMachineSchemaInput",
    "MachineUserSchema",
    "CreateMachineUserSchemaInput",
    "MachineReportSchema",
    "CreateMachineReportSchemaInput",
    "MachineStatusCacheSchema",
    "CreateMachineStatusCacheSchemaInput"
]


outputs = []


__all__ = [
    *inputs,
    *schemas,
    *outputs
]