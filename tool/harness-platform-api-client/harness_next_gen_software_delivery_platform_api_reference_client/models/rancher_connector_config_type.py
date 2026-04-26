from typing import Literal, cast

RancherConnectorConfigType = Literal["ManualConfig"]

RANCHER_CONNECTOR_CONFIG_TYPE_VALUES: set[RancherConnectorConfigType] = {
    "ManualConfig",
}


def check_rancher_connector_config_type(value: str) -> RancherConnectorConfigType:
    if value in RANCHER_CONNECTOR_CONFIG_TYPE_VALUES:
        return cast(RancherConnectorConfigType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {RANCHER_CONNECTOR_CONFIG_TYPE_VALUES!r}")
