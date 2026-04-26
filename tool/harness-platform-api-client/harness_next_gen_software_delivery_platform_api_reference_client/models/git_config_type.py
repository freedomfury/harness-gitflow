from typing import Literal, cast

GitConfigType = Literal["Http", "Ssh"]

GIT_CONFIG_TYPE_VALUES: set[GitConfigType] = {
    "Http",
    "Ssh",
}


def check_git_config_type(value: str) -> GitConfigType:
    if value in GIT_CONFIG_TYPE_VALUES:
        return cast(GitConfigType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GIT_CONFIG_TYPE_VALUES!r}")
