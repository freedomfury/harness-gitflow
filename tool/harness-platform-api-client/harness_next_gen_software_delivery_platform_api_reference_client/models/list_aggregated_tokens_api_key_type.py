from typing import Literal, cast

ListAggregatedTokensApiKeyType = Literal["PGP_KEY", "SERVICE_ACCOUNT", "SSH_KEY", "USER"]

LIST_AGGREGATED_TOKENS_API_KEY_TYPE_VALUES: set[ListAggregatedTokensApiKeyType] = {
    "PGP_KEY",
    "SERVICE_ACCOUNT",
    "SSH_KEY",
    "USER",
}


def check_list_aggregated_tokens_api_key_type(value: str) -> ListAggregatedTokensApiKeyType:
    if value in LIST_AGGREGATED_TOKENS_API_KEY_TYPE_VALUES:
        return cast(ListAggregatedTokensApiKeyType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_AGGREGATED_TOKENS_API_KEY_TYPE_VALUES!r}")
