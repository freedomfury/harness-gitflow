from typing import Literal, cast

ResponseDTONgSmtpStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_NG_SMTP_STATUS_VALUES: set[ResponseDTONgSmtpStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_ng_smtp_status(value: str) -> ResponseDTONgSmtpStatus:
    if value in RESPONSE_DTO_NG_SMTP_STATUS_VALUES:
        return cast(ResponseDTONgSmtpStatus, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_NG_SMTP_STATUS_VALUES!r}")
