from typing import Literal, cast

InterruptResponseType = Literal[
    "Abort",
    "AbortAll",
    "ExpireAll",
    "Ignore",
    "MarkAsFailure",
    "MarkAsSuccess",
    "Pause",
    "PipelineRollback",
    "Resume",
    "Retry",
    "StageRollback",
    "StepGroupRollback",
    "UserMarkedFailure",
]

INTERRUPT_RESPONSE_TYPE_VALUES: set[InterruptResponseType] = {
    "Abort",
    "AbortAll",
    "ExpireAll",
    "Ignore",
    "MarkAsFailure",
    "MarkAsSuccess",
    "Pause",
    "PipelineRollback",
    "Resume",
    "Retry",
    "StageRollback",
    "StepGroupRollback",
    "UserMarkedFailure",
}


def check_interrupt_response_type(value: str) -> InterruptResponseType:
    if value in INTERRUPT_RESPONSE_TYPE_VALUES:
        return cast(InterruptResponseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INTERRUPT_RESPONSE_TYPE_VALUES!r}")
