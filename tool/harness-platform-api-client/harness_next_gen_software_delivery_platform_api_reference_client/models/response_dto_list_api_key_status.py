from typing import Literal, cast

ResponseDTOListApiKeyStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_LIST_API_KEY_STATUS_VALUES: set[ResponseDTOListApiKeyStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_list_api_key_status(value: str) -> ResponseDTOListApiKeyStatus:
    if value in RESPONSE_DTO_LIST_API_KEY_STATUS_VALUES:
        return cast(ResponseDTOListApiKeyStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_LIST_API_KEY_STATUS_VALUES!r}")
