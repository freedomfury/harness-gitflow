from typing import Literal, cast

StrategyMetadataOrBuilderMetadataCase = Literal["FORMETADATA", "MATRIXMETADATA", "METADATA_NOT_SET"]

STRATEGY_METADATA_OR_BUILDER_METADATA_CASE_VALUES: set[StrategyMetadataOrBuilderMetadataCase] = {
    "FORMETADATA",
    "MATRIXMETADATA",
    "METADATA_NOT_SET",
}


def check_strategy_metadata_or_builder_metadata_case(value: str) -> StrategyMetadataOrBuilderMetadataCase:
    if value in STRATEGY_METADATA_OR_BUILDER_METADATA_CASE_VALUES:
        return cast(StrategyMetadataOrBuilderMetadataCase, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {STRATEGY_METADATA_OR_BUILDER_METADATA_CASE_VALUES!r}"
    )
