from typing import Literal, cast

ResponseDTOListUserGroupStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LIST_USER_GROUP_STATUS_VALUES: set[ResponseDTOListUserGroupStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_list_user_group_status(value: str) -> ResponseDTOListUserGroupStatus:
    if value in RESPONSE_DTO_LIST_USER_GROUP_STATUS_VALUES:
        return cast(ResponseDTOListUserGroupStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LIST_USER_GROUP_STATUS_VALUES!r}")
