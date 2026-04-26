from typing import Literal, cast

ResponseDTOPipelineSaveResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PIPELINE_SAVE_RESPONSE_STATUS_VALUES: set[ResponseDTOPipelineSaveResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_pipeline_save_response_status(value: str) -> ResponseDTOPipelineSaveResponseStatus:
    if value in RESPONSE_DTO_PIPELINE_SAVE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPipelineSaveResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PIPELINE_SAVE_RESPONSE_STATUS_VALUES!r}"
    )
