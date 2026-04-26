from typing import Literal, cast

ResponseDTOCreateAnnotationsResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_CREATE_ANNOTATIONS_RESPONSE_STATUS_VALUES: set[ResponseDTOCreateAnnotationsResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_create_annotations_response_status(value: str) -> ResponseDTOCreateAnnotationsResponseStatus:
    if value in RESPONSE_DTO_CREATE_ANNOTATIONS_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOCreateAnnotationsResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_CREATE_ANNOTATIONS_RESPONSE_STATUS_VALUES!r}"
    )
