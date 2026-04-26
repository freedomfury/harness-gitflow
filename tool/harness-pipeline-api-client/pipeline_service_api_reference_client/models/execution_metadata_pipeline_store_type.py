from typing import Literal, cast

ExecutionMetadataPipelineStoreType = Literal["INLINE", "REMOTE", "UNDEFINED", "UNRECOGNIZED"]

EXECUTION_METADATA_PIPELINE_STORE_TYPE_VALUES: set[ExecutionMetadataPipelineStoreType] = {
    "INLINE",
    "REMOTE",
    "UNDEFINED",
    "UNRECOGNIZED",
}


def check_execution_metadata_pipeline_store_type(value: str) -> ExecutionMetadataPipelineStoreType:
    if value in EXECUTION_METADATA_PIPELINE_STORE_TYPE_VALUES:
        return cast(ExecutionMetadataPipelineStoreType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {EXECUTION_METADATA_PIPELINE_STORE_TYPE_VALUES!r}")
