from typing import Literal, cast

BranchHookAction = Literal[
    "CLOSE",
    "CREATE",
    "DELETE",
    "DISMISSED",
    "EDIT",
    "LABEL",
    "MERGE",
    "OPEN",
    "PRERELEASE",
    "PUBLISH",
    "RELEASE",
    "REOPEN",
    "REVIEWREADY",
    "SUBMITTED",
    "SYNC",
    "UNKNOWN",
    "UNLABEL",
    "UNPUBLISH",
    "UNRECOGNIZED",
    "UPDATE",
]

BRANCH_HOOK_ACTION_VALUES: set[BranchHookAction] = {
    "CLOSE",
    "CREATE",
    "DELETE",
    "DISMISSED",
    "EDIT",
    "LABEL",
    "MERGE",
    "OPEN",
    "PRERELEASE",
    "PUBLISH",
    "RELEASE",
    "REOPEN",
    "REVIEWREADY",
    "SUBMITTED",
    "SYNC",
    "UNKNOWN",
    "UNLABEL",
    "UNPUBLISH",
    "UNRECOGNIZED",
    "UPDATE",
}


def check_branch_hook_action(value: str) -> BranchHookAction:
    if value in BRANCH_HOOK_ACTION_VALUES:
        return cast(BranchHookAction, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BRANCH_HOOK_ACTION_VALUES!r}")
