from typing import Literal, cast

GithubApiAccessType = Literal["GithubApp", "OAuth", "Token"]

GITHUB_API_ACCESS_TYPE_VALUES: set[GithubApiAccessType] = {
    "GithubApp",
    "OAuth",
    "Token",
}


def check_github_api_access_type(value: str) -> GithubApiAccessType:
    if value in GITHUB_API_ACCESS_TYPE_VALUES:
        return cast(GithubApiAccessType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GITHUB_API_ACCESS_TYPE_VALUES!r}")
