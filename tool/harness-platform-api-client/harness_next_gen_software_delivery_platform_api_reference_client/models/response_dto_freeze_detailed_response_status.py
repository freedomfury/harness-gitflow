from typing import Literal, cast

ResponseDTOFreezeDetailedResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_FREEZE_DETAILED_RESPONSE_STATUS_VALUES: set[ResponseDTOFreezeDetailedResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_freeze_detailed_response_status(value: str) -> ResponseDTOFreezeDetailedResponseStatus:
    if value in RESPONSE_DTO_FREEZE_DETAILED_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOFreezeDetailedResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_FREEZE_DETAILED_RESPONSE_STATUS_VALUES!r}"
    )
