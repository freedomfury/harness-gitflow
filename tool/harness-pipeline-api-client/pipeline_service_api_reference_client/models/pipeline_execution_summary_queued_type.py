from typing import Literal, cast

PipelineExecutionSummaryQueuedType = Literal[
    "MAX_CONCURRENCY_NOT_REACHED", "MAX_CONCURRENCY_REACHED", "PRIORITY_CONCURRENCY_REACHED"
]

PIPELINE_EXECUTION_SUMMARY_QUEUED_TYPE_VALUES: set[PipelineExecutionSummaryQueuedType] = {
    "MAX_CONCURRENCY_NOT_REACHED",
    "MAX_CONCURRENCY_REACHED",
    "PRIORITY_CONCURRENCY_REACHED",
}


def check_pipeline_execution_summary_queued_type(value: str) -> PipelineExecutionSummaryQueuedType:
    if value in PIPELINE_EXECUTION_SUMMARY_QUEUED_TYPE_VALUES:
        return cast(PipelineExecutionSummaryQueuedType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PIPELINE_EXECUTION_SUMMARY_QUEUED_TYPE_VALUES!r}")
