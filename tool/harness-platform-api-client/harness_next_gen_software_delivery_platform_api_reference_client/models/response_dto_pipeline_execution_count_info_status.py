from typing import Literal, cast

ResponseDTOPipelineExecutionCountInfoStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PIPELINE_EXECUTION_COUNT_INFO_STATUS_VALUES: set[ResponseDTOPipelineExecutionCountInfoStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_pipeline_execution_count_info_status(value: str) -> ResponseDTOPipelineExecutionCountInfoStatus:
    if value in RESPONSE_DTO_PIPELINE_EXECUTION_COUNT_INFO_STATUS_VALUES:
        return cast(ResponseDTOPipelineExecutionCountInfoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PIPELINE_EXECUTION_COUNT_INFO_STATUS_VALUES!r}"
    )
