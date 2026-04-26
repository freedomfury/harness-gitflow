from typing import Literal, cast

QueuedPipelineExecutionPriorityType = Literal["HIGH", "LOW", "NORMAL"]

QUEUED_PIPELINE_EXECUTION_PRIORITY_TYPE_VALUES: set[QueuedPipelineExecutionPriorityType] = {
    "HIGH",
    "LOW",
    "NORMAL",
}


def check_queued_pipeline_execution_priority_type(value: str) -> QueuedPipelineExecutionPriorityType:
    if value in QUEUED_PIPELINE_EXECUTION_PRIORITY_TYPE_VALUES:
        return cast(QueuedPipelineExecutionPriorityType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {QUEUED_PIPELINE_EXECUTION_PRIORITY_TYPE_VALUES!r}")
