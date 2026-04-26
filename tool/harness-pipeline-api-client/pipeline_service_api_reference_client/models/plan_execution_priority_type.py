from typing import Literal, cast

PlanExecutionPriorityType = Literal["HIGH", "LOW", "NORMAL"]

PLAN_EXECUTION_PRIORITY_TYPE_VALUES: set[PlanExecutionPriorityType] = {
    "HIGH",
    "LOW",
    "NORMAL",
}


def check_plan_execution_priority_type(value: str) -> PlanExecutionPriorityType:
    if value in PLAN_EXECUTION_PRIORITY_TYPE_VALUES:
        return cast(PlanExecutionPriorityType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PLAN_EXECUTION_PRIORITY_TYPE_VALUES!r}")
