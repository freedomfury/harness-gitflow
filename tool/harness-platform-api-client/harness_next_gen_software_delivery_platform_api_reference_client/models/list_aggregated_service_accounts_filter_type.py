from typing import Literal, cast

ListAggregatedServiceAccountsFilterType = Literal[
    "EXCLUDE_INHERITED_SERVICE_ACCOUNTS", "INCLUDE_CHILD_SCOPE_SERVICE_ACCOUNTS", "INCLUDE_INHERITED_SERVICE_ACCOUNTS"
]

LIST_AGGREGATED_SERVICE_ACCOUNTS_FILTER_TYPE_VALUES: set[ListAggregatedServiceAccountsFilterType] = {
    "EXCLUDE_INHERITED_SERVICE_ACCOUNTS",
    "INCLUDE_CHILD_SCOPE_SERVICE_ACCOUNTS",
    "INCLUDE_INHERITED_SERVICE_ACCOUNTS",
}


def check_list_aggregated_service_accounts_filter_type(value: str) -> ListAggregatedServiceAccountsFilterType:
    if value in LIST_AGGREGATED_SERVICE_ACCOUNTS_FILTER_TYPE_VALUES:
        return cast(ListAggregatedServiceAccountsFilterType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {LIST_AGGREGATED_SERVICE_ACCOUNTS_FILTER_TYPE_VALUES!r}"
    )
