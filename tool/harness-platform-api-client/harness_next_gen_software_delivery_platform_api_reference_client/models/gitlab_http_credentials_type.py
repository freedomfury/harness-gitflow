from typing import Literal, cast

GitlabHttpCredentialsType = Literal["Kerberos", "OAuth", "UsernamePassword", "UsernameToken"]

GITLAB_HTTP_CREDENTIALS_TYPE_VALUES: set[GitlabHttpCredentialsType] = {
    "Kerberos",
    "OAuth",
    "UsernamePassword",
    "UsernameToken",
}


def check_gitlab_http_credentials_type(value: str) -> GitlabHttpCredentialsType:
    if value in GITLAB_HTTP_CREDENTIALS_TYPE_VALUES:
        return cast(GitlabHttpCredentialsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GITLAB_HTTP_CREDENTIALS_TYPE_VALUES!r}")
