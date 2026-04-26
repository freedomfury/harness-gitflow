from typing import Literal, cast

AwsKmsConnectorCredentialType = Literal["AssumeIAMRole", "AssumeSTSRole", "ManualConfig", "OidcAuthentication"]

AWS_KMS_CONNECTOR_CREDENTIAL_TYPE_VALUES: set[AwsKmsConnectorCredentialType] = {
    "AssumeIAMRole",
    "AssumeSTSRole",
    "ManualConfig",
    "OidcAuthentication",
}


def check_aws_kms_connector_credential_type(value: str) -> AwsKmsConnectorCredentialType:
    if value in AWS_KMS_CONNECTOR_CREDENTIAL_TYPE_VALUES:
        return cast(AwsKmsConnectorCredentialType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AWS_KMS_CONNECTOR_CREDENTIAL_TYPE_VALUES!r}")
