from typing import Literal, cast

ResponseDTOPageResponseGitSyncErrorStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_GIT_SYNC_ERROR_STATUS_VALUES: set[ResponseDTOPageResponseGitSyncErrorStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_git_sync_error_status(value: str) -> ResponseDTOPageResponseGitSyncErrorStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_GIT_SYNC_ERROR_STATUS_VALUES:
        return cast(ResponseDTOPageResponseGitSyncErrorStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_GIT_SYNC_ERROR_STATUS_VALUES!r}"
    )
