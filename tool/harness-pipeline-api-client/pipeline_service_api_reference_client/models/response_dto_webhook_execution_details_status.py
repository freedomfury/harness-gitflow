from typing import Literal, cast

ResponseDTOWebhookExecutionDetailsStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_WEBHOOK_EXECUTION_DETAILS_STATUS_VALUES: set[ResponseDTOWebhookExecutionDetailsStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_webhook_execution_details_status(value: str) -> ResponseDTOWebhookExecutionDetailsStatus:
    if value in RESPONSE_DTO_WEBHOOK_EXECUTION_DETAILS_STATUS_VALUES:
        return cast(ResponseDTOWebhookExecutionDetailsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_WEBHOOK_EXECUTION_DETAILS_STATUS_VALUES!r}"
    )
