from typing import Literal, cast

FreezeResponseStatus = Literal["Disabled", "Enabled"]

FREEZE_RESPONSE_STATUS_VALUES: set[FreezeResponseStatus] = {
    "Disabled",
    "Enabled",
}


def check_freeze_response_status(value: str) -> FreezeResponseStatus:
    if value in FREEZE_RESPONSE_STATUS_VALUES:
        return cast(FreezeResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FREEZE_RESPONSE_STATUS_VALUES!r}")
