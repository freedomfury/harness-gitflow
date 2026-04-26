from typing import Literal, cast

CeAwsCredentialType = Literal["Default", "OidcAuthentication"]

CE_AWS_CREDENTIAL_TYPE_VALUES: set[CeAwsCredentialType] = {
    "Default",
    "OidcAuthentication",
}


def check_ce_aws_credential_type(value: str) -> CeAwsCredentialType:
    if value in CE_AWS_CREDENTIAL_TYPE_VALUES:
        return cast(CeAwsCredentialType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {CE_AWS_CREDENTIAL_TYPE_VALUES!r}")
