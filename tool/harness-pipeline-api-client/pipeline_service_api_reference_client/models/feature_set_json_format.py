from typing import Literal, cast

FeatureSetJsonFormat = Literal["ALLOW", "JSON_FORMAT_UNKNOWN", "LEGACY_BEST_EFFORT"]

FEATURE_SET_JSON_FORMAT_VALUES: set[FeatureSetJsonFormat] = {
    "ALLOW",
    "JSON_FORMAT_UNKNOWN",
    "LEGACY_BEST_EFFORT",
}


def check_feature_set_json_format(value: str) -> FeatureSetJsonFormat:
    if value in FEATURE_SET_JSON_FORMAT_VALUES:
        return cast(FeatureSetJsonFormat, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FEATURE_SET_JSON_FORMAT_VALUES!r}")
