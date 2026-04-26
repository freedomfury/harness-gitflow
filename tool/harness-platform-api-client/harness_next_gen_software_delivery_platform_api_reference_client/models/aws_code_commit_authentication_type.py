from typing import Literal, cast

AwsCodeCommitAuthenticationType = Literal["HTTPS"]

AWS_CODE_COMMIT_AUTHENTICATION_TYPE_VALUES: set[AwsCodeCommitAuthenticationType] = {
    "HTTPS",
}


def check_aws_code_commit_authentication_type(value: str) -> AwsCodeCommitAuthenticationType:
    if value in AWS_CODE_COMMIT_AUTHENTICATION_TYPE_VALUES:
        return cast(AwsCodeCommitAuthenticationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AWS_CODE_COMMIT_AUTHENTICATION_TYPE_VALUES!r}")
