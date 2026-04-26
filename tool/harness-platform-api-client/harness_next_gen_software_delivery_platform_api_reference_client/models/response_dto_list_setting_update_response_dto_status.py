from typing import Literal, cast

ResponseDTOListSettingUpdateResponseDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LIST_SETTING_UPDATE_RESPONSE_DTO_STATUS_VALUES: set[ResponseDTOListSettingUpdateResponseDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_list_setting_update_response_dto_status(
    value: str,
) -> ResponseDTOListSettingUpdateResponseDTOStatus:
    if value in RESPONSE_DTO_LIST_SETTING_UPDATE_RESPONSE_DTO_STATUS_VALUES:
        return cast(ResponseDTOListSettingUpdateResponseDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LIST_SETTING_UPDATE_RESPONSE_DTO_STATUS_VALUES!r}"
    )
