from typing import Literal, cast

GithubAuthenticationType = Literal["Http", "Ssh"]

GITHUB_AUTHENTICATION_TYPE_VALUES: set[GithubAuthenticationType] = {
    "Http",
    "Ssh",
}


def check_github_authentication_type(value: str) -> GithubAuthenticationType:
    if value in GITHUB_AUTHENTICATION_TYPE_VALUES:
        return cast(GithubAuthenticationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GITHUB_AUTHENTICATION_TYPE_VALUES!r}")
