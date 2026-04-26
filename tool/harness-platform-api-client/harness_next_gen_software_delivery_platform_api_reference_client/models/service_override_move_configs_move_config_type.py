from typing import Literal, cast

ServiceOverrideMoveConfigsMoveConfigType = Literal["INLINE_TO_REMOTE", "REMOTE_TO_INLINE"]

SERVICE_OVERRIDE_MOVE_CONFIGS_MOVE_CONFIG_TYPE_VALUES: set[ServiceOverrideMoveConfigsMoveConfigType] = {
    "INLINE_TO_REMOTE",
    "REMOTE_TO_INLINE",
}


def check_service_override_move_configs_move_config_type(value: str) -> ServiceOverrideMoveConfigsMoveConfigType:
    if value in SERVICE_OVERRIDE_MOVE_CONFIGS_MOVE_CONFIG_TYPE_VALUES:
        return cast(ServiceOverrideMoveConfigsMoveConfigType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SERVICE_OVERRIDE_MOVE_CONFIGS_MOVE_CONFIG_TYPE_VALUES!r}"
    )
