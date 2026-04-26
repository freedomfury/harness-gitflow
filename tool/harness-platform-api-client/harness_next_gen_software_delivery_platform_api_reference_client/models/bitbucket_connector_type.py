from typing import Literal, cast

BitbucketConnectorType = Literal["Account", "Repo"]

BITBUCKET_CONNECTOR_TYPE_VALUES: set[BitbucketConnectorType] = {
    "Account",
    "Repo",
}


def check_bitbucket_connector_type(value: str) -> BitbucketConnectorType:
    if value in BITBUCKET_CONNECTOR_TYPE_VALUES:
        return cast(BitbucketConnectorType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {BITBUCKET_CONNECTOR_TYPE_VALUES!r}")
