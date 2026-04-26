from typing import Literal, cast

ResponseDTOPagePipelineExecutionIdentifierSummaryStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_PIPELINE_EXECUTION_IDENTIFIER_SUMMARY_STATUS_VALUES: set[
    ResponseDTOPagePipelineExecutionIdentifierSummaryStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_pipeline_execution_identifier_summary_status(
    value: str,
) -> ResponseDTOPagePipelineExecutionIdentifierSummaryStatus:
    if value in RESPONSE_DTO_PAGE_PIPELINE_EXECUTION_IDENTIFIER_SUMMARY_STATUS_VALUES:
        return cast(ResponseDTOPagePipelineExecutionIdentifierSummaryStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_PIPELINE_EXECUTION_IDENTIFIER_SUMMARY_STATUS_VALUES!r}"
    )
