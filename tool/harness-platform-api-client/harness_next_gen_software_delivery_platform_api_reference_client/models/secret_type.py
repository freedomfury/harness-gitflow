from typing import Literal, cast

SecretType = Literal["SecretFile", "SecretText", "SSHKey", "WinRmCredentials"]

SECRET_TYPE_VALUES: set[SecretType] = {
    "SecretFile",
    "SecretText",
    "SSHKey",
    "WinRmCredentials",
}


def check_secret_type(value: str) -> SecretType:
    if value in SECRET_TYPE_VALUES:
        return cast(SecretType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SECRET_TYPE_VALUES!r}")
