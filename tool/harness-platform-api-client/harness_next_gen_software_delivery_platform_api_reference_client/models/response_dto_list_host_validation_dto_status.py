from typing import Literal, cast

ResponseDTOListHostValidationDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LIST_HOST_VALIDATION_DTO_STATUS_VALUES: set[ResponseDTOListHostValidationDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_list_host_validation_dto_status(value: str) -> ResponseDTOListHostValidationDTOStatus:
    if value in RESPONSE_DTO_LIST_HOST_VALIDATION_DTO_STATUS_VALUES:
        return cast(ResponseDTOListHostValidationDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LIST_HOST_VALIDATION_DTO_STATUS_VALUES!r}"
    )
