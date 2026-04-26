from typing import Literal, cast

CEAzureConnectorAutostoppingFeaturesItem = Literal[
    "ALB", "ASG", "AZURE_APP_GATEWAY", "AZURE_VM", "EC2", "ECS", "GCP_INSTANCE_GROUP", "GCP_VM", "PROXY", "RDS", "SPOT"
]

CE_AZURE_CONNECTOR_AUTOSTOPPING_FEATURES_ITEM_VALUES: set[CEAzureConnectorAutostoppingFeaturesItem] = {
    "ALB",
    "ASG",
    "AZURE_APP_GATEWAY",
    "AZURE_VM",
    "EC2",
    "ECS",
    "GCP_INSTANCE_GROUP",
    "GCP_VM",
    "PROXY",
    "RDS",
    "SPOT",
}


def check_ce_azure_connector_autostopping_features_item(value: str) -> CEAzureConnectorAutostoppingFeaturesItem:
    if value in CE_AZURE_CONNECTOR_AUTOSTOPPING_FEATURES_ITEM_VALUES:
        return cast(CEAzureConnectorAutostoppingFeaturesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CE_AZURE_CONNECTOR_AUTOSTOPPING_FEATURES_ITEM_VALUES!r}"
    )
