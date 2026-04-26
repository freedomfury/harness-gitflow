from typing import Literal, cast

ValidationStatusStatusResult = Literal["FAILED", "PENDING", "SUCCESS", "UNKNOWN"]

VALIDATION_STATUS_STATUS_RESULT_VALUES: set[ValidationStatusStatusResult] = {
    "FAILED",
    "PENDING",
    "SUCCESS",
    "UNKNOWN",
}


def check_validation_status_status_result(value: str) -> ValidationStatusStatusResult:
    if value in VALIDATION_STATUS_STATUS_RESULT_VALUES:
        return cast(ValidationStatusStatusResult, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VALIDATION_STATUS_STATUS_RESULT_VALUES!r}")
