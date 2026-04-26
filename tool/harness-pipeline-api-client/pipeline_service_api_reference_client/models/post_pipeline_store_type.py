from typing import Literal, cast

PostPipelineStoreType = Literal["INLINE", "INLINE_HC", "REMOTE"]

POST_PIPELINE_STORE_TYPE_VALUES: set[PostPipelineStoreType] = {
    "INLINE",
    "INLINE_HC",
    "REMOTE",
}


def check_post_pipeline_store_type(value: str) -> PostPipelineStoreType:
    if value in POST_PIPELINE_STORE_TYPE_VALUES:
        return cast(PostPipelineStoreType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POST_PIPELINE_STORE_TYPE_VALUES!r}")
