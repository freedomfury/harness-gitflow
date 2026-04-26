from typing import Literal, cast

ResponseDTOPageResponseInviteStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_INVITE_STATUS_VALUES: set[ResponseDTOPageResponseInviteStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_invite_status(value: str) -> ResponseDTOPageResponseInviteStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_INVITE_STATUS_VALUES:
        return cast(ResponseDTOPageResponseInviteStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_INVITE_STATUS_VALUES!r}")
