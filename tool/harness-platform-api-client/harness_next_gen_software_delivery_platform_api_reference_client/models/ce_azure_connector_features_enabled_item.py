from typing import Literal, cast

CEAzureConnectorFeaturesEnabledItem = Literal[
    "BILLING", "CLUSTER_ORCHESTRATOR", "COMMITMENT_ORCHESTRATOR", "GOVERNANCE", "OPTIMIZATION", "VISIBILITY"
]

CE_AZURE_CONNECTOR_FEATURES_ENABLED_ITEM_VALUES: set[CEAzureConnectorFeaturesEnabledItem] = {
    "BILLING",
    "CLUSTER_ORCHESTRATOR",
    "COMMITMENT_ORCHESTRATOR",
    "GOVERNANCE",
    "OPTIMIZATION",
    "VISIBILITY",
}


def check_ce_azure_connector_features_enabled_item(value: str) -> CEAzureConnectorFeaturesEnabledItem:
    if value in CE_AZURE_CONNECTOR_FEATURES_ENABLED_ITEM_VALUES:
        return cast(CEAzureConnectorFeaturesEnabledItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CE_AZURE_CONNECTOR_FEATURES_ENABLED_ITEM_VALUES!r}")
