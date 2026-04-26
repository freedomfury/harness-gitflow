from typing import Literal, cast

HarnessApprovalActivityRequestAction = Literal["APPROVE", "REJECT"]

HARNESS_APPROVAL_ACTIVITY_REQUEST_ACTION_VALUES: set[HarnessApprovalActivityRequestAction] = {
    "APPROVE",
    "REJECT",
}


def check_harness_approval_activity_request_action(value: str) -> HarnessApprovalActivityRequestAction:
    if value in HARNESS_APPROVAL_ACTIVITY_REQUEST_ACTION_VALUES:
        return cast(HarnessApprovalActivityRequestAction, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HARNESS_APPROVAL_ACTIVITY_REQUEST_ACTION_VALUES!r}")
