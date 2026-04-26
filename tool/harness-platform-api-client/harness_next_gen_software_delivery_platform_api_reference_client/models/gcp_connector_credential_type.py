from typing import Literal, cast

GcpConnectorCredentialType = Literal["InheritFromDelegate", "ManualConfig", "OidcAuthentication"]

GCP_CONNECTOR_CREDENTIAL_TYPE_VALUES: set[GcpConnectorCredentialType] = {
    "InheritFromDelegate",
    "ManualConfig",
    "OidcAuthentication",
}


def check_gcp_connector_credential_type(value: str) -> GcpConnectorCredentialType:
    if value in GCP_CONNECTOR_CREDENTIAL_TYPE_VALUES:
        return cast(GcpConnectorCredentialType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {GCP_CONNECTOR_CREDENTIAL_TYPE_VALUES!r}")
