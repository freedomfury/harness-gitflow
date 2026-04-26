from typing import Literal, cast

ResponseDTOWebhookEventProcessingDetailsStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_WEBHOOK_EVENT_PROCESSING_DETAILS_STATUS_VALUES: set[ResponseDTOWebhookEventProcessingDetailsStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_webhook_event_processing_details_status(
    value: str,
) -> ResponseDTOWebhookEventProcessingDetailsStatus:
    if value in RESPONSE_DTO_WEBHOOK_EVENT_PROCESSING_DETAILS_STATUS_VALUES:
        return cast(ResponseDTOWebhookEventProcessingDetailsStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_WEBHOOK_EVENT_PROCESSING_DETAILS_STATUS_VALUES!r}"
    )
