from typing import Literal, cast

SpotCredentialType = Literal["PermanentTokenConfig"]

SPOT_CREDENTIAL_TYPE_VALUES: set[SpotCredentialType] = {
    "PermanentTokenConfig",
}


def check_spot_credential_type(value: str) -> SpotCredentialType:
    if value in SPOT_CREDENTIAL_TYPE_VALUES:
        return cast(SpotCredentialType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SPOT_CREDENTIAL_TYPE_VALUES!r}")
