from typing import Literal, cast

PullRequestHookOrBuilderAction = Literal[
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

PULL_REQUEST_HOOK_OR_BUILDER_ACTION_VALUES: set[PullRequestHookOrBuilderAction] = {
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


def check_pull_request_hook_or_builder_action(value: str) -> PullRequestHookOrBuilderAction:
    if value in PULL_REQUEST_HOOK_OR_BUILDER_ACTION_VALUES:
        return cast(PullRequestHookOrBuilderAction, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PULL_REQUEST_HOOK_OR_BUILDER_ACTION_VALUES!r}")
