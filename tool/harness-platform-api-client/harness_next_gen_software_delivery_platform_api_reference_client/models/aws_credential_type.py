from typing import Literal, cast

AwsCredentialType = Literal["InheritFromDelegate", "Irsa", "ManualConfig", "OidcAuthentication"]

AWS_CREDENTIAL_TYPE_VALUES: set[AwsCredentialType] = {
    "InheritFromDelegate",
    "Irsa",
    "ManualConfig",
    "OidcAuthentication",
}


def check_aws_credential_type(value: str) -> AwsCredentialType:
    if value in AWS_CREDENTIAL_TYPE_VALUES:
        return cast(AwsCredentialType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {AWS_CREDENTIAL_TYPE_VALUES!r}")
