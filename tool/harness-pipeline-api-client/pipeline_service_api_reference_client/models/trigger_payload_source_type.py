from typing import Literal, cast

TriggerPayloadSourceType = Literal[
    "AWS_CODECOMMIT_REPO",
    "AZURE_REPO",
    "BITBUCKET_REPO",
    "CUSTOM_REPO",
    "GITHUB_REPO",
    "GITLAB_REPO",
    "HARNESS_REPO",
    "UNRECOGNIZED",
]

TRIGGER_PAYLOAD_SOURCE_TYPE_VALUES: set[TriggerPayloadSourceType] = {
    "AWS_CODECOMMIT_REPO",
    "AZURE_REPO",
    "BITBUCKET_REPO",
    "CUSTOM_REPO",
    "GITHUB_REPO",
    "GITLAB_REPO",
    "HARNESS_REPO",
    "UNRECOGNIZED",
}


def check_trigger_payload_source_type(value: str) -> TriggerPayloadSourceType:
    if value in TRIGGER_PAYLOAD_SOURCE_TYPE_VALUES:
        return cast(TriggerPayloadSourceType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TRIGGER_PAYLOAD_SOURCE_TYPE_VALUES!r}")
