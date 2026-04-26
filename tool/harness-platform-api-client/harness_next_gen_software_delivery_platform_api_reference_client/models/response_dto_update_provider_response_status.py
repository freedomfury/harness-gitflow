from typing import Literal, cast

ResponseDTOUpdateProviderResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_UPDATE_PROVIDER_RESPONSE_STATUS_VALUES: set[ResponseDTOUpdateProviderResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_update_provider_response_status(value: str) -> ResponseDTOUpdateProviderResponseStatus:
    if value in RESPONSE_DTO_UPDATE_PROVIDER_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOUpdateProviderResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_UPDATE_PROVIDER_RESPONSE_STATUS_VALUES!r}"
    )
