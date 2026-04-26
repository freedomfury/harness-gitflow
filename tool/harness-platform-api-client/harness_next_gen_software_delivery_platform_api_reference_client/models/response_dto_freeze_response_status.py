from typing import Literal, cast

ResponseDTOFreezeResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_FREEZE_RESPONSE_STATUS_VALUES: set[ResponseDTOFreezeResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_freeze_response_status(value: str) -> ResponseDTOFreezeResponseStatus:
    if value in RESPONSE_DTO_FREEZE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOFreezeResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_FREEZE_RESPONSE_STATUS_VALUES!r}")
