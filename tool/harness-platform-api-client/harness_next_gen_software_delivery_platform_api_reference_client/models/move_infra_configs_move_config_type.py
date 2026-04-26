from typing import Literal, cast

MoveInfraConfigsMoveConfigType = Literal["INLINE_TO_REMOTE", "REMOTE_TO_INLINE"]

MOVE_INFRA_CONFIGS_MOVE_CONFIG_TYPE_VALUES: set[MoveInfraConfigsMoveConfigType] = {
    "INLINE_TO_REMOTE",
    "REMOTE_TO_INLINE",
}


def check_move_infra_configs_move_config_type(value: str) -> MoveInfraConfigsMoveConfigType:
    if value in MOVE_INFRA_CONFIGS_MOVE_CONFIG_TYPE_VALUES:
        return cast(MoveInfraConfigsMoveConfigType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {MOVE_INFRA_CONFIGS_MOVE_CONFIG_TYPE_VALUES!r}")
