from typing import Literal, cast

ResponseDTOTriggerGitFullSyncResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_TRIGGER_GIT_FULL_SYNC_RESPONSE_STATUS_VALUES: set[ResponseDTOTriggerGitFullSyncResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_trigger_git_full_sync_response_status(value: str) -> ResponseDTOTriggerGitFullSyncResponseStatus:
    if value in RESPONSE_DTO_TRIGGER_GIT_FULL_SYNC_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOTriggerGitFullSyncResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_TRIGGER_GIT_FULL_SYNC_RESPONSE_STATUS_VALUES!r}"
    )
