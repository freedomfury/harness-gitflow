from typing import Literal, cast

ResponseDTOListStringStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LIST_STRING_STATUS_VALUES: set[ResponseDTOListStringStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_list_string_status(value: str) -> ResponseDTOListStringStatus:
    if value in RESPONSE_DTO_LIST_STRING_STATUS_VALUES:
        return cast(ResponseDTOListStringStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LIST_STRING_STATUS_VALUES!r}")
