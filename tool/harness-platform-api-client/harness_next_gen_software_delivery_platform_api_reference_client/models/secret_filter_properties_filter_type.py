from typing import Literal, cast

SecretFilterPropertiesFilterType = Literal["Secret"]

SECRET_FILTER_PROPERTIES_FILTER_TYPE_VALUES: set[SecretFilterPropertiesFilterType] = {
    "Secret",
}


def check_secret_filter_properties_filter_type(value: str) -> SecretFilterPropertiesFilterType:
    if value in SECRET_FILTER_PROPERTIES_FILTER_TYPE_VALUES:
        return cast(SecretFilterPropertiesFilterType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SECRET_FILTER_PROPERTIES_FILTER_TYPE_VALUES!r}")
