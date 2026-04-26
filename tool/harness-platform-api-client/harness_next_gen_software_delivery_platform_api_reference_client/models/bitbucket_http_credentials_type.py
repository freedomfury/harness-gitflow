from typing import Literal, cast

BitbucketHttpCredentialsType = Literal["UsernamePassword"]

BITBUCKET_HTTP_CREDENTIALS_TYPE_VALUES: set[BitbucketHttpCredentialsType] = {
    "UsernamePassword",
}


def check_bitbucket_http_credentials_type(value: str) -> BitbucketHttpCredentialsType:
    if value in BITBUCKET_HTTP_CREDENTIALS_TYPE_VALUES:
        return cast(BitbucketHttpCredentialsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BITBUCKET_HTTP_CREDENTIALS_TYPE_VALUES!r}")
