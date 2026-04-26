from typing import Literal, cast

ResponseDTOPollingInfoForTriggersStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_POLLING_INFO_FOR_TRIGGERS_STATUS_VALUES: set[ResponseDTOPollingInfoForTriggersStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_polling_info_for_triggers_status(value: str) -> ResponseDTOPollingInfoForTriggersStatus:
    if value in RESPONSE_DTO_POLLING_INFO_FOR_TRIGGERS_STATUS_VALUES:
        return cast(ResponseDTOPollingInfoForTriggersStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_POLLING_INFO_FOR_TRIGGERS_STATUS_VALUES!r}"
    )
