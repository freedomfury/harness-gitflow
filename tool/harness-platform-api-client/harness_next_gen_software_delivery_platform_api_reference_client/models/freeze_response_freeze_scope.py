from typing import Literal, cast

FreezeResponseFreezeScope = Literal["account", "org", "project", "unknown"]

FREEZE_RESPONSE_FREEZE_SCOPE_VALUES: set[FreezeResponseFreezeScope] = {
    "account",
    "org",
    "project",
    "unknown",
}


def check_freeze_response_freeze_scope(value: str) -> FreezeResponseFreezeScope:
    if value in FREEZE_RESPONSE_FREEZE_SCOPE_VALUES:
        return cast(FreezeResponseFreezeScope, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FREEZE_RESPONSE_FREEZE_SCOPE_VALUES!r}")
