from typing import Literal, cast

ReleaseHookOrBuilderAction = Literal[
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

RELEASE_HOOK_OR_BUILDER_ACTION_VALUES: set[ReleaseHookOrBuilderAction] = {
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


def check_release_hook_or_builder_action(value: str) -> ReleaseHookOrBuilderAction:
    if value in RELEASE_HOOK_OR_BUILDER_ACTION_VALUES:
        return cast(ReleaseHookOrBuilderAction, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RELEASE_HOOK_OR_BUILDER_ACTION_VALUES!r}")
