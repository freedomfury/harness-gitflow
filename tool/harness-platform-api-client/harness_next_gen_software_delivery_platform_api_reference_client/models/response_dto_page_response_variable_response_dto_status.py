from typing import Literal, cast

ResponseDTOPageResponseVariableResponseDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_VARIABLE_RESPONSE_DTO_STATUS_VALUES: set[
    ResponseDTOPageResponseVariableResponseDTOStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_variable_response_dto_status(
    value: str,
) -> ResponseDTOPageResponseVariableResponseDTOStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_VARIABLE_RESPONSE_DTO_STATUS_VALUES:
        return cast(ResponseDTOPageResponseVariableResponseDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_VARIABLE_RESPONSE_DTO_STATUS_VALUES!r}"
    )
