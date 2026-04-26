from typing import Literal, cast

ApprovalInstanceResponseType = Literal["CustomApproval", "HarnessApproval", "JiraApproval", "ServiceNowApproval"]

APPROVAL_INSTANCE_RESPONSE_TYPE_VALUES: set[ApprovalInstanceResponseType] = {
    "CustomApproval",
    "HarnessApproval",
    "JiraApproval",
    "ServiceNowApproval",
}


def check_approval_instance_response_type(value: str) -> ApprovalInstanceResponseType:
    if value in APPROVAL_INSTANCE_RESPONSE_TYPE_VALUES:
        return cast(ApprovalInstanceResponseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {APPROVAL_INSTANCE_RESPONSE_TYPE_VALUES!r}")
