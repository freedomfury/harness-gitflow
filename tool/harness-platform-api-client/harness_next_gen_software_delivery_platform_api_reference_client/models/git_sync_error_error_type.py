from typing import Literal, cast

GitSyncErrorErrorType = Literal["CONNECTIVITY_ISSUE", "FULL_SYNC", "GIT_TO_HARNESS"]

GIT_SYNC_ERROR_ERROR_TYPE_VALUES: set[GitSyncErrorErrorType] = {
    "CONNECTIVITY_ISSUE",
    "FULL_SYNC",
    "GIT_TO_HARNESS",
}


def check_git_sync_error_error_type(value: str) -> GitSyncErrorErrorType:
    if value in GIT_SYNC_ERROR_ERROR_TYPE_VALUES:
        return cast(GitSyncErrorErrorType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GIT_SYNC_ERROR_ERROR_TYPE_VALUES!r}")
