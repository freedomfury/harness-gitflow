from typing import Literal, cast

ResponseDTOAnnotationContentResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_ANNOTATION_CONTENT_RESPONSE_STATUS_VALUES: set[ResponseDTOAnnotationContentResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_annotation_content_response_status(value: str) -> ResponseDTOAnnotationContentResponseStatus:
    if value in RESPONSE_DTO_ANNOTATION_CONTENT_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOAnnotationContentResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_ANNOTATION_CONTENT_RESPONSE_STATUS_VALUES!r}"
    )
