from typing import Literal, cast

StoreConfigWrapperType = Literal[
    "ArtifactBundle",
    "Artifactory",
    "AzureRepo",
    "Bitbucket",
    "CustomRemote",
    "Gcs",
    "Git",
    "Github",
    "GitLab",
    "Harness",
    "HarnessCode",
    "Http",
    "InheritFromManifest",
    "Inline",
    "OciHelmChart",
    "S3",
    "S3Url",
]

STORE_CONFIG_WRAPPER_TYPE_VALUES: set[StoreConfigWrapperType] = {
    "ArtifactBundle",
    "Artifactory",
    "AzureRepo",
    "Bitbucket",
    "CustomRemote",
    "Gcs",
    "Git",
    "Github",
    "GitLab",
    "Harness",
    "HarnessCode",
    "Http",
    "InheritFromManifest",
    "Inline",
    "OciHelmChart",
    "S3",
    "S3Url",
}


def check_store_config_wrapper_type(value: str) -> StoreConfigWrapperType:
    if value in STORE_CONFIG_WRAPPER_TYPE_VALUES:
        return cast(StoreConfigWrapperType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {STORE_CONFIG_WRAPPER_TYPE_VALUES!r}")
