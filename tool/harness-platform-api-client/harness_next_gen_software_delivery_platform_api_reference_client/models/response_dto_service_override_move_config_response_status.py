from typing import Literal, cast

ResponseDTOServiceOverrideMoveConfigResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SERVICE_OVERRIDE_MOVE_CONFIG_RESPONSE_STATUS_VALUES: set[
    ResponseDTOServiceOverrideMoveConfigResponseStatus
] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_service_override_move_config_response_status(
    value: str,
) -> ResponseDTOServiceOverrideMoveConfigResponseStatus:
    if value in RESPONSE_DTO_SERVICE_OVERRIDE_MOVE_CONFIG_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOServiceOverrideMoveConfigResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SERVICE_OVERRIDE_MOVE_CONFIG_RESPONSE_STATUS_VALUES!r}"
    )
