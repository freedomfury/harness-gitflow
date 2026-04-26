from typing import Literal, cast

ResponseDTOQueuedPipelineListResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_QUEUED_PIPELINE_LIST_RESPONSE_STATUS_VALUES: set[ResponseDTOQueuedPipelineListResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_queued_pipeline_list_response_status(value: str) -> ResponseDTOQueuedPipelineListResponseStatus:
    if value in RESPONSE_DTO_QUEUED_PIPELINE_LIST_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOQueuedPipelineListResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_QUEUED_PIPELINE_LIST_RESPONSE_STATUS_VALUES!r}"
    )
