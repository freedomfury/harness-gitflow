from typing import Literal, cast

TriggerStatusStatus = Literal["FAILED", "PENDING", "SUCCESS", "UNKNOWN"]

TRIGGER_STATUS_STATUS_VALUES: set[TriggerStatusStatus] = {
    "FAILED",
    "PENDING",
    "SUCCESS",
    "UNKNOWN",
}


def check_trigger_status_status(value: str) -> TriggerStatusStatus:
    if value in TRIGGER_STATUS_STATUS_VALUES:
        return cast(TriggerStatusStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRIGGER_STATUS_STATUS_VALUES!r}")
