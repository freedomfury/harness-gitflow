from typing import Literal, cast

FeatureSetOrBuilderRepeatedFieldEncoding = Literal["EXPANDED", "PACKED", "REPEATED_FIELD_ENCODING_UNKNOWN"]

FEATURE_SET_OR_BUILDER_REPEATED_FIELD_ENCODING_VALUES: set[FeatureSetOrBuilderRepeatedFieldEncoding] = {
    "EXPANDED",
    "PACKED",
    "REPEATED_FIELD_ENCODING_UNKNOWN",
}


def check_feature_set_or_builder_repeated_field_encoding(value: str) -> FeatureSetOrBuilderRepeatedFieldEncoding:
    if value in FEATURE_SET_OR_BUILDER_REPEATED_FIELD_ENCODING_VALUES:
        return cast(FeatureSetOrBuilderRepeatedFieldEncoding, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {FEATURE_SET_OR_BUILDER_REPEATED_FIELD_ENCODING_VALUES!r}"
    )
