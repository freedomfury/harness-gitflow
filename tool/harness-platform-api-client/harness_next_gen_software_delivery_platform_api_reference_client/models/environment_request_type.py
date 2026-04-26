from typing import Literal, cast

EnvironmentRequestType = Literal["PreProduction", "Production"]

ENVIRONMENT_REQUEST_TYPE_VALUES: set[EnvironmentRequestType] = {
    "PreProduction",
    "Production",
}


def check_environment_request_type(value: str) -> EnvironmentRequestType:
    if value in ENVIRONMENT_REQUEST_TYPE_VALUES:
        return cast(EnvironmentRequestType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENVIRONMENT_REQUEST_TYPE_VALUES!r}")
