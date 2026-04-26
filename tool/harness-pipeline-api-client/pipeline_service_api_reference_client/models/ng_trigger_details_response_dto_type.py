from typing import Literal, cast

NGTriggerDetailsResponseDTOType = Literal["Artifact", "Manifest", "MultiRegionArtifact", "Scheduled", "Webhook"]

NG_TRIGGER_DETAILS_RESPONSE_DTO_TYPE_VALUES: set[NGTriggerDetailsResponseDTOType] = {
    "Artifact",
    "Manifest",
    "MultiRegionArtifact",
    "Scheduled",
    "Webhook",
}


def check_ng_trigger_details_response_dto_type(value: str) -> NGTriggerDetailsResponseDTOType:
    if value in NG_TRIGGER_DETAILS_RESPONSE_DTO_TYPE_VALUES:
        return cast(NGTriggerDetailsResponseDTOType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {NG_TRIGGER_DETAILS_RESPONSE_DTO_TYPE_VALUES!r}")
