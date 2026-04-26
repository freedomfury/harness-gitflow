from typing import Literal, cast

GcpCcmConnectorCredentialType = Literal["Default", "OidcAuthentication"]

GCP_CCM_CONNECTOR_CREDENTIAL_TYPE_VALUES: set[GcpCcmConnectorCredentialType] = {
    "Default",
    "OidcAuthentication",
}


def check_gcp_ccm_connector_credential_type(value: str) -> GcpCcmConnectorCredentialType:
    if value in GCP_CCM_CONNECTOR_CREDENTIAL_TYPE_VALUES:
        return cast(GcpCcmConnectorCredentialType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GCP_CCM_CONNECTOR_CREDENTIAL_TYPE_VALUES!r}")
