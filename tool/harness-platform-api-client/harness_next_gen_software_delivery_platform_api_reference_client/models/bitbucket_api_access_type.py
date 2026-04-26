from typing import Literal, cast

BitbucketApiAccessType = Literal["AccessToken", "EmailAndApiToken", "OAuth", "UsernameToken"]

BITBUCKET_API_ACCESS_TYPE_VALUES: set[BitbucketApiAccessType] = {
    "AccessToken",
    "EmailAndApiToken",
    "OAuth",
    "UsernameToken",
}


def check_bitbucket_api_access_type(value: str) -> BitbucketApiAccessType:
    if value in BITBUCKET_API_ACCESS_TYPE_VALUES:
        return cast(BitbucketApiAccessType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BITBUCKET_API_ACCESS_TYPE_VALUES!r}")
