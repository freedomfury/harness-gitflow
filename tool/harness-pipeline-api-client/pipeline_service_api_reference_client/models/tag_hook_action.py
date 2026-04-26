from typing import Literal, cast

TagHookAction = Literal[
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

TAG_HOOK_ACTION_VALUES: set[TagHookAction] = {
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


def check_tag_hook_action(value: str) -> TagHookAction:
    if value in TAG_HOOK_ACTION_VALUES:
        return cast(TagHookAction, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TAG_HOOK_ACTION_VALUES!r}")
