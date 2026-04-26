from typing import Literal, cast

FeatureSetOrBuilderFieldPresence = Literal["EXPLICIT", "FIELD_PRESENCE_UNKNOWN", "IMPLICIT", "LEGACY_REQUIRED"]

FEATURE_SET_OR_BUILDER_FIELD_PRESENCE_VALUES: set[FeatureSetOrBuilderFieldPresence] = {
    "EXPLICIT",
    "FIELD_PRESENCE_UNKNOWN",
    "IMPLICIT",
    "LEGACY_REQUIRED",
}


def check_feature_set_or_builder_field_presence(value: str) -> FeatureSetOrBuilderFieldPresence:
    if value in FEATURE_SET_OR_BUILDER_FIELD_PRESENCE_VALUES:
        return cast(FeatureSetOrBuilderFieldPresence, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FEATURE_SET_OR_BUILDER_FIELD_PRESENCE_VALUES!r}")
