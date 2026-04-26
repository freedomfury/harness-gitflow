from typing import Literal, cast

GitlabAuthenticationType = Literal["Http", "Ssh"]

GITLAB_AUTHENTICATION_TYPE_VALUES: set[GitlabAuthenticationType] = {
    "Http",
    "Ssh",
}


def check_gitlab_authentication_type(value: str) -> GitlabAuthenticationType:
    if value in GITLAB_AUTHENTICATION_TYPE_VALUES:
        return cast(GitlabAuthenticationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GITLAB_AUTHENTICATION_TYPE_VALUES!r}")
