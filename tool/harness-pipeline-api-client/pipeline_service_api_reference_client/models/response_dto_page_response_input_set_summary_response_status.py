from typing import Literal, cast

ResponseDTOPageResponseInputSetSummaryResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_INPUT_SET_SUMMARY_RESPONSE_STATUS_VALUES: set[
    ResponseDTOPageResponseInputSetSummaryResponseStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_input_set_summary_response_status(
    value: str,
) -> ResponseDTOPageResponseInputSetSummaryResponseStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_INPUT_SET_SUMMARY_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPageResponseInputSetSummaryResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_INPUT_SET_SUMMARY_RESPONSE_STATUS_VALUES!r}"
    )
