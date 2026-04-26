from typing import Literal, cast

ResponseDTOPMSPipelineSummaryResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTOPMS_PIPELINE_SUMMARY_RESPONSE_STATUS_VALUES: set[ResponseDTOPMSPipelineSummaryResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dtopms_pipeline_summary_response_status(value: str) -> ResponseDTOPMSPipelineSummaryResponseStatus:
    if value in RESPONSE_DTOPMS_PIPELINE_SUMMARY_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPMSPipelineSummaryResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTOPMS_PIPELINE_SUMMARY_RESPONSE_STATUS_VALUES!r}"
    )
