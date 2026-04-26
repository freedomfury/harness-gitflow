from typing import Literal, cast

AwsSecretManagerCredentialType = Literal["AssumeIAMRole", "AssumeSTSRole", "ManualConfig", "OidcAuthentication"]

AWS_SECRET_MANAGER_CREDENTIAL_TYPE_VALUES: set[AwsSecretManagerCredentialType] = {
    "AssumeIAMRole",
    "AssumeSTSRole",
    "ManualConfig",
    "OidcAuthentication",
}


def check_aws_secret_manager_credential_type(value: str) -> AwsSecretManagerCredentialType:
    if value in AWS_SECRET_MANAGER_CREDENTIAL_TYPE_VALUES:
        return cast(AwsSecretManagerCredentialType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AWS_SECRET_MANAGER_CREDENTIAL_TYPE_VALUES!r}")
