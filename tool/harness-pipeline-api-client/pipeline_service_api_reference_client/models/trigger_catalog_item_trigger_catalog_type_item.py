from typing import Literal, cast

TriggerCatalogItemTriggerCatalogTypeItem = Literal[
    "Acr",
    "AmazonMachineImage",
    "AmazonS3",
    "ArtifactoryRegistry",
    "AzureArtifacts",
    "AzureRepo",
    "Bamboo",
    "Bitbucket",
    "Cron",
    "Custom",
    "CustomArtifact",
    "DockerRegistry",
    "Ecr",
    "EventRelay",
    "GceImage",
    "Gcr",
    "Github",
    "GithubPackageRegistry",
    "Gitlab",
    "GoogleArtifactRegistry",
    "GoogleCloudStorage",
    "Harness",
    "HarnessArtifactRegistry",
    "HelmChart",
    "Jenkins",
    "Nexus2Registry",
    "Nexus3Registry",
]

TRIGGER_CATALOG_ITEM_TRIGGER_CATALOG_TYPE_ITEM_VALUES: set[TriggerCatalogItemTriggerCatalogTypeItem] = {
    "Acr",
    "AmazonMachineImage",
    "AmazonS3",
    "ArtifactoryRegistry",
    "AzureArtifacts",
    "AzureRepo",
    "Bamboo",
    "Bitbucket",
    "Cron",
    "Custom",
    "CustomArtifact",
    "DockerRegistry",
    "Ecr",
    "EventRelay",
    "GceImage",
    "Gcr",
    "Github",
    "GithubPackageRegistry",
    "Gitlab",
    "GoogleArtifactRegistry",
    "GoogleCloudStorage",
    "Harness",
    "HarnessArtifactRegistry",
    "HelmChart",
    "Jenkins",
    "Nexus2Registry",
    "Nexus3Registry",
}


def check_trigger_catalog_item_trigger_catalog_type_item(value: str) -> TriggerCatalogItemTriggerCatalogTypeItem:
    if value in TRIGGER_CATALOG_ITEM_TRIGGER_CATALOG_TYPE_ITEM_VALUES:
        return cast(TriggerCatalogItemTriggerCatalogTypeItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRIGGER_CATALOG_ITEM_TRIGGER_CATALOG_TYPE_ITEM_VALUES!r}"
    )
