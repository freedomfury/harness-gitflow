from typing import Literal, cast

ResponseDTOPageResponseKeyStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_KEY_STATUS_VALUES: set[ResponseDTOPageResponseKeyStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_key_status(value: str) -> ResponseDTOPageResponseKeyStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_KEY_STATUS_VALUES:
        return cast(ResponseDTOPageResponseKeyStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_KEY_STATUS_VALUES!r}")
