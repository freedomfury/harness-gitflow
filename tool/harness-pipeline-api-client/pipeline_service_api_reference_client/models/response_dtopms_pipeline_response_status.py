from typing import Literal, cast

ResponseDTOPMSPipelineResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTOPMS_PIPELINE_RESPONSE_STATUS_VALUES: set[ResponseDTOPMSPipelineResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dtopms_pipeline_response_status(value: str) -> ResponseDTOPMSPipelineResponseStatus:
    if value in RESPONSE_DTOPMS_PIPELINE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPMSPipelineResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTOPMS_PIPELINE_RESPONSE_STATUS_VALUES!r}")
