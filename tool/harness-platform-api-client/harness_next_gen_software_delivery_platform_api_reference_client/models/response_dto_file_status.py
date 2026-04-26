from typing import Literal, cast

ResponseDTOFileStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_FILE_STATUS_VALUES: set[ResponseDTOFileStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_file_status(value: str) -> ResponseDTOFileStatus:
    if value in RESPONSE_DTO_FILE_STATUS_VALUES:
        return cast(ResponseDTOFileStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_FILE_STATUS_VALUES!r}")
