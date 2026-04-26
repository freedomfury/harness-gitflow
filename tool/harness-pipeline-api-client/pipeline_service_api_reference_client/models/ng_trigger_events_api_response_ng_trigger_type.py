from typing import Literal, cast

NGTriggerEventsApiResponseNgTriggerType = Literal["Artifact", "Manifest", "MultiRegionArtifact", "Scheduled", "Webhook"]

NG_TRIGGER_EVENTS_API_RESPONSE_NG_TRIGGER_TYPE_VALUES: set[NGTriggerEventsApiResponseNgTriggerType] = {
    "Artifact",
    "Manifest",
    "MultiRegionArtifact",
    "Scheduled",
    "Webhook",
}


def check_ng_trigger_events_api_response_ng_trigger_type(value: str) -> NGTriggerEventsApiResponseNgTriggerType:
    if value in NG_TRIGGER_EVENTS_API_RESPONSE_NG_TRIGGER_TYPE_VALUES:
        return cast(NGTriggerEventsApiResponseNgTriggerType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {NG_TRIGGER_EVENTS_API_RESPONSE_NG_TRIGGER_TYPE_VALUES!r}"
    )
