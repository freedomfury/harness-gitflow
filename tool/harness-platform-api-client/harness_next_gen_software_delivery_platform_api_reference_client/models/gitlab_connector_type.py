from typing import Literal, cast

GitlabConnectorType = Literal["Account", "Project", "Repo"]

GITLAB_CONNECTOR_TYPE_VALUES: set[GitlabConnectorType] = {
    "Account",
    "Project",
    "Repo",
}


def check_gitlab_connector_type(value: str) -> GitlabConnectorType:
    if value in GITLAB_CONNECTOR_TYPE_VALUES:
        return cast(GitlabConnectorType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GITLAB_CONNECTOR_TYPE_VALUES!r}")
