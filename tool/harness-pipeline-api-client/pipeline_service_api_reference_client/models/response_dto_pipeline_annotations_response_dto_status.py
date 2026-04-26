from typing import Literal, cast

ResponseDTOPipelineAnnotationsResponseDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PIPELINE_ANNOTATIONS_RESPONSE_DTO_STATUS_VALUES: set[ResponseDTOPipelineAnnotationsResponseDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_pipeline_annotations_response_dto_status(
    value: str,
) -> ResponseDTOPipelineAnnotationsResponseDTOStatus:
    if value in RESPONSE_DTO_PIPELINE_ANNOTATIONS_RESPONSE_DTO_STATUS_VALUES:
        return cast(ResponseDTOPipelineAnnotationsResponseDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PIPELINE_ANNOTATIONS_RESPONSE_DTO_STATUS_VALUES!r}"
    )
