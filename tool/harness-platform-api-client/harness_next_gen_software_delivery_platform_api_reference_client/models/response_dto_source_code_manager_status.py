from typing import Literal, cast

ResponseDTOSourceCodeManagerStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SOURCE_CODE_MANAGER_STATUS_VALUES: set[ResponseDTOSourceCodeManagerStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_source_code_manager_status(value: str) -> ResponseDTOSourceCodeManagerStatus:
    if value in RESPONSE_DTO_SOURCE_CODE_MANAGER_STATUS_VALUES:
        return cast(ResponseDTOSourceCodeManagerStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SOURCE_CODE_MANAGER_STATUS_VALUES!r}")
