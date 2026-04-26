from typing import Literal, cast

TriggerPayloadType = Literal["ARTIFACT", "CUSTOM", "GIT", "MANIFEST", "SCHEDULED", "UNRECOGNIZED", "WEBHOOK"]

TRIGGER_PAYLOAD_TYPE_VALUES: set[TriggerPayloadType] = {
    "ARTIFACT",
    "CUSTOM",
    "GIT",
    "MANIFEST",
    "SCHEDULED",
    "UNRECOGNIZED",
    "WEBHOOK",
}


def check_trigger_payload_type(value: str) -> TriggerPayloadType:
    if value in TRIGGER_PAYLOAD_TYPE_VALUES:
        return cast(TriggerPayloadType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRIGGER_PAYLOAD_TYPE_VALUES!r}")
