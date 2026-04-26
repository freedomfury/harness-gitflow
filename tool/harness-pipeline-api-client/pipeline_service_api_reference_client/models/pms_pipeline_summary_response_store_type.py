from typing import Literal, cast

PMSPipelineSummaryResponseStoreType = Literal["INLINE", "INLINE_HC", "REMOTE"]

PMS_PIPELINE_SUMMARY_RESPONSE_STORE_TYPE_VALUES: set[PMSPipelineSummaryResponseStoreType] = {
    "INLINE",
    "INLINE_HC",
    "REMOTE",
}


def check_pms_pipeline_summary_response_store_type(value: str) -> PMSPipelineSummaryResponseStoreType:
    if value in PMS_PIPELINE_SUMMARY_RESPONSE_STORE_TYPE_VALUES:
        return cast(PMSPipelineSummaryResponseStoreType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {PMS_PIPELINE_SUMMARY_RESPONSE_STORE_TYPE_VALUES!r}")
