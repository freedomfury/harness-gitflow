from typing import Literal, cast

ManualExecutionRequestAction = Literal["MARK_AS_FAIL", "MARK_AS_RESUME"]

MANUAL_EXECUTION_REQUEST_ACTION_VALUES: set[ManualExecutionRequestAction] = {
    "MARK_AS_FAIL",
    "MARK_AS_RESUME",
}


def check_manual_execution_request_action(value: str) -> ManualExecutionRequestAction:
    if value in MANUAL_EXECUTION_REQUEST_ACTION_VALUES:
        return cast(ManualExecutionRequestAction, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MANUAL_EXECUTION_REQUEST_ACTION_VALUES!r}")
