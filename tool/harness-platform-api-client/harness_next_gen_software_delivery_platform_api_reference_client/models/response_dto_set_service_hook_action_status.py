from typing import Literal, cast

ResponseDTOSetServiceHookActionStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SET_SERVICE_HOOK_ACTION_STATUS_VALUES: set[ResponseDTOSetServiceHookActionStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_set_service_hook_action_status(value: str) -> ResponseDTOSetServiceHookActionStatus:
    if value in RESPONSE_DTO_SET_SERVICE_HOOK_ACTION_STATUS_VALUES:
        return cast(ResponseDTOSetServiceHookActionStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SET_SERVICE_HOOK_ACTION_STATUS_VALUES!r}"
    )
