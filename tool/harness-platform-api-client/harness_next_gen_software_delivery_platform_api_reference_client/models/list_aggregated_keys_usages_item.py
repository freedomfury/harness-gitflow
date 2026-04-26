from typing import Literal, cast

ListAggregatedKeysUsagesItem = Literal["AUTH", "CERTIFY", "ENCRYPT", "SIGN"]

LIST_AGGREGATED_KEYS_USAGES_ITEM_VALUES: set[ListAggregatedKeysUsagesItem] = {
    "AUTH",
    "CERTIFY",
    "ENCRYPT",
    "SIGN",
}


def check_list_aggregated_keys_usages_item(value: str) -> ListAggregatedKeysUsagesItem:
    if value in LIST_AGGREGATED_KEYS_USAGES_ITEM_VALUES:
        return cast(ListAggregatedKeysUsagesItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_AGGREGATED_KEYS_USAGES_ITEM_VALUES!r}")
