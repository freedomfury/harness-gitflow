from typing import Literal, cast

ResponseDTOListScopeNameStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LIST_SCOPE_NAME_STATUS_VALUES: set[ResponseDTOListScopeNameStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_list_scope_name_status(value: str) -> ResponseDTOListScopeNameStatus:
    if value in RESPONSE_DTO_LIST_SCOPE_NAME_STATUS_VALUES:
        return cast(ResponseDTOListScopeNameStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LIST_SCOPE_NAME_STATUS_VALUES!r}")
