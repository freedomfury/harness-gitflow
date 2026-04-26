from typing import Literal, cast

SortOrderOrderType = Literal["ASC", "DESC"]

SORT_ORDER_ORDER_TYPE_VALUES: set[SortOrderOrderType] = {
    "ASC",
    "DESC",
}


def check_sort_order_order_type(value: str) -> SortOrderOrderType:
    if value in SORT_ORDER_ORDER_TYPE_VALUES:
        return cast(SortOrderOrderType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SORT_ORDER_ORDER_TYPE_VALUES!r}")
