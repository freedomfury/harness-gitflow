from typing import Literal, cast

ResponseDTOPageFileStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_FILE_STATUS_VALUES: set[ResponseDTOPageFileStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_file_status(value: str) -> ResponseDTOPageFileStatus:
    if value in RESPONSE_DTO_PAGE_FILE_STATUS_VALUES:
        return cast(ResponseDTOPageFileStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_FILE_STATUS_VALUES!r}")
