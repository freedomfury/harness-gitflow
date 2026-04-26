from typing import Literal, cast

TriggerFilterPropertiesTriggerTypesItem = Literal["Artifact", "Manifest", "MultiRegionArtifact", "Scheduled", "Webhook"]

TRIGGER_FILTER_PROPERTIES_TRIGGER_TYPES_ITEM_VALUES: set[TriggerFilterPropertiesTriggerTypesItem] = {
    "Artifact",
    "Manifest",
    "MultiRegionArtifact",
    "Scheduled",
    "Webhook",
}


def check_trigger_filter_properties_trigger_types_item(value: str) -> TriggerFilterPropertiesTriggerTypesItem:
    if value in TRIGGER_FILTER_PROPERTIES_TRIGGER_TYPES_ITEM_VALUES:
        return cast(TriggerFilterPropertiesTriggerTypesItem, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRIGGER_FILTER_PROPERTIES_TRIGGER_TYPES_ITEM_VALUES!r}"
    )
