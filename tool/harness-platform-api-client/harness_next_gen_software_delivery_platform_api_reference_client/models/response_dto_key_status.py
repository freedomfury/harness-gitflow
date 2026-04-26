from typing import Literal, cast

ResponseDTOKeyStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_KEY_STATUS_VALUES: set[ResponseDTOKeyStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_key_status(value: str) -> ResponseDTOKeyStatus:
    if value in RESPONSE_DTO_KEY_STATUS_VALUES:
        return cast(ResponseDTOKeyStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_KEY_STATUS_VALUES!r}")
