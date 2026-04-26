from typing import Literal, cast

KubernetesCredentialType = Literal["InheritFromDelegate", "ManualConfig"]

KUBERNETES_CREDENTIAL_TYPE_VALUES: set[KubernetesCredentialType] = {
    "InheritFromDelegate",
    "ManualConfig",
}


def check_kubernetes_credential_type(value: str) -> KubernetesCredentialType:
    if value in KUBERNETES_CREDENTIAL_TYPE_VALUES:
        return cast(KubernetesCredentialType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {KUBERNETES_CREDENTIAL_TYPE_VALUES!r}")
