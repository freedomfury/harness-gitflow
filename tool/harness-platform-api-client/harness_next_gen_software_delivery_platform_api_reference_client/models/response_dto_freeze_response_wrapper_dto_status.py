from typing import Literal, cast

ResponseDTOFreezeResponseWrapperDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_FREEZE_RESPONSE_WRAPPER_DTO_STATUS_VALUES: set[ResponseDTOFreezeResponseWrapperDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_freeze_response_wrapper_dto_status(value: str) -> ResponseDTOFreezeResponseWrapperDTOStatus:
    if value in RESPONSE_DTO_FREEZE_RESPONSE_WRAPPER_DTO_STATUS_VALUES:
        return cast(ResponseDTOFreezeResponseWrapperDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_FREEZE_RESPONSE_WRAPPER_DTO_STATUS_VALUES!r}"
    )
