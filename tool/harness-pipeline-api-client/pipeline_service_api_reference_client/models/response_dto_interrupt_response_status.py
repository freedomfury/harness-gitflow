from typing import Literal, cast

ResponseDTOInterruptResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_INTERRUPT_RESPONSE_STATUS_VALUES: set[ResponseDTOInterruptResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_interrupt_response_status(value: str) -> ResponseDTOInterruptResponseStatus:
    if value in RESPONSE_DTO_INTERRUPT_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOInterruptResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_INTERRUPT_RESPONSE_STATUS_VALUES!r}")
