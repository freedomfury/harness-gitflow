from typing import Literal, cast

ResponseDTOOverrideResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_OVERRIDE_RESPONSE_STATUS_VALUES: set[ResponseDTOOverrideResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_override_response_status(value: str) -> ResponseDTOOverrideResponseStatus:
    if value in RESPONSE_DTO_OVERRIDE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOOverrideResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_OVERRIDE_RESPONSE_STATUS_VALUES!r}")
