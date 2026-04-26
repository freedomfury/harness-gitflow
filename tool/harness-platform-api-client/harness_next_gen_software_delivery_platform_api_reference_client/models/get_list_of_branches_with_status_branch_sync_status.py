from typing import Literal, cast

GetListOfBranchesWithStatusBranchSyncStatus = Literal["SYNCED", "SYNCING", "UNSYNCED"]

GET_LIST_OF_BRANCHES_WITH_STATUS_BRANCH_SYNC_STATUS_VALUES: set[GetListOfBranchesWithStatusBranchSyncStatus] = {
    "SYNCED",
    "SYNCING",
    "UNSYNCED",
}


def check_get_list_of_branches_with_status_branch_sync_status(
    value: str,
) -> GetListOfBranchesWithStatusBranchSyncStatus:
    if value in GET_LIST_OF_BRANCHES_WITH_STATUS_BRANCH_SYNC_STATUS_VALUES:
        return cast(GetListOfBranchesWithStatusBranchSyncStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GET_LIST_OF_BRANCHES_WITH_STATUS_BRANCH_SYNC_STATUS_VALUES!r}"
    )
