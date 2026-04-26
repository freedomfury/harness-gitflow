from typing import Literal, cast

ResponseDTOUserGroupStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_USER_GROUP_STATUS_VALUES: set[ResponseDTOUserGroupStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_user_group_status(value: str) -> ResponseDTOUserGroupStatus:
    if value in RESPONSE_DTO_USER_GROUP_STATUS_VALUES:
        return cast(ResponseDTOUserGroupStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_USER_GROUP_STATUS_VALUES!r}")
