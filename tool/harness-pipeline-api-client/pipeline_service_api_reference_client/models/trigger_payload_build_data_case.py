from typing import Literal, cast

TriggerPayloadBuildDataCase = Literal["ARTIFACTDATA", "BUILDDATA_NOT_SET", "MANIFESTDATA"]

TRIGGER_PAYLOAD_BUILD_DATA_CASE_VALUES: set[TriggerPayloadBuildDataCase] = {
    "ARTIFACTDATA",
    "BUILDDATA_NOT_SET",
    "MANIFESTDATA",
}


def check_trigger_payload_build_data_case(value: str) -> TriggerPayloadBuildDataCase:
    if value in TRIGGER_PAYLOAD_BUILD_DATA_CASE_VALUES:
        return cast(TriggerPayloadBuildDataCase, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRIGGER_PAYLOAD_BUILD_DATA_CASE_VALUES!r}")
