from typing import Literal, cast

ResponseDTOListServiceAccountStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LIST_SERVICE_ACCOUNT_STATUS_VALUES: set[ResponseDTOListServiceAccountStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_list_service_account_status(value: str) -> ResponseDTOListServiceAccountStatus:
    if value in RESPONSE_DTO_LIST_SERVICE_ACCOUNT_STATUS_VALUES:
        return cast(ResponseDTOListServiceAccountStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LIST_SERVICE_ACCOUNT_STATUS_VALUES!r}")
