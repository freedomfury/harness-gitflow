from typing import Literal, cast

ResponseDTOOptionalInviteStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_OPTIONAL_INVITE_STATUS_VALUES: set[ResponseDTOOptionalInviteStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_optional_invite_status(value: str) -> ResponseDTOOptionalInviteStatus:
    if value in RESPONSE_DTO_OPTIONAL_INVITE_STATUS_VALUES:
        return cast(ResponseDTOOptionalInviteStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_OPTIONAL_INVITE_STATUS_VALUES!r}")
