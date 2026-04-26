from typing import Literal, cast

ResponseDTOPipelineExecutionNotesStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PIPELINE_EXECUTION_NOTES_STATUS_VALUES: set[ResponseDTOPipelineExecutionNotesStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_pipeline_execution_notes_status(value: str) -> ResponseDTOPipelineExecutionNotesStatus:
    if value in RESPONSE_DTO_PIPELINE_EXECUTION_NOTES_STATUS_VALUES:
        return cast(ResponseDTOPipelineExecutionNotesStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PIPELINE_EXECUTION_NOTES_STATUS_VALUES!r}"
    )
