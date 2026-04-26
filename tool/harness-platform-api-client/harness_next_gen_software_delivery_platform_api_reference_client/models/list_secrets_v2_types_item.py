from typing import Literal, cast

ListSecretsV2TypesItem = Literal["SecretFile", "SecretText", "SSHKey", "WinRmCredentials"]

LIST_SECRETS_V2_TYPES_ITEM_VALUES: set[ListSecretsV2TypesItem] = {
    "SecretFile",
    "SecretText",
    "SSHKey",
    "WinRmCredentials",
}


def check_list_secrets_v2_types_item(value: str) -> ListSecretsV2TypesItem:
    if value in LIST_SECRETS_V2_TYPES_ITEM_VALUES:
        return cast(ListSecretsV2TypesItem, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {LIST_SECRETS_V2_TYPES_ITEM_VALUES!r}")
