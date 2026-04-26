from typing import Literal, cast

GithubConnectorType = Literal["Account", "Repo"]

GITHUB_CONNECTOR_TYPE_VALUES: set[GithubConnectorType] = {
    "Account",
    "Repo",
}


def check_github_connector_type(value: str) -> GithubConnectorType:
    if value in GITHUB_CONNECTOR_TYPE_VALUES:
        return cast(GithubConnectorType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GITHUB_CONNECTOR_TYPE_VALUES!r}")
