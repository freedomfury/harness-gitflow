from typing import Literal, cast

ResponseDTOAccountStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_ACCOUNT_STATUS_VALUES: set[ResponseDTOAccountStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_account_status(value: str) -> ResponseDTOAccountStatus:
    if value in RESPONSE_DTO_ACCOUNT_STATUS_VALUES:
        return cast(ResponseDTOAccountStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_ACCOUNT_STATUS_VALUES!r}")
