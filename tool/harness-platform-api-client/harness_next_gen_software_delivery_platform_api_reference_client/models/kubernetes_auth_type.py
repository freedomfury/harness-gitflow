from typing import Literal, cast

KubernetesAuthType = Literal["ClientKeyCert", "OpenIdConnect", "ServiceAccount", "UsernamePassword"]

KUBERNETES_AUTH_TYPE_VALUES: set[KubernetesAuthType] = {
    "ClientKeyCert",
    "OpenIdConnect",
    "ServiceAccount",
    "UsernamePassword",
}


def check_kubernetes_auth_type(value: str) -> KubernetesAuthType:
    if value in KUBERNETES_AUTH_TYPE_VALUES:
        return cast(KubernetesAuthType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {KUBERNETES_AUTH_TYPE_VALUES!r}")
