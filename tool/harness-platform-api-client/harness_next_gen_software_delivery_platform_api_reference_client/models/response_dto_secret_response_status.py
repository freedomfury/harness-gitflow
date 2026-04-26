from typing import Literal, cast

ResponseDTOSecretResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SECRET_RESPONSE_STATUS_VALUES: set[ResponseDTOSecretResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_secret_response_status(value: str) -> ResponseDTOSecretResponseStatus:
    if value in RESPONSE_DTO_SECRET_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOSecretResponseStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SECRET_RESPONSE_STATUS_VALUES!r}")
