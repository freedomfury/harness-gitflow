from typing import Literal, cast

ResponseDTOListServiceResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LIST_SERVICE_RESPONSE_STATUS_VALUES: set[ResponseDTOListServiceResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_list_service_response_status(value: str) -> ResponseDTOListServiceResponseStatus:
    if value in RESPONSE_DTO_LIST_SERVICE_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOListServiceResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LIST_SERVICE_RESPONSE_STATUS_VALUES!r}")
