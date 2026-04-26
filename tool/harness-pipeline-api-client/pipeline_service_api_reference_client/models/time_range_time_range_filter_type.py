from typing import Literal, cast

TimeRangeTimeRangeFilterType = Literal[
    "LAST_12_MONTHS",
    "LAST_30_DAYS",
    "LAST_3_MONTHS",
    "LAST_6_MONTHS",
    "LAST_7_DAYS",
    "LAST_MONTH",
    "LAST_QUARTER",
    "LAST_YEAR",
    "THIS_MONTH",
    "THIS_QUARTER",
    "THIS_YEAR",
]

TIME_RANGE_TIME_RANGE_FILTER_TYPE_VALUES: set[TimeRangeTimeRangeFilterType] = {
    "LAST_12_MONTHS",
    "LAST_30_DAYS",
    "LAST_3_MONTHS",
    "LAST_6_MONTHS",
    "LAST_7_DAYS",
    "LAST_MONTH",
    "LAST_QUARTER",
    "LAST_YEAR",
    "THIS_MONTH",
    "THIS_QUARTER",
    "THIS_YEAR",
}


def check_time_range_time_range_filter_type(value: str) -> TimeRangeTimeRangeFilterType:
    if value in TIME_RANGE_TIME_RANGE_FILTER_TYPE_VALUES:
        return cast(TimeRangeTimeRangeFilterType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {TIME_RANGE_TIME_RANGE_FILTER_TYPE_VALUES!r}")
