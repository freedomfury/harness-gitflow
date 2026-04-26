from typing import Literal, cast

ResponseDTOPipelineExecutionDetailStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PIPELINE_EXECUTION_DETAIL_STATUS_VALUES: set[ResponseDTOPipelineExecutionDetailStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_pipeline_execution_detail_status(value: str) -> ResponseDTOPipelineExecutionDetailStatus:
    if value in RESPONSE_DTO_PIPELINE_EXECUTION_DETAIL_STATUS_VALUES:
        return cast(ResponseDTOPipelineExecutionDetailStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PIPELINE_EXECUTION_DETAIL_STATUS_VALUES!r}"
    )
