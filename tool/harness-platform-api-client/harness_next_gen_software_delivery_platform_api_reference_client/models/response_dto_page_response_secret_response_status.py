from typing import Literal, cast

ResponseDTOPageResponseSecretResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_RESPONSE_SECRET_RESPONSE_STATUS_VALUES: set[ResponseDTOPageResponseSecretResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_response_secret_response_status(value: str) -> ResponseDTOPageResponseSecretResponseStatus:
    if value in RESPONSE_DTO_PAGE_RESPONSE_SECRET_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPageResponseSecretResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_RESPONSE_SECRET_RESPONSE_STATUS_VALUES!r}"
    )
