from typing import Literal, cast

GetAggregatedApiKeyApiKeyType = Literal["PGP_KEY", "SERVICE_ACCOUNT", "SSH_KEY", "USER"]

GET_AGGREGATED_API_KEY_API_KEY_TYPE_VALUES: set[GetAggregatedApiKeyApiKeyType] = {
    "PGP_KEY",
    "SERVICE_ACCOUNT",
    "SSH_KEY",
    "USER",
}


def check_get_aggregated_api_key_api_key_type(value: str) -> GetAggregatedApiKeyApiKeyType:
    if value in GET_AGGREGATED_API_KEY_API_KEY_TYPE_VALUES:
        return cast(GetAggregatedApiKeyApiKeyType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_AGGREGATED_API_KEY_API_KEY_TYPE_VALUES!r}")
