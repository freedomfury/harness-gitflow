from typing import Literal, cast

TagHookOrBuilderAction = Literal[
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

TAG_HOOK_OR_BUILDER_ACTION_VALUES: set[TagHookOrBuilderAction] = {
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


def check_tag_hook_or_builder_action(value: str) -> TagHookOrBuilderAction:
    if value in TAG_HOOK_OR_BUILDER_ACTION_VALUES:
        return cast(TagHookOrBuilderAction, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TAG_HOOK_OR_BUILDER_ACTION_VALUES!r}")
