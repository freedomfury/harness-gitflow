from typing import Literal, cast

EncryptedRecordDataEncryptionType = Literal[
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

ENCRYPTED_RECORD_DATA_ENCRYPTION_TYPE_VALUES: set[EncryptedRecordDataEncryptionType] = {
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


def check_encrypted_record_data_encryption_type(value: str) -> EncryptedRecordDataEncryptionType:
    if value in ENCRYPTED_RECORD_DATA_ENCRYPTION_TYPE_VALUES:
        return cast(EncryptedRecordDataEncryptionType, value)
    raise TypeError(f"Unexpected value {value!r}. Expected one of {ENCRYPTED_RECORD_DATA_ENCRYPTION_TYPE_VALUES!r}")
