from typing import Literal, cast

SSHConfigCredentialType = Literal["KeyPath", "KeyReference", "Password"]

SSH_CONFIG_CREDENTIAL_TYPE_VALUES: set[SSHConfigCredentialType] = {
    "KeyPath",
    "KeyReference",
    "Password",
}


def check_ssh_config_credential_type(value: str) -> SSHConfigCredentialType:
    if value in SSH_CONFIG_CREDENTIAL_TYPE_VALUES:
        return cast(SSHConfigCredentialType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SSH_CONFIG_CREDENTIAL_TYPE_VALUES!r}")
