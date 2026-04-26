from typing import Literal, cast

ResponseDTOPageNGTriggerEventHistoryDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_NG_TRIGGER_EVENT_HISTORY_DTO_STATUS_VALUES: set[ResponseDTOPageNGTriggerEventHistoryDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_ng_trigger_event_history_dto_status(
    value: str,
) -> ResponseDTOPageNGTriggerEventHistoryDTOStatus:
    if value in RESPONSE_DTO_PAGE_NG_TRIGGER_EVENT_HISTORY_DTO_STATUS_VALUES:
        return cast(ResponseDTOPageNGTriggerEventHistoryDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_NG_TRIGGER_EVENT_HISTORY_DTO_STATUS_VALUES!r}"
    )
