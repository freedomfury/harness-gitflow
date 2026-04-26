from typing import Literal, cast

ResponseDTOPageNGTriggerEventsApiResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_NG_TRIGGER_EVENTS_API_RESPONSE_STATUS_VALUES: set[ResponseDTOPageNGTriggerEventsApiResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_ng_trigger_events_api_response_status(
    value: str,
) -> ResponseDTOPageNGTriggerEventsApiResponseStatus:
    if value in RESPONSE_DTO_PAGE_NG_TRIGGER_EVENTS_API_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOPageNGTriggerEventsApiResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_NG_TRIGGER_EVENTS_API_RESPONSE_STATUS_VALUES!r}"
    )
