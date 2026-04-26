from typing import Literal, cast

PipelineExecutionFilterPropertiesExecutionModeFilter = Literal["ALL", "DEFAULT", "ROLLBACK"]

PIPELINE_EXECUTION_FILTER_PROPERTIES_EXECUTION_MODE_FILTER_VALUES: set[
    PipelineExecutionFilterPropertiesExecutionModeFilter
] = {
    "ALL",
    "DEFAULT",
    "ROLLBACK",
}


def check_pipeline_execution_filter_properties_execution_mode_filter(
    value: str,
) -> PipelineExecutionFilterPropertiesExecutionModeFilter:
    if value in PIPELINE_EXECUTION_FILTER_PROPERTIES_EXECUTION_MODE_FILTER_VALUES:
        return cast(PipelineExecutionFilterPropertiesExecutionModeFilter, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PIPELINE_EXECUTION_FILTER_PROPERTIES_EXECUTION_MODE_FILTER_VALUES!r}"
    )
