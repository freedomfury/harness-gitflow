from typing import Literal, cast

PostPipelineV2StoreType = Literal["INLINE", "INLINE_HC", "REMOTE"]

POST_PIPELINE_V2_STORE_TYPE_VALUES: set[PostPipelineV2StoreType] = {
    "INLINE",
    "INLINE_HC",
    "REMOTE",
}


def check_post_pipeline_v2_store_type(value: str) -> PostPipelineV2StoreType:
    if value in POST_PIPELINE_V2_STORE_TYPE_VALUES:
        return cast(PostPipelineV2StoreType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {POST_PIPELINE_V2_STORE_TYPE_VALUES!r}")
