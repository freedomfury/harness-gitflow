from typing import Literal, cast

BitbucketAuthenticationType = Literal["Http", "Ssh"]

BITBUCKET_AUTHENTICATION_TYPE_VALUES: set[BitbucketAuthenticationType] = {
    "Http",
    "Ssh",
}


def check_bitbucket_authentication_type(value: str) -> BitbucketAuthenticationType:
    if value in BITBUCKET_AUTHENTICATION_TYPE_VALUES:
        return cast(BitbucketAuthenticationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BITBUCKET_AUTHENTICATION_TYPE_VALUES!r}")
