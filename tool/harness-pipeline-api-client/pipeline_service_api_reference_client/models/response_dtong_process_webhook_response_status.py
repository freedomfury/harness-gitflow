from typing import Literal, cast

ResponseDTONGProcessWebhookResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTONG_PROCESS_WEBHOOK_RESPONSE_STATUS_VALUES: set[ResponseDTONGProcessWebhookResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dtong_process_webhook_response_status(value: str) -> ResponseDTONGProcessWebhookResponseStatus:
    if value in RESPONSE_DTONG_PROCESS_WEBHOOK_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTONGProcessWebhookResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTONG_PROCESS_WEBHOOK_RESPONSE_STATUS_VALUES!r}"
    )
