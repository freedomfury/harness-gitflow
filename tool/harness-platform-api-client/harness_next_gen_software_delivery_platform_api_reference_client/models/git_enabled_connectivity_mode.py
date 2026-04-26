from typing import Literal, cast

GitEnabledConnectivityMode = Literal["DELEGATE", "MANAGER"]

GIT_ENABLED_CONNECTIVITY_MODE_VALUES: set[GitEnabledConnectivityMode] = {
    "DELEGATE",
    "MANAGER",
}


def check_git_enabled_connectivity_mode(value: str) -> GitEnabledConnectivityMode:
    if value in GIT_ENABLED_CONNECTIVITY_MODE_VALUES:
        return cast(GitEnabledConnectivityMode, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GIT_ENABLED_CONNECTIVITY_MODE_VALUES!r}")
