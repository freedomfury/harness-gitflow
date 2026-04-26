from typing import Literal, cast

ListAggregatedKeysSchemesItem = Literal["PGP", "SSH"]

LIST_AGGREGATED_KEYS_SCHEMES_ITEM_VALUES: set[ListAggregatedKeysSchemesItem] = {
    "PGP",
    "SSH",
}


def check_list_aggregated_keys_schemes_item(value: str) -> ListAggregatedKeysSchemesItem:
    if value in LIST_AGGREGATED_KEYS_SCHEMES_ITEM_VALUES:
        return cast(ListAggregatedKeysSchemesItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_AGGREGATED_KEYS_SCHEMES_ITEM_VALUES!r}")
