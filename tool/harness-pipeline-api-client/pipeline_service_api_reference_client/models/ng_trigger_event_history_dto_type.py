from typing import Literal, cast

NGTriggerEventHistoryDTOType = Literal["Artifact", "Manifest", "MultiRegionArtifact", "Scheduled", "Webhook"]

NG_TRIGGER_EVENT_HISTORY_DTO_TYPE_VALUES: set[NGTriggerEventHistoryDTOType] = {
    "Artifact",
    "Manifest",
    "MultiRegionArtifact",
    "Scheduled",
    "Webhook",
}


def check_ng_trigger_event_history_dto_type(value: str) -> NGTriggerEventHistoryDTOType:
    if value in NG_TRIGGER_EVENT_HISTORY_DTO_TYPE_VALUES:
        return cast(NGTriggerEventHistoryDTOType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NG_TRIGGER_EVENT_HISTORY_DTO_TYPE_VALUES!r}")
