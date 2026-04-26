from typing import Literal, cast

ResponseDTOBulkInputSetsAPIResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_BULK_INPUT_SETS_API_RESPONSE_STATUS_VALUES: set[ResponseDTOBulkInputSetsAPIResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_bulk_input_sets_api_response_status(value: str) -> ResponseDTOBulkInputSetsAPIResponseStatus:
    if value in RESPONSE_DTO_BULK_INPUT_SETS_API_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOBulkInputSetsAPIResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_BULK_INPUT_SETS_API_RESPONSE_STATUS_VALUES!r}"
    )
