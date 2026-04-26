from typing import Literal, cast

PipelineExecutionSummaryExecutionMode = Literal[
    "NORMAL", "PIPELINE_ROLLBACK", "POST_EXECUTION_ROLLBACK", "UNDEFINED_MODE", "UNRECOGNIZED"
]

PIPELINE_EXECUTION_SUMMARY_EXECUTION_MODE_VALUES: set[PipelineExecutionSummaryExecutionMode] = {
    "NORMAL",
    "PIPELINE_ROLLBACK",
    "POST_EXECUTION_ROLLBACK",
    "UNDEFINED_MODE",
    "UNRECOGNIZED",
}


def check_pipeline_execution_summary_execution_mode(value: str) -> PipelineExecutionSummaryExecutionMode:
    if value in PIPELINE_EXECUTION_SUMMARY_EXECUTION_MODE_VALUES:
        return cast(PipelineExecutionSummaryExecutionMode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PIPELINE_EXECUTION_SUMMARY_EXECUTION_MODE_VALUES!r}")
