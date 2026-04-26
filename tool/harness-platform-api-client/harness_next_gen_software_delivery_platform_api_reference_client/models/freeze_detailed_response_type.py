from typing import Literal, cast

FreezeDetailedResponseType = Literal["GLOBAL", "MANUAL"]

FREEZE_DETAILED_RESPONSE_TYPE_VALUES: set[FreezeDetailedResponseType] = {
    "GLOBAL",
    "MANUAL",
}


def check_freeze_detailed_response_type(value: str) -> FreezeDetailedResponseType:
    if value in FREEZE_DETAILED_RESPONSE_TYPE_VALUES:
        return cast(FreezeDetailedResponseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FREEZE_DETAILED_RESPONSE_TYPE_VALUES!r}")
