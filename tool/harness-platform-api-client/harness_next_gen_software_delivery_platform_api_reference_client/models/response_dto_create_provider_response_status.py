from typing import Literal, cast

ResponseDTOCreateProviderResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_CREATE_PROVIDER_RESPONSE_STATUS_VALUES: set[ResponseDTOCreateProviderResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_create_provider_response_status(value: str) -> ResponseDTOCreateProviderResponseStatus:
    if value in RESPONSE_DTO_CREATE_PROVIDER_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOCreateProviderResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_CREATE_PROVIDER_RESPONSE_STATUS_VALUES!r}"
    )
