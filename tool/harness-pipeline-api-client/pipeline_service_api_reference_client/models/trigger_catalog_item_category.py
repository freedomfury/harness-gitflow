from typing import Literal, cast

TriggerCatalogItemCategory = Literal["Artifact", "Manifest", "MultiRegionArtifact", "Scheduled", "Webhook"]

TRIGGER_CATALOG_ITEM_CATEGORY_VALUES: set[TriggerCatalogItemCategory] = {
    "Artifact",
    "Manifest",
    "MultiRegionArtifact",
    "Scheduled",
    "Webhook",
}


def check_trigger_catalog_item_category(value: str) -> TriggerCatalogItemCategory:
    if value in TRIGGER_CATALOG_ITEM_CATEGORY_VALUES:
        return cast(TriggerCatalogItemCategory, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRIGGER_CATALOG_ITEM_CATEGORY_VALUES!r}")
