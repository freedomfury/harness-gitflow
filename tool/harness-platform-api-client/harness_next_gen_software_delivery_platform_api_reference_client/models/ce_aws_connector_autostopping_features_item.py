from typing import Literal, cast

CEAwsConnectorAutostoppingFeaturesItem = Literal[
    "ALB", "ASG", "AZURE_APP_GATEWAY", "AZURE_VM", "EC2", "ECS", "GCP_INSTANCE_GROUP", "GCP_VM", "PROXY", "RDS", "SPOT"
]

CE_AWS_CONNECTOR_AUTOSTOPPING_FEATURES_ITEM_VALUES: set[CEAwsConnectorAutostoppingFeaturesItem] = {
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


def check_ce_aws_connector_autostopping_features_item(value: str) -> CEAwsConnectorAutostoppingFeaturesItem:
    if value in CE_AWS_CONNECTOR_AUTOSTOPPING_FEATURES_ITEM_VALUES:
        return cast(CEAwsConnectorAutostoppingFeaturesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CE_AWS_CONNECTOR_AUTOSTOPPING_FEATURES_ITEM_VALUES!r}"
    )
