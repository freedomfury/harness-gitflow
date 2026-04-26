from typing import Literal, cast

FeatureSetRepeatedFieldEncoding = Literal["EXPANDED", "PACKED", "REPEATED_FIELD_ENCODING_UNKNOWN"]

FEATURE_SET_REPEATED_FIELD_ENCODING_VALUES: set[FeatureSetRepeatedFieldEncoding] = {
    "EXPANDED",
    "PACKED",
    "REPEATED_FIELD_ENCODING_UNKNOWN",
}


def check_feature_set_repeated_field_encoding(value: str) -> FeatureSetRepeatedFieldEncoding:
    if value in FEATURE_SET_REPEATED_FIELD_ENCODING_VALUES:
        return cast(FeatureSetRepeatedFieldEncoding, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FEATURE_SET_REPEATED_FIELD_ENCODING_VALUES!r}")
