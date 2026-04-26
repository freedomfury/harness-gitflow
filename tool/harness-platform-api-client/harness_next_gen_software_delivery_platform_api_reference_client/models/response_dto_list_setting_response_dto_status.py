from typing import Literal, cast

ResponseDTOListSettingResponseDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LIST_SETTING_RESPONSE_DTO_STATUS_VALUES: set[ResponseDTOListSettingResponseDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_list_setting_response_dto_status(value: str) -> ResponseDTOListSettingResponseDTOStatus:
    if value in RESPONSE_DTO_LIST_SETTING_RESPONSE_DTO_STATUS_VALUES:
        return cast(ResponseDTOListSettingResponseDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LIST_SETTING_RESPONSE_DTO_STATUS_VALUES!r}"
    )
