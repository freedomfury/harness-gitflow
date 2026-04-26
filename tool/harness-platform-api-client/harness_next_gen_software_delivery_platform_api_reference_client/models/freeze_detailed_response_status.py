from typing import Literal, cast

FreezeDetailedResponseStatus = Literal["Disabled", "Enabled"]

FREEZE_DETAILED_RESPONSE_STATUS_VALUES: set[FreezeDetailedResponseStatus] = {
    "Disabled",
    "Enabled",
}


def check_freeze_detailed_response_status(value: str) -> FreezeDetailedResponseStatus:
    if value in FREEZE_DETAILED_RESPONSE_STATUS_VALUES:
        return cast(FreezeDetailedResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FREEZE_DETAILED_RESPONSE_STATUS_VALUES!r}")
