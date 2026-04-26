from typing import Literal, cast

GitlabApiAccessType = Literal["OAuth", "Token"]

GITLAB_API_ACCESS_TYPE_VALUES: set[GitlabApiAccessType] = {
    "OAuth",
    "Token",
}


def check_gitlab_api_access_type(value: str) -> GitlabApiAccessType:
    if value in GITLAB_API_ACCESS_TYPE_VALUES:
        return cast(GitlabApiAccessType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GITLAB_API_ACCESS_TYPE_VALUES!r}")
