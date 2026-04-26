from typing import Literal, cast

SecretManagerMetadataDTOEncryptionType = Literal[
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

SECRET_MANAGER_METADATA_DTO_ENCRYPTION_TYPE_VALUES: set[SecretManagerMetadataDTOEncryptionType] = {
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


def check_secret_manager_metadata_dto_encryption_type(value: str) -> SecretManagerMetadataDTOEncryptionType:
    if value in SECRET_MANAGER_METADATA_DTO_ENCRYPTION_TYPE_VALUES:
        return cast(SecretManagerMetadataDTOEncryptionType, value)
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {SECRET_MANAGER_METADATA_DTO_ENCRYPTION_TYPE_VALUES!r}"
    )
