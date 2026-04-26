from typing import Literal, cast

ResponseDTOGitSyncSettingsStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_GIT_SYNC_SETTINGS_STATUS_VALUES: set[ResponseDTOGitSyncSettingsStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_git_sync_settings_status(value: str) -> ResponseDTOGitSyncSettingsStatus:
    if value in RESPONSE_DTO_GIT_SYNC_SETTINGS_STATUS_VALUES:
        return cast(ResponseDTOGitSyncSettingsStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_GIT_SYNC_SETTINGS_STATUS_VALUES!r}")
