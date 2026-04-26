from typing import Literal, cast

ResponseDTOQueuedPipelineBulkAbortResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_QUEUED_PIPELINE_BULK_ABORT_RESPONSE_STATUS_VALUES: set[
    ResponseDTOQueuedPipelineBulkAbortResponseStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_queued_pipeline_bulk_abort_response_status(
    value: str,
) -> ResponseDTOQueuedPipelineBulkAbortResponseStatus:
    if value in RESPONSE_DTO_QUEUED_PIPELINE_BULK_ABORT_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOQueuedPipelineBulkAbortResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_QUEUED_PIPELINE_BULK_ABORT_RESPONSE_STATUS_VALUES!r}"
    )
