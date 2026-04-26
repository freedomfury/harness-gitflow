from typing import Literal, cast

TriggerEventHistoryUsingFiltersTriggerType = Literal[
    "Artifact", "Manifest", "MultiRegionArtifact", "Scheduled", "Webhook"
]

TRIGGER_EVENT_HISTORY_USING_FILTERS_TRIGGER_TYPE_VALUES: set[TriggerEventHistoryUsingFiltersTriggerType] = {
    "Artifact",
    "Manifest",
    "MultiRegionArtifact",
    "Scheduled",
    "Webhook",
}


def check_trigger_event_history_using_filters_trigger_type(value: str) -> TriggerEventHistoryUsingFiltersTriggerType:
    if value in TRIGGER_EVENT_HISTORY_USING_FILTERS_TRIGGER_TYPE_VALUES:
        return cast(TriggerEventHistoryUsingFiltersTriggerType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {TRIGGER_EVENT_HISTORY_USING_FILTERS_TRIGGER_TYPE_VALUES!r}"
    )
