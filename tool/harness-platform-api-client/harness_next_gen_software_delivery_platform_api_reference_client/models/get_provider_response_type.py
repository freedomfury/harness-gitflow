from typing import Literal, cast

GetProviderResponseType = Literal["BITBUCKET_SERVER", "GITHUB_ENTERPRISE", "GITLAB_ON_PREM"]

GET_PROVIDER_RESPONSE_TYPE_VALUES: set[GetProviderResponseType] = {
    "BITBUCKET_SERVER",
    "GITHUB_ENTERPRISE",
    "GITLAB_ON_PREM",
}


def check_get_provider_response_type(value: str) -> GetProviderResponseType:
    if value in GET_PROVIDER_RESPONSE_TYPE_VALUES:
        return cast(GetProviderResponseType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GET_PROVIDER_RESPONSE_TYPE_VALUES!r}")
