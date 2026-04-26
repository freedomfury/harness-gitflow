from typing import Literal, cast

ResponseDTOEnvironmentResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_ENVIRONMENT_RESPONSE_STATUS_VALUES: set[ResponseDTOEnvironmentResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_environment_response_status(value: str) -> ResponseDTOEnvironmentResponseStatus:
    if value in RESPONSE_DTO_ENVIRONMENT_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOEnvironmentResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_ENVIRONMENT_RESPONSE_STATUS_VALUES!r}")
