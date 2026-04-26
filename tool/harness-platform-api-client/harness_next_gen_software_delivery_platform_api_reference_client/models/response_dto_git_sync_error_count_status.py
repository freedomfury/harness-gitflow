from typing import Literal, cast

ResponseDTOGitSyncErrorCountStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_GIT_SYNC_ERROR_COUNT_STATUS_VALUES: set[ResponseDTOGitSyncErrorCountStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_git_sync_error_count_status(value: str) -> ResponseDTOGitSyncErrorCountStatus:
    if value in RESPONSE_DTO_GIT_SYNC_ERROR_COUNT_STATUS_VALUES:
        return cast(ResponseDTOGitSyncErrorCountStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_GIT_SYNC_ERROR_COUNT_STATUS_VALUES!r}")
