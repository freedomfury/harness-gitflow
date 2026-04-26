from typing import Literal, cast

PullRequestHookAction = Literal[
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

PULL_REQUEST_HOOK_ACTION_VALUES: set[PullRequestHookAction] = {
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


def check_pull_request_hook_action(value: str) -> PullRequestHookAction:
    if value in PULL_REQUEST_HOOK_ACTION_VALUES:
        return cast(PullRequestHookAction, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PULL_REQUEST_HOOK_ACTION_VALUES!r}")
