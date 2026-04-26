from typing import Literal, cast

UnitProgressStatus = Literal["EXPIRED", "FAILURE", "QUEUED", "RUNNING", "SKIPPED", "SUCCESS", "UNKNOWN", "UNRECOGNIZED"]

UNIT_PROGRESS_STATUS_VALUES: set[UnitProgressStatus] = {
    "EXPIRED",
    "FAILURE",
    "QUEUED",
    "RUNNING",
    "SKIPPED",
    "SUCCESS",
    "UNKNOWN",
    "UNRECOGNIZED",
}


def check_unit_progress_status(value: str) -> UnitProgressStatus:
    if value in UNIT_PROGRESS_STATUS_VALUES:
        return cast(UnitProgressStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {UNIT_PROGRESS_STATUS_VALUES!r}")
