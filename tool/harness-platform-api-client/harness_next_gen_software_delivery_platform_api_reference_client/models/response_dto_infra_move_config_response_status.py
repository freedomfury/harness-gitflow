from typing import Literal, cast

ResponseDTOInfraMoveConfigResponseStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_INFRA_MOVE_CONFIG_RESPONSE_STATUS_VALUES: set[ResponseDTOInfraMoveConfigResponseStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_infra_move_config_response_status(value: str) -> ResponseDTOInfraMoveConfigResponseStatus:
    if value in RESPONSE_DTO_INFRA_MOVE_CONFIG_RESPONSE_STATUS_VALUES:
        return cast(ResponseDTOInfraMoveConfigResponseStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_INFRA_MOVE_CONFIG_RESPONSE_STATUS_VALUES!r}"
    )
