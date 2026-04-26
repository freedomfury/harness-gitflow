from typing import Literal, cast

OverrideMoveConfigsMoveConfigType = Literal["INLINE_TO_REMOTE", "REMOTE_TO_INLINE"]

OVERRIDE_MOVE_CONFIGS_MOVE_CONFIG_TYPE_VALUES: set[OverrideMoveConfigsMoveConfigType] = {
    "INLINE_TO_REMOTE",
    "REMOTE_TO_INLINE",
}


def check_override_move_configs_move_config_type(value: str) -> OverrideMoveConfigsMoveConfigType:
    if value in OVERRIDE_MOVE_CONFIGS_MOVE_CONFIG_TYPE_VALUES:
        return cast(OverrideMoveConfigsMoveConfigType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OVERRIDE_MOVE_CONFIGS_MOVE_CONFIG_TYPE_VALUES!r}")
