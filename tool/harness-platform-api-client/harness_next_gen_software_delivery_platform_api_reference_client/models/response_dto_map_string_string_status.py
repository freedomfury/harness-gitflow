from typing import Literal, cast

ResponseDTOMapStringStringStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_MAP_STRING_STRING_STATUS_VALUES: set[ResponseDTOMapStringStringStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_map_string_string_status(value: str) -> ResponseDTOMapStringStringStatus:
    if value in RESPONSE_DTO_MAP_STRING_STRING_STATUS_VALUES:
        return cast(ResponseDTOMapStringStringStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_MAP_STRING_STRING_STATUS_VALUES!r}")
