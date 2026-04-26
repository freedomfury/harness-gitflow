from typing import Literal, cast

FreezeDetailedResponseFreezeScope = Literal["account", "org", "project", "unknown"]

FREEZE_DETAILED_RESPONSE_FREEZE_SCOPE_VALUES: set[FreezeDetailedResponseFreezeScope] = {
    "account",
    "org",
    "project",
    "unknown",
}


def check_freeze_detailed_response_freeze_scope(value: str) -> FreezeDetailedResponseFreezeScope:
    if value in FREEZE_DETAILED_RESPONSE_FREEZE_SCOPE_VALUES:
        return cast(FreezeDetailedResponseFreezeScope, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FREEZE_DETAILED_RESPONSE_FREEZE_SCOPE_VALUES!r}")
