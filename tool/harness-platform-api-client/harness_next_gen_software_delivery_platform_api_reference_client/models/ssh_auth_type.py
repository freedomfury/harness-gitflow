from typing import Literal, cast

SSHAuthType = Literal["Kerberos", "SSH"]

SSH_AUTH_TYPE_VALUES: set[SSHAuthType] = {
    "Kerberos",
    "SSH",
}


def check_ssh_auth_type(value: str) -> SSHAuthType:
    if value in SSH_AUTH_TYPE_VALUES:
        return cast(SSHAuthType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {SSH_AUTH_TYPE_VALUES!r}")
