from typing import Literal, cast

ServiceFailureResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

SERVICE_FAILURE_RESPONSE_STATUS_VALUES: set[ServiceFailureResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_service_failure_response_status(value: str) -> ServiceFailureResponseStatus:
    if value in SERVICE_FAILURE_RESPONSE_STATUS_VALUES:
        return cast(ServiceFailureResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SERVICE_FAILURE_RESPONSE_STATUS_VALUES!r}")
