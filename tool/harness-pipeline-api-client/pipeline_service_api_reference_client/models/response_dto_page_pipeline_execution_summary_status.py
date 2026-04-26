from typing import Literal, cast

ResponseDTOPagePipelineExecutionSummaryStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_PIPELINE_EXECUTION_SUMMARY_STATUS_VALUES: set[ResponseDTOPagePipelineExecutionSummaryStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_pipeline_execution_summary_status(
    value: str,
) -> ResponseDTOPagePipelineExecutionSummaryStatus:
    if value in RESPONSE_DTO_PAGE_PIPELINE_EXECUTION_SUMMARY_STATUS_VALUES:
        return cast(ResponseDTOPagePipelineExecutionSummaryStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_PIPELINE_EXECUTION_SUMMARY_STATUS_VALUES!r}"
    )
