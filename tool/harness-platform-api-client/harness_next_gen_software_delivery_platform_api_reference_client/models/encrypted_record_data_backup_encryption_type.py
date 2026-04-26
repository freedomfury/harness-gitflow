from typing import Literal, cast

EncryptedRecordDataBackupEncryptionType = Literal[
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

ENCRYPTED_RECORD_DATA_BACKUP_ENCRYPTION_TYPE_VALUES: set[EncryptedRecordDataBackupEncryptionType] = {
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


def check_encrypted_record_data_backup_encryption_type(value: str) -> EncryptedRecordDataBackupEncryptionType:
    if value in ENCRYPTED_RECORD_DATA_BACKUP_ENCRYPTION_TYPE_VALUES:
        return cast(EncryptedRecordDataBackupEncryptionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ENCRYPTED_RECORD_DATA_BACKUP_ENCRYPTION_TYPE_VALUES!r}"
    )
