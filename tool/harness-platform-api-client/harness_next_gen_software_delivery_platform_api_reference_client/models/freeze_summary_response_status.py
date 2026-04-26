from typing import Literal, cast

FreezeSummaryResponseStatus = Literal["Disabled", "Enabled"]

FREEZE_SUMMARY_RESPONSE_STATUS_VALUES: set[FreezeSummaryResponseStatus] = {
    "Disabled",
    "Enabled",
}


def check_freeze_summary_response_status(value: str) -> FreezeSummaryResponseStatus:
    if value in FREEZE_SUMMARY_RESPONSE_STATUS_VALUES:
        return cast(FreezeSummaryResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FREEZE_SUMMARY_RESPONSE_STATUS_VALUES!r}")
