from typing import Literal, cast

EnvironmentFailureResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

ENVIRONMENT_FAILURE_RESPONSE_STATUS_VALUES: set[EnvironmentFailureResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_environment_failure_response_status(value: str) -> EnvironmentFailureResponseStatus:
    if value in ENVIRONMENT_FAILURE_RESPONSE_STATUS_VALUES:
        return cast(EnvironmentFailureResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENVIRONMENT_FAILURE_RESPONSE_STATUS_VALUES!r}")
