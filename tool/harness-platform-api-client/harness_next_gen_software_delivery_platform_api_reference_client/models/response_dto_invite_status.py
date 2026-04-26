from typing import Literal, cast

ResponseDTOInviteStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_INVITE_STATUS_VALUES: set[ResponseDTOInviteStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_invite_status(value: str) -> ResponseDTOInviteStatus:
    if value in RESPONSE_DTO_INVITE_STATUS_VALUES:
        return cast(ResponseDTOInviteStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_INVITE_STATUS_VALUES!r}")
