from typing import Literal, cast

ResponseDTOLongStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LONG_STATUS_VALUES: set[ResponseDTOLongStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_long_status(value: str) -> ResponseDTOLongStatus:
    if value in RESPONSE_DTO_LONG_STATUS_VALUES:
        return cast(ResponseDTOLongStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LONG_STATUS_VALUES!r}")
