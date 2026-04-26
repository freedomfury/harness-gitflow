from typing import Literal, cast

ResponseDTOPageResponseFreezeSummaryResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_FREEZE_SUMMARY_RESPONSE_STATUS_VALUES: set[
    ResponseDTOPageResponseFreezeSummaryResponseStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_freeze_summary_response_status(
    value: str,
) -> ResponseDTOPageResponseFreezeSummaryResponseStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_FREEZE_SUMMARY_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPageResponseFreezeSummaryResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_FREEZE_SUMMARY_RESPONSE_STATUS_VALUES!r}"
    )
