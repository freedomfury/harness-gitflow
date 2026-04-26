from typing import Literal, cast

ResponseDTOTokenStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_TOKEN_STATUS_VALUES: set[ResponseDTOTokenStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_token_status(value: str) -> ResponseDTOTokenStatus:
    if value in RESPONSE_DTO_TOKEN_STATUS_VALUES:
        return cast(ResponseDTOTokenStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_TOKEN_STATUS_VALUES!r}")
