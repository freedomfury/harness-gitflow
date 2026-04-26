from typing import Literal, cast

SecretFilterPropertiesSecretTypesItem = Literal["SecretFile", "SecretText", "SSHKey", "WinRmCredentials"]

SECRET_FILTER_PROPERTIES_SECRET_TYPES_ITEM_VALUES: set[SecretFilterPropertiesSecretTypesItem] = {
    "SecretFile",
    "SecretText",
    "SSHKey",
    "WinRmCredentials",
}


def check_secret_filter_properties_secret_types_item(value: str) -> SecretFilterPropertiesSecretTypesItem:
    if value in SECRET_FILTER_PROPERTIES_SECRET_TYPES_ITEM_VALUES:
        return cast(SecretFilterPropertiesSecretTypesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SECRET_FILTER_PROPERTIES_SECRET_TYPES_ITEM_VALUES!r}"
    )
