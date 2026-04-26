from typing import Literal, cast

GitFullSyncEntityInfoFilterSyncStatus = Literal["FAILED", "OVERRIDDEN", "QUEUED", "SUCCESS"]

GIT_FULL_SYNC_ENTITY_INFO_FILTER_SYNC_STATUS_VALUES: set[GitFullSyncEntityInfoFilterSyncStatus] = {
    "FAILED",
    "OVERRIDDEN",
    "QUEUED",
    "SUCCESS",
}


def check_git_full_sync_entity_info_filter_sync_status(value: str) -> GitFullSyncEntityInfoFilterSyncStatus:
    if value in GIT_FULL_SYNC_ENTITY_INFO_FILTER_SYNC_STATUS_VALUES:
        return cast(GitFullSyncEntityInfoFilterSyncStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GIT_FULL_SYNC_ENTITY_INFO_FILTER_SYNC_STATUS_VALUES!r}"
    )
