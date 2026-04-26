from typing import Literal, cast

ResponseDTOSecretValidationResultStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SECRET_VALIDATION_RESULT_STATUS_VALUES: set[ResponseDTOSecretValidationResultStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_secret_validation_result_status(value: str) -> ResponseDTOSecretValidationResultStatus:
    if value in RESPONSE_DTO_SECRET_VALIDATION_RESULT_STATUS_VALUES:
        return cast(ResponseDTOSecretValidationResultStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SECRET_VALIDATION_RESULT_STATUS_VALUES!r}"
    )
