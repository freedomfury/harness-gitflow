from typing import Literal, cast

ResponseDTOCannyCategoriesResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_CANNY_CATEGORIES_RESPONSE_STATUS_VALUES: set[ResponseDTOCannyCategoriesResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_canny_categories_response_status(value: str) -> ResponseDTOCannyCategoriesResponseStatus:
    if value in RESPONSE_DTO_CANNY_CATEGORIES_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOCannyCategoriesResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_CANNY_CATEGORIES_RESPONSE_STATUS_VALUES!r}"
    )
