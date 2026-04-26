from typing import Literal, cast

ErrorStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

ERROR_STATUS_VALUES: set[ErrorStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_error_status(value: str) -> ErrorStatus:
    if value in ERROR_STATUS_VALUES:
        return cast(ErrorStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ERROR_STATUS_VALUES!r}")
