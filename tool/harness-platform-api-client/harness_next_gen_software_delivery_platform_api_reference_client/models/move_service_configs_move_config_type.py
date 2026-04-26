from typing import Literal, cast

MoveServiceConfigsMoveConfigType = Literal["INLINE_TO_REMOTE", "REMOTE_TO_INLINE"]

MOVE_SERVICE_CONFIGS_MOVE_CONFIG_TYPE_VALUES: set[MoveServiceConfigsMoveConfigType] = {
    "INLINE_TO_REMOTE",
    "REMOTE_TO_INLINE",
}


def check_move_service_configs_move_config_type(value: str) -> MoveServiceConfigsMoveConfigType:
    if value in MOVE_SERVICE_CONFIGS_MOVE_CONFIG_TYPE_VALUES:
        return cast(MoveServiceConfigsMoveConfigType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MOVE_SERVICE_CONFIGS_MOVE_CONFIG_TYPE_VALUES!r}")
