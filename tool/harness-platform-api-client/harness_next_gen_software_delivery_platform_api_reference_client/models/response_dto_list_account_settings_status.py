from typing import Literal, cast

ResponseDTOListAccountSettingsStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LIST_ACCOUNT_SETTINGS_STATUS_VALUES: set[ResponseDTOListAccountSettingsStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_list_account_settings_status(value: str) -> ResponseDTOListAccountSettingsStatus:
    if value in RESPONSE_DTO_LIST_ACCOUNT_SETTINGS_STATUS_VALUES:
        return cast(ResponseDTOListAccountSettingsStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LIST_ACCOUNT_SETTINGS_STATUS_VALUES!r}")
