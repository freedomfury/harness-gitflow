from typing import Literal, cast

FilterFilterVisibility = Literal["EveryOne", "OnlyCreator"]

FILTER_FILTER_VISIBILITY_VALUES: set[FilterFilterVisibility] = {
    "EveryOne",
    "OnlyCreator",
}


def check_filter_filter_visibility(value: str) -> FilterFilterVisibility:
    if value in FILTER_FILTER_VISIBILITY_VALUES:
        return cast(FilterFilterVisibility, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {FILTER_FILTER_VISIBILITY_VALUES!r}")
