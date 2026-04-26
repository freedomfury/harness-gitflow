from typing import Literal, cast

ExecutionPrincipalInfoPrincipalType = Literal[
    "API_KEY", "SERVICE", "SERVICE_ACCOUNT", "UNKNOWN", "UNRECOGNIZED", "USER", "USER_GROUP"
]

EXECUTION_PRINCIPAL_INFO_PRINCIPAL_TYPE_VALUES: set[ExecutionPrincipalInfoPrincipalType] = {
    "API_KEY",
    "SERVICE",
    "SERVICE_ACCOUNT",
    "UNKNOWN",
    "UNRECOGNIZED",
    "USER",
    "USER_GROUP",
}


def check_execution_principal_info_principal_type(value: str) -> ExecutionPrincipalInfoPrincipalType:
    if value in EXECUTION_PRINCIPAL_INFO_PRINCIPAL_TYPE_VALUES:
        return cast(ExecutionPrincipalInfoPrincipalType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EXECUTION_PRINCIPAL_INFO_PRINCIPAL_TYPE_VALUES!r}")
