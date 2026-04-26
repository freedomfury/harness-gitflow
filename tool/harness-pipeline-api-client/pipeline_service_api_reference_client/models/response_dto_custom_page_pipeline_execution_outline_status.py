from typing import Literal, cast

ResponseDTOCustomPagePipelineExecutionOutlineStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_CUSTOM_PAGE_PIPELINE_EXECUTION_OUTLINE_STATUS_VALUES: set[
    ResponseDTOCustomPagePipelineExecutionOutlineStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_custom_page_pipeline_execution_outline_status(
    value: str,
) -> ResponseDTOCustomPagePipelineExecutionOutlineStatus:
    if value in RESPONSE_DTO_CUSTOM_PAGE_PIPELINE_EXECUTION_OUTLINE_STATUS_VALUES:
        return cast(ResponseDTOCustomPagePipelineExecutionOutlineStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_CUSTOM_PAGE_PIPELINE_EXECUTION_OUTLINE_STATUS_VALUES!r}"
    )
