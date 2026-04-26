from typing import Literal, cast

ResponseDTOSettingValueResponseDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SETTING_VALUE_RESPONSE_DTO_STATUS_VALUES: set[ResponseDTOSettingValueResponseDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_setting_value_response_dto_status(value: str) -> ResponseDTOSettingValueResponseDTOStatus:
    if value in RESPONSE_DTO_SETTING_VALUE_RESPONSE_DTO_STATUS_VALUES:
        return cast(ResponseDTOSettingValueResponseDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SETTING_VALUE_RESPONSE_DTO_STATUS_VALUES!r}"
    )
