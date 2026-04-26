from typing import Literal, cast

FreezeSummaryResponseType = Literal["GLOBAL", "MANUAL"]

FREEZE_SUMMARY_RESPONSE_TYPE_VALUES: set[FreezeSummaryResponseType] = {
    "GLOBAL",
    "MANUAL",
}


def check_freeze_summary_response_type(value: str) -> FreezeSummaryResponseType:
    if value in FREEZE_SUMMARY_RESPONSE_TYPE_VALUES:
        return cast(FreezeSummaryResponseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FREEZE_SUMMARY_RESPONSE_TYPE_VALUES!r}")
