from typing import Literal, cast

PrincipalType = Literal["API_KEY", "SERVICE", "SERVICE_ACCOUNT", "USER"]

PRINCIPAL_TYPE_VALUES: set[PrincipalType] = {
    "API_KEY",
    "SERVICE",
    "SERVICE_ACCOUNT",
    "USER",
}


def check_principal_type(value: str) -> PrincipalType:
    if value in PRINCIPAL_TYPE_VALUES:
        return cast(PrincipalType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PRINCIPAL_TYPE_VALUES!r}")
