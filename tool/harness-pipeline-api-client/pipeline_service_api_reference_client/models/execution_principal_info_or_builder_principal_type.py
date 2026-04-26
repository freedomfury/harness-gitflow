from typing import Literal, cast

ExecutionPrincipalInfoOrBuilderPrincipalType = Literal[
    "API_KEY", "SERVICE", "SERVICE_ACCOUNT", "UNKNOWN", "UNRECOGNIZED", "USER", "USER_GROUP"
]

EXECUTION_PRINCIPAL_INFO_OR_BUILDER_PRINCIPAL_TYPE_VALUES: set[ExecutionPrincipalInfoOrBuilderPrincipalType] = {
    "API_KEY",
    "SERVICE",
    "SERVICE_ACCOUNT",
    "UNKNOWN",
    "UNRECOGNIZED",
    "USER",
    "USER_GROUP",
}


def check_execution_principal_info_or_builder_principal_type(
    value: str,
) -> ExecutionPrincipalInfoOrBuilderPrincipalType:
    if value in EXECUTION_PRINCIPAL_INFO_OR_BUILDER_PRINCIPAL_TYPE_VALUES:
        return cast(ExecutionPrincipalInfoOrBuilderPrincipalType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXECUTION_PRINCIPAL_INFO_OR_BUILDER_PRINCIPAL_TYPE_VALUES!r}"
    )
