from typing import Literal, cast

FreezeResponseType = Literal["GLOBAL", "MANUAL"]

FREEZE_RESPONSE_TYPE_VALUES: set[FreezeResponseType] = {
    "GLOBAL",
    "MANUAL",
}


def check_freeze_response_type(value: str) -> FreezeResponseType:
    if value in FREEZE_RESPONSE_TYPE_VALUES:
        return cast(FreezeResponseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FREEZE_RESPONSE_TYPE_VALUES!r}")
