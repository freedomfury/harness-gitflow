from typing import Literal, cast

ResponseDTOListGetProviderResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LIST_GET_PROVIDER_RESPONSE_STATUS_VALUES: set[ResponseDTOListGetProviderResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_list_get_provider_response_status(value: str) -> ResponseDTOListGetProviderResponseStatus:
    if value in RESPONSE_DTO_LIST_GET_PROVIDER_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOListGetProviderResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LIST_GET_PROVIDER_RESPONSE_STATUS_VALUES!r}"
    )
