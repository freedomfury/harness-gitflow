from typing import Literal, cast

ResponseDTOGetProviderResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_GET_PROVIDER_RESPONSE_STATUS_VALUES: set[ResponseDTOGetProviderResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_get_provider_response_status(value: str) -> ResponseDTOGetProviderResponseStatus:
    if value in RESPONSE_DTO_GET_PROVIDER_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOGetProviderResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_GET_PROVIDER_RESPONSE_STATUS_VALUES!r}")
