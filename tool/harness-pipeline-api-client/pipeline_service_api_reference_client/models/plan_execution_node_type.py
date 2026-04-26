from typing import Literal, cast

PlanExecutionNodeType = Literal["IDENTITY_PLAN_NODE", "PLAN", "PLAN_NODE"]

PLAN_EXECUTION_NODE_TYPE_VALUES: set[PlanExecutionNodeType] = {
    "IDENTITY_PLAN_NODE",
    "PLAN",
    "PLAN_NODE",
}


def check_plan_execution_node_type(value: str) -> PlanExecutionNodeType:
    if value in PLAN_EXECUTION_NODE_TYPE_VALUES:
        return cast(PlanExecutionNodeType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PLAN_EXECUTION_NODE_TYPE_VALUES!r}")
