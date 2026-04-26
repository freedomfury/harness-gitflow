from typing import Literal, cast

ResponseDTOUserGroupResponseV2Status = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_USER_GROUP_RESPONSE_V2_STATUS_VALUES: set[ResponseDTOUserGroupResponseV2Status] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_user_group_response_v2_status(value: str) -> ResponseDTOUserGroupResponseV2Status:
    if value in RESPONSE_DTO_USER_GROUP_RESPONSE_V2_STATUS_VALUES:
        return cast(ResponseDTOUserGroupResponseV2Status, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_USER_GROUP_RESPONSE_V2_STATUS_VALUES!r}"
    )
