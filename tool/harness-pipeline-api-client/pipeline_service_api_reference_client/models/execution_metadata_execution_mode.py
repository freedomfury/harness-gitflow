from typing import Literal, cast

ExecutionMetadataExecutionMode = Literal[
    "NORMAL", "PIPELINE_ROLLBACK", "POST_EXECUTION_ROLLBACK", "UNDEFINED_MODE", "UNRECOGNIZED"
]

EXECUTION_METADATA_EXECUTION_MODE_VALUES: set[ExecutionMetadataExecutionMode] = {
    "NORMAL",
    "PIPELINE_ROLLBACK",
    "POST_EXECUTION_ROLLBACK",
    "UNDEFINED_MODE",
    "UNRECOGNIZED",
}


def check_execution_metadata_execution_mode(value: str) -> ExecutionMetadataExecutionMode:
    if value in EXECUTION_METADATA_EXECUTION_MODE_VALUES:
        return cast(ExecutionMetadataExecutionMode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EXECUTION_METADATA_EXECUTION_MODE_VALUES!r}")
