from typing import Literal, cast

NGTriggerResponseType = Literal["Artifact", "Manifest", "MultiRegionArtifact", "Scheduled", "Webhook"]

NG_TRIGGER_RESPONSE_TYPE_VALUES: set[NGTriggerResponseType] = {
    "Artifact",
    "Manifest",
    "MultiRegionArtifact",
    "Scheduled",
    "Webhook",
}


def check_ng_trigger_response_type(value: str) -> NGTriggerResponseType:
    if value in NG_TRIGGER_RESPONSE_TYPE_VALUES:
        return cast(NGTriggerResponseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NG_TRIGGER_RESPONSE_TYPE_VALUES!r}")
