from typing import Literal, cast

FeatureSetOrBuilderJsonFormat = Literal["ALLOW", "JSON_FORMAT_UNKNOWN", "LEGACY_BEST_EFFORT"]

FEATURE_SET_OR_BUILDER_JSON_FORMAT_VALUES: set[FeatureSetOrBuilderJsonFormat] = {
    "ALLOW",
    "JSON_FORMAT_UNKNOWN",
    "LEGACY_BEST_EFFORT",
}


def check_feature_set_or_builder_json_format(value: str) -> FeatureSetOrBuilderJsonFormat:
    if value in FEATURE_SET_OR_BUILDER_JSON_FORMAT_VALUES:
        return cast(FeatureSetOrBuilderJsonFormat, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FEATURE_SET_OR_BUILDER_JSON_FORMAT_VALUES!r}")
