from typing import Literal, cast

ResponseDTOServiceResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SERVICE_RESPONSE_STATUS_VALUES: set[ResponseDTOServiceResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_service_response_status(value: str) -> ResponseDTOServiceResponseStatus:
    if value in RESPONSE_DTO_SERVICE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOServiceResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SERVICE_RESPONSE_STATUS_VALUES!r}")
