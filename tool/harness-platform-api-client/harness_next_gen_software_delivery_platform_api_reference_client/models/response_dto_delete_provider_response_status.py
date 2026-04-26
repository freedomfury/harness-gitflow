from typing import Literal, cast

ResponseDTODeleteProviderResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_DELETE_PROVIDER_RESPONSE_STATUS_VALUES: set[ResponseDTODeleteProviderResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_delete_provider_response_status(value: str) -> ResponseDTODeleteProviderResponseStatus:
    if value in RESPONSE_DTO_DELETE_PROVIDER_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTODeleteProviderResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_DELETE_PROVIDER_RESPONSE_STATUS_VALUES!r}"
    )
