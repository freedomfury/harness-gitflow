from typing import Literal, cast

CEKubernetesClusterConfigDTOFeaturesEnabledItem = Literal[
    "BILLING", "CLUSTER_ORCHESTRATOR", "COMMITMENT_ORCHESTRATOR", "GOVERNANCE", "OPTIMIZATION", "VISIBILITY"
]

CE_KUBERNETES_CLUSTER_CONFIG_DTO_FEATURES_ENABLED_ITEM_VALUES: set[CEKubernetesClusterConfigDTOFeaturesEnabledItem] = {
    "BILLING",
    "CLUSTER_ORCHESTRATOR",
    "COMMITMENT_ORCHESTRATOR",
    "GOVERNANCE",
    "OPTIMIZATION",
    "VISIBILITY",
}


def check_ce_kubernetes_cluster_config_dto_features_enabled_item(
    value: str,
) -> CEKubernetesClusterConfigDTOFeaturesEnabledItem:
    if value in CE_KUBERNETES_CLUSTER_CONFIG_DTO_FEATURES_ENABLED_ITEM_VALUES:
        return cast(CEKubernetesClusterConfigDTOFeaturesEnabledItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {CE_KUBERNETES_CLUSTER_CONFIG_DTO_FEATURES_ENABLED_ITEM_VALUES!r}"
    )
