from typing import Literal, cast

ResponseDTOGitFullSyncConfigStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_GIT_FULL_SYNC_CONFIG_STATUS_VALUES: set[ResponseDTOGitFullSyncConfigStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_git_full_sync_config_status(value: str) -> ResponseDTOGitFullSyncConfigStatus:
    if value in RESPONSE_DTO_GIT_FULL_SYNC_CONFIG_STATUS_VALUES:
        return cast(ResponseDTOGitFullSyncConfigStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_GIT_FULL_SYNC_CONFIG_STATUS_VALUES!r}")
