from typing import Literal, cast

FeatureSetEnumType = Literal["CLOSED", "ENUM_TYPE_UNKNOWN", "OPEN"]

FEATURE_SET_ENUM_TYPE_VALUES: set[FeatureSetEnumType] = {
    "CLOSED",
    "ENUM_TYPE_UNKNOWN",
    "OPEN",
}


def check_feature_set_enum_type(value: str) -> FeatureSetEnumType:
    if value in FEATURE_SET_ENUM_TYPE_VALUES:
        return cast(FeatureSetEnumType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FEATURE_SET_ENUM_TYPE_VALUES!r}")
