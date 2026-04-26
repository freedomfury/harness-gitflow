from typing import Literal, cast

SourceCodeManagerType = Literal[
    "AWS_CODE_COMMIT",
    "AZURE_REPO",
    "BITBUCKET",
    "BITBUCKET_SERVER",
    "GITHUB",
    "GITHUB_ENTERPRISE",
    "GITLAB",
    "GITLAB_ON_PREM",
    "HARNESS",
]

SOURCE_CODE_MANAGER_TYPE_VALUES: set[SourceCodeManagerType] = {
    "AWS_CODE_COMMIT",
    "AZURE_REPO",
    "BITBUCKET",
    "BITBUCKET_SERVER",
    "GITHUB",
    "GITHUB_ENTERPRISE",
    "GITLAB",
    "GITLAB_ON_PREM",
    "HARNESS",
}


def check_source_code_manager_type(value: str) -> SourceCodeManagerType:
    if value in SOURCE_CODE_MANAGER_TYPE_VALUES:
        return cast(SourceCodeManagerType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SOURCE_CODE_MANAGER_TYPE_VALUES!r}")
