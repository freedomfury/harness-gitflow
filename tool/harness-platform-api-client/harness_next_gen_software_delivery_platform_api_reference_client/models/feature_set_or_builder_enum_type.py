from typing import Literal, cast

FeatureSetOrBuilderEnumType = Literal["CLOSED", "ENUM_TYPE_UNKNOWN", "OPEN"]

FEATURE_SET_OR_BUILDER_ENUM_TYPE_VALUES: set[FeatureSetOrBuilderEnumType] = {
    "CLOSED",
    "ENUM_TYPE_UNKNOWN",
    "OPEN",
}


def check_feature_set_or_builder_enum_type(value: str) -> FeatureSetOrBuilderEnumType:
    if value in FEATURE_SET_OR_BUILDER_ENUM_TYPE_VALUES:
        return cast(FeatureSetOrBuilderEnumType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FEATURE_SET_OR_BUILDER_ENUM_TYPE_VALUES!r}")
