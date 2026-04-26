from typing import Literal, cast

ResponseDTOListEntityTypeStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LIST_ENTITY_TYPE_STATUS_VALUES: set[ResponseDTOListEntityTypeStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_list_entity_type_status(value: str) -> ResponseDTOListEntityTypeStatus:
    if value in RESPONSE_DTO_LIST_ENTITY_TYPE_STATUS_VALUES:
        return cast(ResponseDTOListEntityTypeStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LIST_ENTITY_TYPE_STATUS_VALUES!r}")
