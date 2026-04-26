from typing import Literal, cast

ResponseDTOServiceAccountStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SERVICE_ACCOUNT_STATUS_VALUES: set[ResponseDTOServiceAccountStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_service_account_status(value: str) -> ResponseDTOServiceAccountStatus:
    if value in RESPONSE_DTO_SERVICE_ACCOUNT_STATUS_VALUES:
        return cast(ResponseDTOServiceAccountStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SERVICE_ACCOUNT_STATUS_VALUES!r}")
