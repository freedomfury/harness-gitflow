from typing import Literal, cast

ResponseDTOApiKeyStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_API_KEY_STATUS_VALUES: set[ResponseDTOApiKeyStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_api_key_status(value: str) -> ResponseDTOApiKeyStatus:
    if value in RESPONSE_DTO_API_KEY_STATUS_VALUES:
        return cast(ResponseDTOApiKeyStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_API_KEY_STATUS_VALUES!r}")
