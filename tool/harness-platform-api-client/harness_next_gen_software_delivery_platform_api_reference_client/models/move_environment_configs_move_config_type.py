from typing import Literal, cast

MoveEnvironmentConfigsMoveConfigType = Literal["INLINE_TO_REMOTE", "REMOTE_TO_INLINE"]

MOVE_ENVIRONMENT_CONFIGS_MOVE_CONFIG_TYPE_VALUES: set[MoveEnvironmentConfigsMoveConfigType] = {
    "INLINE_TO_REMOTE",
    "REMOTE_TO_INLINE",
}


def check_move_environment_configs_move_config_type(value: str) -> MoveEnvironmentConfigsMoveConfigType:
    if value in MOVE_ENVIRONMENT_CONFIGS_MOVE_CONFIG_TYPE_VALUES:
        return cast(MoveEnvironmentConfigsMoveConfigType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MOVE_ENVIRONMENT_CONFIGS_MOVE_CONFIG_TYPE_VALUES!r}")
