from typing import Literal, cast

StepTypeOrBuilderSubCategory = Literal["NONE", "STAGE_LEVEL", "STEP_LEVEL", "UNRECOGNIZED"]

STEP_TYPE_OR_BUILDER_SUB_CATEGORY_VALUES: set[StepTypeOrBuilderSubCategory] = {
    "NONE",
    "STAGE_LEVEL",
    "STEP_LEVEL",
    "UNRECOGNIZED",
}


def check_step_type_or_builder_sub_category(value: str) -> StepTypeOrBuilderSubCategory:
    if value in STEP_TYPE_OR_BUILDER_SUB_CATEGORY_VALUES:
        return cast(StepTypeOrBuilderSubCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STEP_TYPE_OR_BUILDER_SUB_CATEGORY_VALUES!r}")
