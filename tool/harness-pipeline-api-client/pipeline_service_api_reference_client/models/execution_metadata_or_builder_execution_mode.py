from typing import Literal, cast

ExecutionMetadataOrBuilderExecutionMode = Literal[
    "NORMAL", "PIPELINE_ROLLBACK", "POST_EXECUTION_ROLLBACK", "UNDEFINED_MODE", "UNRECOGNIZED"
]

EXECUTION_METADATA_OR_BUILDER_EXECUTION_MODE_VALUES: set[ExecutionMetadataOrBuilderExecutionMode] = {
    "NORMAL",
    "PIPELINE_ROLLBACK",
    "POST_EXECUTION_ROLLBACK",
    "UNDEFINED_MODE",
    "UNRECOGNIZED",
}


def check_execution_metadata_or_builder_execution_mode(value: str) -> ExecutionMetadataOrBuilderExecutionMode:
    if value in EXECUTION_METADATA_OR_BUILDER_EXECUTION_MODE_VALUES:
        return cast(ExecutionMetadataOrBuilderExecutionMode, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXECUTION_METADATA_OR_BUILDER_EXECUTION_MODE_VALUES!r}"
    )
