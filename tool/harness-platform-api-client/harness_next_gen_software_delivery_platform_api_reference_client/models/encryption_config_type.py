from typing import Literal, cast

EncryptionConfigType = Literal["CUSTOM", "KMS", "SSH", "VAULT"]

ENCRYPTION_CONFIG_TYPE_VALUES: set[EncryptionConfigType] = {
    "CUSTOM",
    "KMS",
    "SSH",
    "VAULT",
}


def check_encryption_config_type(value: str) -> EncryptionConfigType:
    if value in ENCRYPTION_CONFIG_TYPE_VALUES:
        return cast(EncryptionConfigType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENCRYPTION_CONFIG_TYPE_VALUES!r}")
