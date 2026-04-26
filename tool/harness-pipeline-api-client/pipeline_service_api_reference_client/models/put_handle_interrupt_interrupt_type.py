from typing import Literal, cast

PutHandleInterruptInterruptType = Literal["AbortAll", "UserMarkedFailure"]

PUT_HANDLE_INTERRUPT_INTERRUPT_TYPE_VALUES: set[PutHandleInterruptInterruptType] = {
    "AbortAll",
    "UserMarkedFailure",
}


def check_put_handle_interrupt_interrupt_type(value: str) -> PutHandleInterruptInterruptType:
    if value in PUT_HANDLE_INTERRUPT_INTERRUPT_TYPE_VALUES:
        return cast(PutHandleInterruptInterruptType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PUT_HANDLE_INTERRUPT_INTERRUPT_TYPE_VALUES!r}")
