from typing import Literal, cast

StrategyInfoOrBuilderMetadataCase = Literal["FORMETADATA", "METADATA_NOT_SET"]

STRATEGY_INFO_OR_BUILDER_METADATA_CASE_VALUES: set[StrategyInfoOrBuilderMetadataCase] = {
    "FORMETADATA",
    "METADATA_NOT_SET",
}


def check_strategy_info_or_builder_metadata_case(value: str) -> StrategyInfoOrBuilderMetadataCase:
    if value in STRATEGY_INFO_OR_BUILDER_METADATA_CASE_VALUES:
        return cast(StrategyInfoOrBuilderMetadataCase, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STRATEGY_INFO_OR_BUILDER_METADATA_CASE_VALUES!r}")
