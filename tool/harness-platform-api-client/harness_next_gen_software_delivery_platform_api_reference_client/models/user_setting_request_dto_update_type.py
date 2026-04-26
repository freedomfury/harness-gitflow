from typing import Literal, cast

UserSettingRequestDTOUpdateType = Literal["RESTORE", "UPDATE"]

USER_SETTING_REQUEST_DTO_UPDATE_TYPE_VALUES: set[UserSettingRequestDTOUpdateType] = {
    "RESTORE",
    "UPDATE",
}


def check_user_setting_request_dto_update_type(value: str) -> UserSettingRequestDTOUpdateType:
    if value in USER_SETTING_REQUEST_DTO_UPDATE_TYPE_VALUES:
        return cast(UserSettingRequestDTOUpdateType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {USER_SETTING_REQUEST_DTO_UPDATE_TYPE_VALUES!r}")
