from typing import Literal, cast

WebhookAutoRegistrationStatusRegistrationResult = Literal["ERROR", "FAILED", "SUCCESS", "TIMEOUT", "UNAVAILABLE"]

WEBHOOK_AUTO_REGISTRATION_STATUS_REGISTRATION_RESULT_VALUES: set[WebhookAutoRegistrationStatusRegistrationResult] = {
    "ERROR",
    "FAILED",
    "SUCCESS",
    "TIMEOUT",
    "UNAVAILABLE",
}


def check_webhook_auto_registration_status_registration_result(
    value: str,
) -> WebhookAutoRegistrationStatusRegistrationResult:
    if value in WEBHOOK_AUTO_REGISTRATION_STATUS_REGISTRATION_RESULT_VALUES:
        return cast(WebhookAutoRegistrationStatusRegistrationResult, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {WEBHOOK_AUTO_REGISTRATION_STATUS_REGISTRATION_RESULT_VALUES!r}"
    )
