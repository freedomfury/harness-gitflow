from typing import Literal, cast

StepTypeSubCategory = Literal["NONE", "STAGE_LEVEL", "STEP_LEVEL", "UNRECOGNIZED"]

STEP_TYPE_SUB_CATEGORY_VALUES: set[StepTypeSubCategory] = {
    "NONE",
    "STAGE_LEVEL",
    "STEP_LEVEL",
    "UNRECOGNIZED",
}


def check_step_type_sub_category(value: str) -> StepTypeSubCategory:
    if value in STEP_TYPE_SUB_CATEGORY_VALUES:
        return cast(StepTypeSubCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STEP_TYPE_SUB_CATEGORY_VALUES!r}")
