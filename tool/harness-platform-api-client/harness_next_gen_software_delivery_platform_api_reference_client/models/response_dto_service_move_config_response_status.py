from typing import Literal, cast

ResponseDTOServiceMoveConfigResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_SERVICE_MOVE_CONFIG_RESPONSE_STATUS_VALUES: set[ResponseDTOServiceMoveConfigResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_service_move_config_response_status(value: str) -> ResponseDTOServiceMoveConfigResponseStatus:
    if value in RESPONSE_DTO_SERVICE_MOVE_CONFIG_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOServiceMoveConfigResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_SERVICE_MOVE_CONFIG_RESPONSE_STATUS_VALUES!r}"
    )
