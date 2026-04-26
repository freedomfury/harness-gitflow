from typing import Literal, cast

HandleStageInterruptInterruptType = Literal["AbortAll", "UserMarkedFailure"]

HANDLE_STAGE_INTERRUPT_INTERRUPT_TYPE_VALUES: set[HandleStageInterruptInterruptType] = {
    "AbortAll",
    "UserMarkedFailure",
}


def check_handle_stage_interrupt_interrupt_type(value: str) -> HandleStageInterruptInterruptType:
    if value in HANDLE_STAGE_INTERRUPT_INTERRUPT_TYPE_VALUES:
        return cast(HandleStageInterruptInterruptType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {HANDLE_STAGE_INTERRUPT_INTERRUPT_TYPE_VALUES!r}")
