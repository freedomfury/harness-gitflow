from typing import Literal, cast

ResponseDTORollbackResponseDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_ROLLBACK_RESPONSE_DTO_STATUS_VALUES: set[ResponseDTORollbackResponseDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_rollback_response_dto_status(value: str) -> ResponseDTORollbackResponseDTOStatus:
    if value in RESPONSE_DTO_ROLLBACK_RESPONSE_DTO_STATUS_VALUES:
        return cast(ResponseDTORollbackResponseDTOStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_ROLLBACK_RESPONSE_DTO_STATUS_VALUES!r}")
