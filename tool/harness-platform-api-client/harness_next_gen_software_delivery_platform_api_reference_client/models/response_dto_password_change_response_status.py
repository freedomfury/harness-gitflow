from typing import Literal, cast

ResponseDTOPasswordChangeResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PASSWORD_CHANGE_RESPONSE_STATUS_VALUES: set[ResponseDTOPasswordChangeResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_password_change_response_status(value: str) -> ResponseDTOPasswordChangeResponseStatus:
    if value in RESPONSE_DTO_PASSWORD_CHANGE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPasswordChangeResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PASSWORD_CHANGE_RESPONSE_STATUS_VALUES!r}"
    )
