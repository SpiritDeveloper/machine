from .create_user_input import CreateUserInput, CreateUserInputSchema
from .security_login_input import SecurityLoginInput, SecurityLoginInputSchema
from .create_role_input import CreateRoleInput, CreateRoleInputSchema
from .update_user_input import UpdateUserInput, UpdateUserInputSchema
from .update_rol_input import UpdateRoleInput, UpdateRoleInputSchema


from .role_schema import RoleSchema, CreateRoleSchemaInput
from .user_schema import UserSchema, CreateUserSchemaInput
from .machine_schema import MachineSchema, CreateMachineSchemaInput
from .machine_user_schema import MachineUserSchema, CreateMachineUserSchemaInput
from .machine_report_schema import MachineReportSchema, CreateMachineReportSchemaInput


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
    "UpdateRoleInputSchema"
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
    "CreateMachineReportSchemaInput"
]


outputs = []


__all__ = [
    *inputs,
    *schemas,
    *outputs
]