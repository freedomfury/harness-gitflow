from typing import Literal, cast

ResponseDTOPageResponseInputSetListResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_INPUT_SET_LIST_RESPONSE_STATUS_VALUES: set[
    ResponseDTOPageResponseInputSetListResponseStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_input_set_list_response_status(
    value: str,
) -> ResponseDTOPageResponseInputSetListResponseStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_INPUT_SET_LIST_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPageResponseInputSetListResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_INPUT_SET_LIST_RESPONSE_STATUS_VALUES!r}"
    )
