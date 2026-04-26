from typing import Literal, cast

FeatureSetFieldPresence = Literal["EXPLICIT", "FIELD_PRESENCE_UNKNOWN", "IMPLICIT", "LEGACY_REQUIRED"]

FEATURE_SET_FIELD_PRESENCE_VALUES: set[FeatureSetFieldPresence] = {
    "EXPLICIT",
    "FIELD_PRESENCE_UNKNOWN",
    "IMPLICIT",
    "LEGACY_REQUIRED",
}


def check_feature_set_field_presence(value: str) -> FeatureSetFieldPresence:
    if value in FEATURE_SET_FIELD_PRESENCE_VALUES:
        return cast(FeatureSetFieldPresence, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FEATURE_SET_FIELD_PRESENCE_VALUES!r}")
