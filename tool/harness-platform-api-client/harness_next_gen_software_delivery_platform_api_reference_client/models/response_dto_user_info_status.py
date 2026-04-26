from typing import Literal, cast

ResponseDTOUserInfoStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_USER_INFO_STATUS_VALUES: set[ResponseDTOUserInfoStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_user_info_status(value: str) -> ResponseDTOUserInfoStatus:
    if value in RESPONSE_DTO_USER_INFO_STATUS_VALUES:
        return cast(ResponseDTOUserInfoStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_USER_INFO_STATUS_VALUES!r}")
