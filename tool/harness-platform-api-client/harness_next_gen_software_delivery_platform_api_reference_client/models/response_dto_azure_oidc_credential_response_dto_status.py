from typing import Literal, cast

ResponseDTOAzureOidcCredentialResponseDTOStatus = Literal["ERROR", "FAILURE", "SUCCESS"]

RESPONSE_DTO_AZURE_OIDC_CREDENTIAL_RESPONSE_DTO_STATUS_VALUES: set[ResponseDTOAzureOidcCredentialResponseDTOStatus] = {
    "ERROR",
    "FAILURE",
    "SUCCESS",
}


def check_response_dto_azure_oidc_credential_response_dto_status(
    value: str,
) -> ResponseDTOAzureOidcCredentialResponseDTOStatus:
    if value in RESPONSE_DTO_AZURE_OIDC_CREDENTIAL_RESPONSE_DTO_STATUS_VALUES:
        return cast(ResponseDTOAzureOidcCredentialResponseDTOStatus, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {RESPONSE_DTO_AZURE_OIDC_CREDENTIAL_RESPONSE_DTO_STATUS_VALUES!r}"
    )
