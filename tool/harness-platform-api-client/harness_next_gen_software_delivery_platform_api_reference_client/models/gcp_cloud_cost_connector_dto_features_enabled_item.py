from typing import Literal, cast

GcpCloudCostConnectorDTOFeaturesEnabledItem = Literal[
    "BILLING", "CLUSTER_ORCHESTRATOR", "COMMITMENT_ORCHESTRATOR", "GOVERNANCE", "OPTIMIZATION", "VISIBILITY"
]

GCP_CLOUD_COST_CONNECTOR_DTO_FEATURES_ENABLED_ITEM_VALUES: set[GcpCloudCostConnectorDTOFeaturesEnabledItem] = {
    "BILLING",
    "CLUSTER_ORCHESTRATOR",
    "COMMITMENT_ORCHESTRATOR",
    "GOVERNANCE",
    "OPTIMIZATION",
    "VISIBILITY",
}


def check_gcp_cloud_cost_connector_dto_features_enabled_item(value: str) -> GcpCloudCostConnectorDTOFeaturesEnabledItem:
    if value in GCP_CLOUD_COST_CONNECTOR_DTO_FEATURES_ENABLED_ITEM_VALUES:
        return cast(GcpCloudCostConnectorDTOFeaturesEnabledItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {GCP_CLOUD_COST_CONNECTOR_DTO_FEATURES_ENABLED_ITEM_VALUES!r}"
    )
