from typing import Literal, cast

OciHelmAuthenticationType = Literal["Anonymous", "UsernamePassword"]

OCI_HELM_AUTHENTICATION_TYPE_VALUES: set[OciHelmAuthenticationType] = {
    "Anonymous",
    "UsernamePassword",
}


def check_oci_helm_authentication_type(value: str) -> OciHelmAuthenticationType:
    if value in OCI_HELM_AUTHENTICATION_TYPE_VALUES:
        return cast(OciHelmAuthenticationType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {OCI_HELM_AUTHENTICATION_TYPE_VALUES!r}")
