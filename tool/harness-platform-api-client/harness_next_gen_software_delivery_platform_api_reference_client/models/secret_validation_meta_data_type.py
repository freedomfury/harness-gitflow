from typing import Literal, cast

SecretValidationMetaDataType = Literal["SecretFile", "SecretText", "SSHKey", "WinRmCredentials"]

SECRET_VALIDATION_META_DATA_TYPE_VALUES: set[SecretValidationMetaDataType] = {
    "SecretFile",
    "SecretText",
    "SSHKey",
    "WinRmCredentials",
}


def check_secret_validation_meta_data_type(value: str) -> SecretValidationMetaDataType:
    if value in SECRET_VALIDATION_META_DATA_TYPE_VALUES:
        return cast(SecretValidationMetaDataType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SECRET_VALIDATION_META_DATA_TYPE_VALUES!r}")
