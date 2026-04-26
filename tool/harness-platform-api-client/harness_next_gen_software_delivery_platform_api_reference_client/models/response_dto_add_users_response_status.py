from typing import Literal, cast

ResponseDTOAddUsersResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_ADD_USERS_RESPONSE_STATUS_VALUES: set[ResponseDTOAddUsersResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_add_users_response_status(value: str) -> ResponseDTOAddUsersResponseStatus:
    if value in RESPONSE_DTO_ADD_USERS_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOAddUsersResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_ADD_USERS_RESPONSE_STATUS_VALUES!r}")
