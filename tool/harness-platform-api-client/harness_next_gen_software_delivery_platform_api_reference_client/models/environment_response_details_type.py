from typing import Literal, cast

EnvironmentResponseDetailsType = Literal["PreProduction", "Production"]

ENVIRONMENT_RESPONSE_DETAILS_TYPE_VALUES: set[EnvironmentResponseDetailsType] = {
    "PreProduction",
    "Production",
}


def check_environment_response_details_type(value: str) -> EnvironmentResponseDetailsType:
    if value in ENVIRONMENT_RESPONSE_DETAILS_TYPE_VALUES:
        return cast(EnvironmentResponseDetailsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENVIRONMENT_RESPONSE_DETAILS_TYPE_VALUES!r}")
