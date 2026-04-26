from typing import Literal, cast

VaultConnectorAccessType = Literal["APP_ROLE", "AWS_IAM", "JWT", "K8s_AUTH", "TOKEN", "VAULT_AGENT"]

VAULT_CONNECTOR_ACCESS_TYPE_VALUES: set[VaultConnectorAccessType] = {
    "APP_ROLE",
    "AWS_IAM",
    "JWT",
    "K8s_AUTH",
    "TOKEN",
    "VAULT_AGENT",
}


def check_vault_connector_access_type(value: str) -> VaultConnectorAccessType:
    if value in VAULT_CONNECTOR_ACCESS_TYPE_VALUES:
        return cast(VaultConnectorAccessType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {VAULT_CONNECTOR_ACCESS_TYPE_VALUES!r}")
