from typing import Literal, cast

ResponseDTOValidationResultStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_VALIDATION_RESULT_STATUS_VALUES: set[ResponseDTOValidationResultStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_validation_result_status(value: str) -> ResponseDTOValidationResultStatus:
    if value in RESPONSE_DTO_VALIDATION_RESULT_STATUS_VALUES:
        return cast(ResponseDTOValidationResultStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_VALIDATION_RESULT_STATUS_VALUES!r}")
