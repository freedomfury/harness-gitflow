from typing import Literal, cast

StepTypeStepCategory = Literal[
    "FORK", "INSERT", "PIPELINE", "STAGE", "STAGES", "STEP", "STEP_GROUP", "STRATEGY", "UNKNOWN", "UNRECOGNIZED"
]

STEP_TYPE_STEP_CATEGORY_VALUES: set[StepTypeStepCategory] = {
    "FORK",
    "INSERT",
    "PIPELINE",
    "STAGE",
    "STAGES",
    "STEP",
    "STEP_GROUP",
    "STRATEGY",
    "UNKNOWN",
    "UNRECOGNIZED",
}


def check_step_type_step_category(value: str) -> StepTypeStepCategory:
    if value in STEP_TYPE_STEP_CATEGORY_VALUES:
        return cast(StepTypeStepCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STEP_TYPE_STEP_CATEGORY_VALUES!r}")
