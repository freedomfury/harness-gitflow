from typing import Literal, cast

GitSyncErrorStatus = Literal["ACTIVE", "DISCARDED", "EXPIRED", "OVERRIDDEN", "RESOLVED"]

GIT_SYNC_ERROR_STATUS_VALUES: set[GitSyncErrorStatus] = {
    "ACTIVE",
    "DISCARDED",
    "EXPIRED",
    "OVERRIDDEN",
    "RESOLVED",
}


def check_git_sync_error_status(value: str) -> GitSyncErrorStatus:
    if value in GIT_SYNC_ERROR_STATUS_VALUES:
        return cast(GitSyncErrorStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GIT_SYNC_ERROR_STATUS_VALUES!r}")
