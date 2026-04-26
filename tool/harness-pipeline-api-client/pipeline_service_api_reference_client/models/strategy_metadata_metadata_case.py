from typing import Literal, cast

StrategyMetadataMetadataCase = Literal["FORMETADATA", "MATRIXMETADATA", "METADATA_NOT_SET"]

STRATEGY_METADATA_METADATA_CASE_VALUES: set[StrategyMetadataMetadataCase] = {
    "FORMETADATA",
    "MATRIXMETADATA",
    "METADATA_NOT_SET",
}


def check_strategy_metadata_metadata_case(value: str) -> StrategyMetadataMetadataCase:
    if value in STRATEGY_METADATA_METADATA_CASE_VALUES:
        return cast(StrategyMetadataMetadataCase, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STRATEGY_METADATA_METADATA_CASE_VALUES!r}")
