from typing import Literal, cast

TriggerEventStatusStatus = Literal["FAILED", "SKIPPED", "SUCCESS"]

TRIGGER_EVENT_STATUS_STATUS_VALUES: set[TriggerEventStatusStatus] = {
    "FAILED",
    "SKIPPED",
    "SUCCESS",
}


def check_trigger_event_status_status(value: str) -> TriggerEventStatusStatus:
    if value in TRIGGER_EVENT_STATUS_STATUS_VALUES:
        return cast(TriggerEventStatusStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRIGGER_EVENT_STATUS_STATUS_VALUES!r}")
