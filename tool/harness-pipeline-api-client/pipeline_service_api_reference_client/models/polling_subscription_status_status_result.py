from typing import Literal, cast

PollingSubscriptionStatusStatusResult = Literal["FAILED", "PENDING", "SUCCESS", "UNKNOWN"]

POLLING_SUBSCRIPTION_STATUS_STATUS_RESULT_VALUES: set[PollingSubscriptionStatusStatusResult] = {
    "FAILED",
    "PENDING",
    "SUCCESS",
    "UNKNOWN",
}


def check_polling_subscription_status_status_result(value: str) -> PollingSubscriptionStatusStatusResult:
    if value in POLLING_SUBSCRIPTION_STATUS_STATUS_RESULT_VALUES:
        return cast(PollingSubscriptionStatusStatusResult, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POLLING_SUBSCRIPTION_STATUS_STATUS_RESULT_VALUES!r}")
