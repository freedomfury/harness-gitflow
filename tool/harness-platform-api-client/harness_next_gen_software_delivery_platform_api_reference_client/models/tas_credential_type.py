from typing import Literal, cast

TasCredentialType = Literal["ManualConfig"]

TAS_CREDENTIAL_TYPE_VALUES: set[TasCredentialType] = {
    "ManualConfig",
}


def check_tas_credential_type(value: str) -> TasCredentialType:
    if value in TAS_CREDENTIAL_TYPE_VALUES:
        return cast(TasCredentialType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TAS_CREDENTIAL_TYPE_VALUES!r}")
