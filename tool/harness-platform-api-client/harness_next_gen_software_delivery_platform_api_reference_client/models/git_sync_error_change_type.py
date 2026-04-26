from typing import Literal, cast

GitSyncErrorChangeType = Literal["ADD", "ADD_V2", "DELETE", "MODIFY", "NONE", "RENAME", "UPDATE_V2"]

GIT_SYNC_ERROR_CHANGE_TYPE_VALUES: set[GitSyncErrorChangeType] = {
    "ADD",
    "ADD_V2",
    "DELETE",
    "MODIFY",
    "NONE",
    "RENAME",
    "UPDATE_V2",
}


def check_git_sync_error_change_type(value: str) -> GitSyncErrorChangeType:
    if value in GIT_SYNC_ERROR_CHANGE_TYPE_VALUES:
        return cast(GitSyncErrorChangeType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GIT_SYNC_ERROR_CHANGE_TYPE_VALUES!r}")
