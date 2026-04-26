from typing import Literal, cast

ExecutionNodeManualInterventionAvailableActionsItem = Literal[
    "CUSTOM_FAILURE",
    "END_EXECUTION",
    "IGNORE",
    "MANUAL_INTERVENTION",
    "MARK_AS_FAILURE",
    "MARK_AS_SUCCESS",
    "ON_FAIL",
    "PIPELINE_ROLLBACK",
    "RETRY",
    "STAGE_ROLLBACK",
    "STEP_GROUP_ROLLBACK",
    "UNKNOWN",
    "UNRECOGNIZED",
]

EXECUTION_NODE_MANUAL_INTERVENTION_AVAILABLE_ACTIONS_ITEM_VALUES: set[
    ExecutionNodeManualInterventionAvailableActionsItem
] = {
    "CUSTOM_FAILURE",
    "END_EXECUTION",
    "IGNORE",
    "MANUAL_INTERVENTION",
    "MARK_AS_FAILURE",
    "MARK_AS_SUCCESS",
    "ON_FAIL",
    "PIPELINE_ROLLBACK",
    "RETRY",
    "STAGE_ROLLBACK",
    "STEP_GROUP_ROLLBACK",
    "UNKNOWN",
    "UNRECOGNIZED",
}


def check_execution_node_manual_intervention_available_actions_item(
    value: str,
) -> ExecutionNodeManualInterventionAvailableActionsItem:
    if value in EXECUTION_NODE_MANUAL_INTERVENTION_AVAILABLE_ACTIONS_ITEM_VALUES:
        return cast(ExecutionNodeManualInterventionAvailableActionsItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXECUTION_NODE_MANUAL_INTERVENTION_AVAILABLE_ACTIONS_ITEM_VALUES!r}"
    )
