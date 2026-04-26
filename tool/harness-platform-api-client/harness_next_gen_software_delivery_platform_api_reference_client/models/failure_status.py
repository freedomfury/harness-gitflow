from typing import Literal, cast

FailureStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

FAILURE_STATUS_VALUES: set[FailureStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_failure_status(value: str) -> FailureStatus:
    if value in FAILURE_STATUS_VALUES:
        return cast(FailureStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FAILURE_STATUS_VALUES!r}")
