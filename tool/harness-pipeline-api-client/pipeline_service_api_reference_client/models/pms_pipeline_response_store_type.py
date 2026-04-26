from typing import Literal, cast

PMSPipelineResponseStoreType = Literal["INLINE", "INLINE_HC", "REMOTE"]

PMS_PIPELINE_RESPONSE_STORE_TYPE_VALUES: set[PMSPipelineResponseStoreType] = {
    "INLINE",
    "INLINE_HC",
    "REMOTE",
}


def check_pms_pipeline_response_store_type(value: str) -> PMSPipelineResponseStoreType:
    if value in PMS_PIPELINE_RESPONSE_STORE_TYPE_VALUES:
        return cast(PMSPipelineResponseStoreType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PMS_PIPELINE_RESPONSE_STORE_TYPE_VALUES!r}")
