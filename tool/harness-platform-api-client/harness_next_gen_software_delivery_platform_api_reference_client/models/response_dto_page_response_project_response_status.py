from typing import Literal, cast

ResponseDTOPageResponseProjectResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_PROJECT_RESPONSE_STATUS_VALUES: set[ResponseDTOPageResponseProjectResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_project_response_status(
    value: str,
) -> ResponseDTOPageResponseProjectResponseStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_PROJECT_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPageResponseProjectResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_PROJECT_RESPONSE_STATUS_VALUES!r}"
    )
