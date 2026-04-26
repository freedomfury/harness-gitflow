from typing import Literal, cast

GitFullSyncEntityInfoSyncStatus = Literal["FAILED", "OVERRIDDEN", "QUEUED", "SUCCESS"]

GIT_FULL_SYNC_ENTITY_INFO_SYNC_STATUS_VALUES: set[GitFullSyncEntityInfoSyncStatus] = {
    "FAILED",
    "OVERRIDDEN",
    "QUEUED",
    "SUCCESS",
}


def check_git_full_sync_entity_info_sync_status(value: str) -> GitFullSyncEntityInfoSyncStatus:
    if value in GIT_FULL_SYNC_ENTITY_INFO_SYNC_STATUS_VALUES:
        return cast(GitFullSyncEntityInfoSyncStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GIT_FULL_SYNC_ENTITY_INFO_SYNC_STATUS_VALUES!r}")
