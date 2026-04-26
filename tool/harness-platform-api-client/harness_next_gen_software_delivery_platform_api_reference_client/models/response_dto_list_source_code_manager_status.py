from typing import Literal, cast

ResponseDTOListSourceCodeManagerStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LIST_SOURCE_CODE_MANAGER_STATUS_VALUES: set[ResponseDTOListSourceCodeManagerStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_list_source_code_manager_status(value: str) -> ResponseDTOListSourceCodeManagerStatus:
    if value in RESPONSE_DTO_LIST_SOURCE_CODE_MANAGER_STATUS_VALUES:
        return cast(ResponseDTOListSourceCodeManagerStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LIST_SOURCE_CODE_MANAGER_STATUS_VALUES!r}"
    )
