from typing import Literal, cast

EncryptionConfigEncryptionType = Literal[
    "AWS_SECRETS_MANAGER",
    "AZURE_VAULT",
    "CUSTOM",
    "CUSTOM_NG",
    "GCP_KMS",
    "GCP_SECRETS_MANAGER",
    "KMS",
    "LOCAL",
    "VAULT",
    "VAULT_SSH",
]

ENCRYPTION_CONFIG_ENCRYPTION_TYPE_VALUES: set[EncryptionConfigEncryptionType] = {
    "AWS_SECRETS_MANAGER",
    "AZURE_VAULT",
    "CUSTOM",
    "CUSTOM_NG",
    "GCP_KMS",
    "GCP_SECRETS_MANAGER",
    "KMS",
    "LOCAL",
    "VAULT",
    "VAULT_SSH",
}


def check_encryption_config_encryption_type(value: str) -> EncryptionConfigEncryptionType:
    if value in ENCRYPTION_CONFIG_ENCRYPTION_TYPE_VALUES:
        return cast(EncryptionConfigEncryptionType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENCRYPTION_CONFIG_ENCRYPTION_TYPE_VALUES!r}")
