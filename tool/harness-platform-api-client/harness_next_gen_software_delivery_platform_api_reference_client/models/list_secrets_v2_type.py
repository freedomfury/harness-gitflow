from typing import Literal, cast

ListSecretsV2Type = Literal["SecretFile", "SecretText", "SSHKey", "WinRmCredentials"]

LIST_SECRETS_V2_TYPE_VALUES: set[ListSecretsV2Type] = {
    "SecretFile",
    "SecretText",
    "SSHKey",
    "WinRmCredentials",
}


def check_list_secrets_v2_type(value: str) -> ListSecretsV2Type:
    if value in LIST_SECRETS_V2_TYPE_VALUES:
        return cast(ListSecretsV2Type, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_SECRETS_V2_TYPE_VALUES!r}")
