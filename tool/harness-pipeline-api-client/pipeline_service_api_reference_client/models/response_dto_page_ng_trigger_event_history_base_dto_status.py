from typing import Literal, cast

ResponseDTOPageNGTriggerEventHistoryBaseDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_PAGE_NG_TRIGGER_EVENT_HISTORY_BASE_DTO_STATUS_VALUES: set[
    ResponseDTOPageNGTriggerEventHistoryBaseDTOStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_page_ng_trigger_event_history_base_dto_status(
    value: str,
) -> ResponseDTOPageNGTriggerEventHistoryBaseDTOStatus:
    if value in RESPONSE_DTO_PAGE_NG_TRIGGER_EVENT_HISTORY_BASE_DTO_STATUS_VALUES:
        return cast(ResponseDTOPageNGTriggerEventHistoryBaseDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_PAGE_NG_TRIGGER_EVENT_HISTORY_BASE_DTO_STATUS_VALUES!r}"
    )
