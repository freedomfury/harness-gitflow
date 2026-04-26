from typing import Literal, cast

ResponseDTOAccountSettingResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_ACCOUNT_SETTING_RESPONSE_STATUS_VALUES: set[ResponseDTOAccountSettingResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_account_setting_response_status(value: str) -> ResponseDTOAccountSettingResponseStatus:
    if value in RESPONSE_DTO_ACCOUNT_SETTING_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOAccountSettingResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_ACCOUNT_SETTING_RESPONSE_STATUS_VALUES!r}"
    )
