from typing import Literal, cast

ResponseDTOPagePMSPipelineSummaryResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_PMS_PIPELINE_SUMMARY_RESPONSE_STATUS_VALUES: set[ResponseDTOPagePMSPipelineSummaryResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_pms_pipeline_summary_response_status(
    value: str,
) -> ResponseDTOPagePMSPipelineSummaryResponseStatus:
    if value in RESPONSE_DTO_PAGE_PMS_PIPELINE_SUMMARY_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPagePMSPipelineSummaryResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_PMS_PIPELINE_SUMMARY_RESPONSE_STATUS_VALUES!r}"
    )
