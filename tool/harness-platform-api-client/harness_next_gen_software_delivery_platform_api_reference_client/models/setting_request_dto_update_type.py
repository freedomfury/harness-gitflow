from typing import Literal, cast

SettingRequestDTOUpdateType = Literal["RESTORE", "UPDATE"]

SETTING_REQUEST_DTO_UPDATE_TYPE_VALUES: set[SettingRequestDTOUpdateType] = {
    "RESTORE",
    "UPDATE",
}


def check_setting_request_dto_update_type(value: str) -> SettingRequestDTOUpdateType:
    if value in SETTING_REQUEST_DTO_UPDATE_TYPE_VALUES:
        return cast(SettingRequestDTOUpdateType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SETTING_REQUEST_DTO_UPDATE_TYPE_VALUES!r}")
