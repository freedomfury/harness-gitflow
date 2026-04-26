from typing import Literal, cast

ExecutionMetadataOrBuilderPipelineStoreType = Literal["INLINE", "REMOTE", "UNDEFINED", "UNRECOGNIZED"]

EXECUTION_METADATA_OR_BUILDER_PIPELINE_STORE_TYPE_VALUES: set[ExecutionMetadataOrBuilderPipelineStoreType] = {
    "INLINE",
    "REMOTE",
    "UNDEFINED",
    "UNRECOGNIZED",
}


def check_execution_metadata_or_builder_pipeline_store_type(value: str) -> ExecutionMetadataOrBuilderPipelineStoreType:
    if value in EXECUTION_METADATA_OR_BUILDER_PIPELINE_STORE_TYPE_VALUES:
        return cast(ExecutionMetadataOrBuilderPipelineStoreType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {EXECUTION_METADATA_OR_BUILDER_PIPELINE_STORE_TYPE_VALUES!r}"
    )
