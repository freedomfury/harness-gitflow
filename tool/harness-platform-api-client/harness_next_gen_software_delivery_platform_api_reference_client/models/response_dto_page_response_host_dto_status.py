from typing import Literal, cast

ResponseDTOPageResponseHostDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_HOST_DTO_STATUS_VALUES: set[ResponseDTOPageResponseHostDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_host_dto_status(value: str) -> ResponseDTOPageResponseHostDTOStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_HOST_DTO_STATUS_VALUES:
        return cast(ResponseDTOPageResponseHostDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_HOST_DTO_STATUS_VALUES!r}"
    )
