from typing import Literal, cast

SecretResourceFilterSecretTypesItem = Literal["SecretFile", "SecretText", "SSHKey", "WinRmCredentials"]

SECRET_RESOURCE_FILTER_SECRET_TYPES_ITEM_VALUES: set[SecretResourceFilterSecretTypesItem] = {
    "SecretFile",
    "SecretText",
    "SSHKey",
    "WinRmCredentials",
}


def check_secret_resource_filter_secret_types_item(value: str) -> SecretResourceFilterSecretTypesItem:
    if value in SECRET_RESOURCE_FILTER_SECRET_TYPES_ITEM_VALUES:
        return cast(SecretResourceFilterSecretTypesItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SECRET_RESOURCE_FILTER_SECRET_TYPES_ITEM_VALUES!r}")
