from typing import Literal, cast

GithubHttpCredentialsType = Literal["Anonymous", "GithubApp", "OAuth", "UsernamePassword", "UsernameToken"]

GITHUB_HTTP_CREDENTIALS_TYPE_VALUES: set[GithubHttpCredentialsType] = {
    "Anonymous",
    "GithubApp",
    "OAuth",
    "UsernamePassword",
    "UsernameToken",
}


def check_github_http_credentials_type(value: str) -> GithubHttpCredentialsType:
    if value in GITHUB_HTTP_CREDENTIALS_TYPE_VALUES:
        return cast(GithubHttpCredentialsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GITHUB_HTTP_CREDENTIALS_TYPE_VALUES!r}")
