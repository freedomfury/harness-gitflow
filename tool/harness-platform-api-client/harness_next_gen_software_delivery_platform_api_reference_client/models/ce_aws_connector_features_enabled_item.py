from typing import Literal, cast

CEAwsConnectorFeaturesEnabledItem = Literal[
    "BILLING", "CLUSTER_ORCHESTRATOR", "COMMITMENT_ORCHESTRATOR", "GOVERNANCE", "OPTIMIZATION", "VISIBILITY"
]

CE_AWS_CONNECTOR_FEATURES_ENABLED_ITEM_VALUES: set[CEAwsConnectorFeaturesEnabledItem] = {
    "BILLING",
    "CLUSTER_ORCHESTRATOR",
    "COMMITMENT_ORCHESTRATOR",
    "GOVERNANCE",
    "OPTIMIZATION",
    "VISIBILITY",
}


def check_ce_aws_connector_features_enabled_item(value: str) -> CEAwsConnectorFeaturesEnabledItem:
    if value in CE_AWS_CONNECTOR_FEATURES_ENABLED_ITEM_VALUES:
        return cast(CEAwsConnectorFeaturesEnabledItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CE_AWS_CONNECTOR_FEATURES_ENABLED_ITEM_VALUES!r}")
