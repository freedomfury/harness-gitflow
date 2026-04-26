from typing import Literal, cast

ResponseDTOTwoFactorAuthSettingsInfoStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_TWO_FACTOR_AUTH_SETTINGS_INFO_STATUS_VALUES: set[ResponseDTOTwoFactorAuthSettingsInfoStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_two_factor_auth_settings_info_status(value: str) -> ResponseDTOTwoFactorAuthSettingsInfoStatus:
    if value in RESPONSE_DTO_TWO_FACTOR_AUTH_SETTINGS_INFO_STATUS_VALUES:
        return cast(ResponseDTOTwoFactorAuthSettingsInfoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_TWO_FACTOR_AUTH_SETTINGS_INFO_STATUS_VALUES!r}"
    )
