from typing import Literal, cast

ResponseDTOListUserSettingUpdateResponseDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LIST_USER_SETTING_UPDATE_RESPONSE_DTO_STATUS_VALUES: set[
    ResponseDTOListUserSettingUpdateResponseDTOStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_list_user_setting_update_response_dto_status(
    value: str,
) -> ResponseDTOListUserSettingUpdateResponseDTOStatus:
    if value in RESPONSE_DTO_LIST_USER_SETTING_UPDATE_RESPONSE_DTO_STATUS_VALUES:
        return cast(ResponseDTOListUserSettingUpdateResponseDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LIST_USER_SETTING_UPDATE_RESPONSE_DTO_STATUS_VALUES!r}"
    )
