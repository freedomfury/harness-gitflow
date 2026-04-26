from typing import Literal, cast

ApprovalInstanceResponseStatus = Literal["ABORTED", "APPROVED", "EXPIRED", "FAILED", "REJECTED", "WAITING"]

APPROVAL_INSTANCE_RESPONSE_STATUS_VALUES: set[ApprovalInstanceResponseStatus] = {
    "ABORTED",
    "APPROVED",
    "EXPIRED",
    "FAILED",
    "REJECTED",
    "WAITING",
}


def check_approval_instance_response_status(value: str) -> ApprovalInstanceResponseStatus:
    if value in APPROVAL_INSTANCE_RESPONSE_STATUS_VALUES:
        return cast(ApprovalInstanceResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {APPROVAL_INSTANCE_RESPONSE_STATUS_VALUES!r}")
