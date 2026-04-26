from typing import Literal, cast

ResponseDTOProjectResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PROJECT_RESPONSE_STATUS_VALUES: set[ResponseDTOProjectResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_project_response_status(value: str) -> ResponseDTOProjectResponseStatus:
    if value in RESPONSE_DTO_PROJECT_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOProjectResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PROJECT_RESPONSE_STATUS_VALUES!r}")
