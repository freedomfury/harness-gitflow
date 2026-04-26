from typing import Literal, cast

HarnessApprovalActivityAction = Literal["APPROVE", "REJECT"]

HARNESS_APPROVAL_ACTIVITY_ACTION_VALUES: set[HarnessApprovalActivityAction] = {
    "APPROVE",
    "REJECT",
}


def check_harness_approval_activity_action(value: str) -> HarnessApprovalActivityAction:
    if value in HARNESS_APPROVAL_ACTIVITY_ACTION_VALUES:
        return cast(HarnessApprovalActivityAction, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HARNESS_APPROVAL_ACTIVITY_ACTION_VALUES!r}")
