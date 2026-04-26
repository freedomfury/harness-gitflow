from typing import Literal, cast

GitBranchBranchSyncStatus = Literal["SYNCED", "SYNCING", "UNSYNCED"]

GIT_BRANCH_BRANCH_SYNC_STATUS_VALUES: set[GitBranchBranchSyncStatus] = {
    "SYNCED",
    "SYNCING",
    "UNSYNCED",
}


def check_git_branch_branch_sync_status(value: str) -> GitBranchBranchSyncStatus:
    if value in GIT_BRANCH_BRANCH_SYNC_STATUS_VALUES:
        return cast(GitBranchBranchSyncStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GIT_BRANCH_BRANCH_SYNC_STATUS_VALUES!r}")
