from typing import Literal, cast

SecretManagerMetadataRequestEncryptionType = Literal[
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

SECRET_MANAGER_METADATA_REQUEST_ENCRYPTION_TYPE_VALUES: set[SecretManagerMetadataRequestEncryptionType] = {
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


def check_secret_manager_metadata_request_encryption_type(value: str) -> SecretManagerMetadataRequestEncryptionType:
    if value in SECRET_MANAGER_METADATA_REQUEST_ENCRYPTION_TYPE_VALUES:
        return cast(SecretManagerMetadataRequestEncryptionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SECRET_MANAGER_METADATA_REQUEST_ENCRYPTION_TYPE_VALUES!r}"
    )
