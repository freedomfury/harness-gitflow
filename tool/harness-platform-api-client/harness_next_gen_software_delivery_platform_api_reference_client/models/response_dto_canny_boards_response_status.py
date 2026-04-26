from typing import Literal, cast

ResponseDTOCannyBoardsResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_CANNY_BOARDS_RESPONSE_STATUS_VALUES: set[ResponseDTOCannyBoardsResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_canny_boards_response_status(value: str) -> ResponseDTOCannyBoardsResponseStatus:
    if value in RESPONSE_DTO_CANNY_BOARDS_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOCannyBoardsResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_CANNY_BOARDS_RESPONSE_STATUS_VALUES!r}")
