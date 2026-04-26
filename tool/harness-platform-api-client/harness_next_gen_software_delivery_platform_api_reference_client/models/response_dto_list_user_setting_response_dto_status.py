from typing import Literal, cast

ResponseDTOListUserSettingResponseDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LIST_USER_SETTING_RESPONSE_DTO_STATUS_VALUES: set[ResponseDTOListUserSettingResponseDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_list_user_setting_response_dto_status(value: str) -> ResponseDTOListUserSettingResponseDTOStatus:
    if value in RESPONSE_DTO_LIST_USER_SETTING_RESPONSE_DTO_STATUS_VALUES:
        return cast(ResponseDTOListUserSettingResponseDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LIST_USER_SETTING_RESPONSE_DTO_STATUS_VALUES!r}"
    )
