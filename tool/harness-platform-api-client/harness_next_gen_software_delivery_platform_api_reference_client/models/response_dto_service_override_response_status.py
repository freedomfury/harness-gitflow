from typing import Literal, cast

ResponseDTOServiceOverrideResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SERVICE_OVERRIDE_RESPONSE_STATUS_VALUES: set[ResponseDTOServiceOverrideResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_service_override_response_status(value: str) -> ResponseDTOServiceOverrideResponseStatus:
    if value in RESPONSE_DTO_SERVICE_OVERRIDE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOServiceOverrideResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SERVICE_OVERRIDE_RESPONSE_STATUS_VALUES!r}"
    )
