from typing import Literal, cast

ResponseDTOInputSetResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_INPUT_SET_RESPONSE_STATUS_VALUES: set[ResponseDTOInputSetResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_input_set_response_status(value: str) -> ResponseDTOInputSetResponseStatus:
    if value in RESPONSE_DTO_INPUT_SET_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOInputSetResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_INPUT_SET_RESPONSE_STATUS_VALUES!r}")
