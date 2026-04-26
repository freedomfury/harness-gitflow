from typing import Literal, cast

StrategyInfoMetadataCase = Literal["FORMETADATA", "METADATA_NOT_SET"]

STRATEGY_INFO_METADATA_CASE_VALUES: set[StrategyInfoMetadataCase] = {
    "FORMETADATA",
    "METADATA_NOT_SET",
}


def check_strategy_info_metadata_case(value: str) -> StrategyInfoMetadataCase:
    if value in STRATEGY_INFO_METADATA_CASE_VALUES:
        return cast(StrategyInfoMetadataCase, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STRATEGY_INFO_METADATA_CASE_VALUES!r}")
