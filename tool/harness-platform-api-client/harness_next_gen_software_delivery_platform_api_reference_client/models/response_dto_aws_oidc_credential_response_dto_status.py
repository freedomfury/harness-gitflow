from typing import Literal, cast

ResponseDTOAwsOidcCredentialResponseDtoStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_AWS_OIDC_CREDENTIAL_RESPONSE_DTO_STATUS_VALUES: set[ResponseDTOAwsOidcCredentialResponseDtoStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_aws_oidc_credential_response_dto_status(
    value: str,
) -> ResponseDTOAwsOidcCredentialResponseDtoStatus:
    if value in RESPONSE_DTO_AWS_OIDC_CREDENTIAL_RESPONSE_DTO_STATUS_VALUES:
        return cast(ResponseDTOAwsOidcCredentialResponseDtoStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_AWS_OIDC_CREDENTIAL_RESPONSE_DTO_STATUS_VALUES!r}"
    )
