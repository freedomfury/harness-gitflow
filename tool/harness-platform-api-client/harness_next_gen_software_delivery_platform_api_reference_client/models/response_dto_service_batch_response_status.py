from typing import Literal, cast

ResponseDTOServiceBatchResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SERVICE_BATCH_RESPONSE_STATUS_VALUES: set[ResponseDTOServiceBatchResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_service_batch_response_status(value: str) -> ResponseDTOServiceBatchResponseStatus:
    if value in RESPONSE_DTO_SERVICE_BATCH_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOServiceBatchResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SERVICE_BATCH_RESPONSE_STATUS_VALUES!r}"
    )
