from typing import Literal, cast

ResponseDTONGTriggerResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTONG_TRIGGER_RESPONSE_STATUS_VALUES: set[ResponseDTONGTriggerResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dtong_trigger_response_status(value: str) -> ResponseDTONGTriggerResponseStatus:
    if value in RESPONSE_DTONG_TRIGGER_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTONGTriggerResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTONG_TRIGGER_RESPONSE_STATUS_VALUES!r}")
