from typing import Literal, cast

AwsCodeCommitConnectorType = Literal["Region", "Repo"]

AWS_CODE_COMMIT_CONNECTOR_TYPE_VALUES: set[AwsCodeCommitConnectorType] = {
    "Region",
    "Repo",
}


def check_aws_code_commit_connector_type(value: str) -> AwsCodeCommitConnectorType:
    if value in AWS_CODE_COMMIT_CONNECTOR_TYPE_VALUES:
        return cast(AwsCodeCommitConnectorType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AWS_CODE_COMMIT_CONNECTOR_TYPE_VALUES!r}")
