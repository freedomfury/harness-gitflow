from typing import Literal, cast

FreezeSummaryResponseFreezeScope = Literal["account", "org", "project", "unknown"]

FREEZE_SUMMARY_RESPONSE_FREEZE_SCOPE_VALUES: set[FreezeSummaryResponseFreezeScope] = {
    "account",
    "org",
    "project",
    "unknown",
}


def check_freeze_summary_response_freeze_scope(value: str) -> FreezeSummaryResponseFreezeScope:
    if value in FREEZE_SUMMARY_RESPONSE_FREEZE_SCOPE_VALUES:
        return cast(FreezeSummaryResponseFreezeScope, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FREEZE_SUMMARY_RESPONSE_FREEZE_SCOPE_VALUES!r}")
