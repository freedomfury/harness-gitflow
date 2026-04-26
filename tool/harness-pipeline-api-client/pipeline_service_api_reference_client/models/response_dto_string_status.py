from typing import Literal, cast

ResponseDTOStringStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_STRING_STATUS_VALUES: set[ResponseDTOStringStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_string_status(value: str) -> ResponseDTOStringStatus:
    if value in RESPONSE_DTO_STRING_STATUS_VALUES:
        return cast(ResponseDTOStringStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_STRING_STATUS_VALUES!r}")
