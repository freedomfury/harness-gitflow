from typing import Literal, cast

PipelineExecutionSummaryStoreType = Literal["INLINE", "INLINE_HC", "REMOTE"]

PIPELINE_EXECUTION_SUMMARY_STORE_TYPE_VALUES: set[PipelineExecutionSummaryStoreType] = {
    "INLINE",
    "INLINE_HC",
    "REMOTE",
}


def check_pipeline_execution_summary_store_type(value: str) -> PipelineExecutionSummaryStoreType:
    if value in PIPELINE_EXECUTION_SUMMARY_STORE_TYPE_VALUES:
        return cast(PipelineExecutionSummaryStoreType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PIPELINE_EXECUTION_SUMMARY_STORE_TYPE_VALUES!r}")
