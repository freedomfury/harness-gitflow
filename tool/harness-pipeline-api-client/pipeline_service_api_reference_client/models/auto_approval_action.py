from typing import Literal, cast

AutoApprovalAction = Literal["APPROVE"]

AUTO_APPROVAL_ACTION_VALUES: set[AutoApprovalAction] = {
    "APPROVE",
}


def check_auto_approval_action(value: str) -> AutoApprovalAction:
    if value in AUTO_APPROVAL_ACTION_VALUES:
        return cast(AutoApprovalAction, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AUTO_APPROVAL_ACTION_VALUES!r}")
