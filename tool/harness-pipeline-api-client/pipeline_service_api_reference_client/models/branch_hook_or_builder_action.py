from typing import Literal, cast

BranchHookOrBuilderAction = Literal[
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

BRANCH_HOOK_OR_BUILDER_ACTION_VALUES: set[BranchHookOrBuilderAction] = {
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


def check_branch_hook_or_builder_action(value: str) -> BranchHookOrBuilderAction:
    if value in BRANCH_HOOK_OR_BUILDER_ACTION_VALUES:
        return cast(BranchHookOrBuilderAction, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BRANCH_HOOK_OR_BUILDER_ACTION_VALUES!r}")
