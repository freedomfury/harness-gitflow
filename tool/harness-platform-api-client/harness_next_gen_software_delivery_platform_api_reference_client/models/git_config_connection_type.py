from typing import Literal, cast

GitConfigConnectionType = Literal["Account", "Project", "Repo"]

GIT_CONFIG_CONNECTION_TYPE_VALUES: set[GitConfigConnectionType] = {
    "Account",
    "Project",
    "Repo",
}


def check_git_config_connection_type(value: str) -> GitConfigConnectionType:
    if value in GIT_CONFIG_CONNECTION_TYPE_VALUES:
        return cast(GitConfigConnectionType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GIT_CONFIG_CONNECTION_TYPE_VALUES!r}")
