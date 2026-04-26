from typing import Literal, cast

AwsCodeCommitHttpsCredentialsType = Literal["AWSCredentials"]

AWS_CODE_COMMIT_HTTPS_CREDENTIALS_TYPE_VALUES: set[AwsCodeCommitHttpsCredentialsType] = {
    "AWSCredentials",
}


def check_aws_code_commit_https_credentials_type(value: str) -> AwsCodeCommitHttpsCredentialsType:
    if value in AWS_CODE_COMMIT_HTTPS_CREDENTIALS_TYPE_VALUES:
        return cast(AwsCodeCommitHttpsCredentialsType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AWS_CODE_COMMIT_HTTPS_CREDENTIALS_TYPE_VALUES!r}")
