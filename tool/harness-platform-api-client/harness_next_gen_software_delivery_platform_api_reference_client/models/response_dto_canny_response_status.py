from typing import Literal, cast

ResponseDTOCannyResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_CANNY_RESPONSE_STATUS_VALUES: set[ResponseDTOCannyResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_canny_response_status(value: str) -> ResponseDTOCannyResponseStatus:
    if value in RESPONSE_DTO_CANNY_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOCannyResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_CANNY_RESPONSE_STATUS_VALUES!r}")
