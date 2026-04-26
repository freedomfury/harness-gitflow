from typing import Literal, cast

GcpCloudCostConnectorDTOAutostoppingFeaturesItem = Literal[
    "ALB", "ASG", "AZURE_APP_GATEWAY", "AZURE_VM", "EC2", "ECS", "GCP_INSTANCE_GROUP", "GCP_VM", "PROXY", "RDS", "SPOT"
]

GCP_CLOUD_COST_CONNECTOR_DTO_AUTOSTOPPING_FEATURES_ITEM_VALUES: set[
    GcpCloudCostConnectorDTOAutostoppingFeaturesItem
] = {
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


def check_gcp_cloud_cost_connector_dto_autostopping_features_item(
    value: str,
) -> GcpCloudCostConnectorDTOAutostoppingFeaturesItem:
    if value in GCP_CLOUD_COST_CONNECTOR_DTO_AUTOSTOPPING_FEATURES_ITEM_VALUES:
        return cast(GcpCloudCostConnectorDTOAutostoppingFeaturesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GCP_CLOUD_COST_CONNECTOR_DTO_AUTOSTOPPING_FEATURES_ITEM_VALUES!r}"
    )
