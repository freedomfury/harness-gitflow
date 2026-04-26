from typing import Literal, cast

ResponseDTOEnvironmentBatchResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_ENVIRONMENT_BATCH_RESPONSE_STATUS_VALUES: set[ResponseDTOEnvironmentBatchResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_environment_batch_response_status(value: str) -> ResponseDTOEnvironmentBatchResponseStatus:
    if value in RESPONSE_DTO_ENVIRONMENT_BATCH_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOEnvironmentBatchResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_ENVIRONMENT_BATCH_RESPONSE_STATUS_VALUES!r}"
    )
