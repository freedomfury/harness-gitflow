from typing import Literal, cast

ResponseDTOEnvironmentMoveConfigResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_ENVIRONMENT_MOVE_CONFIG_RESPONSE_STATUS_VALUES: set[ResponseDTOEnvironmentMoveConfigResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_environment_move_config_response_status(
    value: str,
) -> ResponseDTOEnvironmentMoveConfigResponseStatus:
    if value in RESPONSE_DTO_ENVIRONMENT_MOVE_CONFIG_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOEnvironmentMoveConfigResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_ENVIRONMENT_MOVE_CONFIG_RESPONSE_STATUS_VALUES!r}"
    )
