from typing import Literal, cast

InterruptEffectDTOInterruptType = Literal[
    "ABORT",
    "ABORT_ALL",
    "CUSTOM_FAILURE",
    "END_EXECUTION",
    "EXPIRE_ALL",
    "IGNORE",
    "MARK_EXPIRED",
    "MARK_FAILED",
    "MARK_SUCCESS",
    "NEXT_STEP",
    "PAUSE",
    "PAUSE_ALL",
    "PROCEED_WITH_DEFAULT",
    "RESUME",
    "RESUME_ALL",
    "RETRY",
    "UNKNOWN",
    "UNRECOGNIZED",
    "USER_MARKED_FAIL_ALL",
    "WAITING_FOR_MANUAL_INTERVENTION",
]

INTERRUPT_EFFECT_DTO_INTERRUPT_TYPE_VALUES: set[InterruptEffectDTOInterruptType] = {
    "ABORT",
    "ABORT_ALL",
    "CUSTOM_FAILURE",
    "END_EXECUTION",
    "EXPIRE_ALL",
    "IGNORE",
    "MARK_EXPIRED",
    "MARK_FAILED",
    "MARK_SUCCESS",
    "NEXT_STEP",
    "PAUSE",
    "PAUSE_ALL",
    "PROCEED_WITH_DEFAULT",
    "RESUME",
    "RESUME_ALL",
    "RETRY",
    "UNKNOWN",
    "UNRECOGNIZED",
    "USER_MARKED_FAIL_ALL",
    "WAITING_FOR_MANUAL_INTERVENTION",
}


def check_interrupt_effect_dto_interrupt_type(value: str) -> InterruptEffectDTOInterruptType:
    if value in INTERRUPT_EFFECT_DTO_INTERRUPT_TYPE_VALUES:
        return cast(InterruptEffectDTOInterruptType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {INTERRUPT_EFFECT_DTO_INTERRUPT_TYPE_VALUES!r}")
