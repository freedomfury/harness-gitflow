from typing import Literal, cast

ResponseDTOPageResponseUserGroupStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_USER_GROUP_STATUS_VALUES: set[ResponseDTOPageResponseUserGroupStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_user_group_status(value: str) -> ResponseDTOPageResponseUserGroupStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_USER_GROUP_STATUS_VALUES:
        return cast(ResponseDTOPageResponseUserGroupStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_USER_GROUP_STATUS_VALUES!r}"
    )
