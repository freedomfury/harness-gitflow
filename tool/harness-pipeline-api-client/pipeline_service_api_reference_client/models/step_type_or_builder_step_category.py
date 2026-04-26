from typing import Literal, cast

StepTypeOrBuilderStepCategory = Literal[
    "FORK", "INSERT", "PIPELINE", "STAGE", "STAGES", "STEP", "STEP_GROUP", "STRATEGY", "UNKNOWN", "UNRECOGNIZED"
]

STEP_TYPE_OR_BUILDER_STEP_CATEGORY_VALUES: set[StepTypeOrBuilderStepCategory] = {
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


def check_step_type_or_builder_step_category(value: str) -> StepTypeOrBuilderStepCategory:
    if value in STEP_TYPE_OR_BUILDER_STEP_CATEGORY_VALUES:
        return cast(StepTypeOrBuilderStepCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STEP_TYPE_OR_BUILDER_STEP_CATEGORY_VALUES!r}")
