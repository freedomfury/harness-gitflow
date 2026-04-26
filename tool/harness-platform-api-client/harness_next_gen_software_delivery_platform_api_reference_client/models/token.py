from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.token_api_key_type import TokenApiKeyType, check_token_api_key_type
from ..models.token_pgp_key_usage_item import TokenPgpKeyUsageItem, check_token_pgp_key_usage_item
from ..models.token_revocation_reason import TokenRevocationReason, check_token_revocation_reason
from ..models.token_ssh_key_usage_item import TokenSshKeyUsageItem, check_token_ssh_key_usage_item
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pgp_key_identity import PGPKeyIdentity
    from ..models.token_tags import TokenTags


T = TypeVar("T", bound="Token")


@_attrs_define
class Token:
    """This has the API Key Token details defined in Harness.

    Attributes:
        identifier (str): Identifier of the Token
        name (str): Name of the Token
        api_key_identifier (str): This is the API Key Id within which the Token is created.
        valid_from (int | Unset): This is the time from which the Token is valid. The time is in milliseconds.
        valid_to (int | Unset): This is the time till which the Token is valid. The time is in milliseconds.
        scheduled_expire_time (int | Unset): Scheduled expiry time in milliseconds.
        valid (bool | Unset): Boolean value to indicate if Token is valid or not.
        account_identifier (str | Unset): Account Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        parent_identifier (str | Unset): This is the ID of the Parent entity from which the Token inherits its role
            bindings.
        api_key_type (TokenApiKeyType | Unset): Type of the API Key
        description (str | Unset): Description of the Token
        tags (TokenTags | Unset): Tags for the Token
        ssh_key_content (str | Unset): SSH key content from a public key, this is only present if API_KEY Type is
            SSH_KEY
        ssh_key_usage (list[TokenSshKeyUsageItem] | Unset): SSH key Usage: SSH keys can be used to authenticate or sign
        content (str | Unset): PGP key content from a public key, this is only present if API_KEY Type is PGP_KEY
        pgp_key_usage (list[TokenPgpKeyUsageItem] | Unset): PGP key Usage: PGP keys can be used to sign, encrypt,
            authenticate or certify
        pgp_key_id (str | Unset): PGP key ID: Last 8 bytes of the fingerprint
        pgp_primary_user_id (str | Unset): Primary user ID associated with the PGP key
        pgp_key_algorithm (str | Unset): PGP key algorithm (RSA, DSA, ECDSA, EdDSA)
        pgp_identities (list[PGPKeyIdentity] | Unset): PGP key identities (name and email pairs)
        pgp_primary_identity (PGPKeyIdentity | Unset): Primary identity associated with the PGP key
        pgp_parent_key_id (str | Unset): For subkeys: the keyId of the parent/master key. Null for primary keys.
        pgp_is_sub_key (bool | Unset): Indicates if this is a subkey (true) or a primary/master key (false)
        revocation_reason (TokenRevocationReason | Unset): Revocation reason if the key has been revoked
    """

    identifier: str
    name: str
    api_key_identifier: str
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    scheduled_expire_time: int | Unset = UNSET
    valid: bool | Unset = UNSET
    account_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    parent_identifier: str | Unset = UNSET
    api_key_type: TokenApiKeyType | Unset = UNSET
    description: str | Unset = UNSET
    tags: TokenTags | Unset = UNSET
    ssh_key_content: str | Unset = UNSET
    ssh_key_usage: list[TokenSshKeyUsageItem] | Unset = UNSET
    content: str | Unset = UNSET
    pgp_key_usage: list[TokenPgpKeyUsageItem] | Unset = UNSET
    pgp_key_id: str | Unset = UNSET
    pgp_primary_user_id: str | Unset = UNSET
    pgp_key_algorithm: str | Unset = UNSET
    pgp_identities: list[PGPKeyIdentity] | Unset = UNSET
    pgp_primary_identity: PGPKeyIdentity | Unset = UNSET
    pgp_parent_key_id: str | Unset = UNSET
    pgp_is_sub_key: bool | Unset = UNSET
    revocation_reason: TokenRevocationReason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        name = self.name

        api_key_identifier = self.api_key_identifier

        valid_from = self.valid_from

        valid_to = self.valid_to

        scheduled_expire_time = self.scheduled_expire_time

        valid = self.valid

        account_identifier = self.account_identifier

        project_identifier = self.project_identifier

        org_identifier = self.org_identifier

        parent_identifier = self.parent_identifier

        api_key_type: str | Unset = UNSET
        if not isinstance(self.api_key_type, Unset):
            api_key_type = self.api_key_type

        description = self.description

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        ssh_key_content = self.ssh_key_content

        ssh_key_usage: list[str] | Unset = UNSET
        if not isinstance(self.ssh_key_usage, Unset):
            ssh_key_usage = []
            for ssh_key_usage_item_data in self.ssh_key_usage:
                ssh_key_usage_item: str = ssh_key_usage_item_data
                ssh_key_usage.append(ssh_key_usage_item)

        content = self.content

        pgp_key_usage: list[str] | Unset = UNSET
        if not isinstance(self.pgp_key_usage, Unset):
            pgp_key_usage = []
            for pgp_key_usage_item_data in self.pgp_key_usage:
                pgp_key_usage_item: str = pgp_key_usage_item_data
                pgp_key_usage.append(pgp_key_usage_item)

        pgp_key_id = self.pgp_key_id

        pgp_primary_user_id = self.pgp_primary_user_id

        pgp_key_algorithm = self.pgp_key_algorithm

        pgp_identities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pgp_identities, Unset):
            pgp_identities = []
            for pgp_identities_item_data in self.pgp_identities:
                pgp_identities_item = pgp_identities_item_data.to_dict()
                pgp_identities.append(pgp_identities_item)

        pgp_primary_identity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pgp_primary_identity, Unset):
            pgp_primary_identity = self.pgp_primary_identity.to_dict()

        pgp_parent_key_id = self.pgp_parent_key_id

        pgp_is_sub_key = self.pgp_is_sub_key

        revocation_reason: str | Unset = UNSET
        if not isinstance(self.revocation_reason, Unset):
            revocation_reason = self.revocation_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "name": name,
                "apiKeyIdentifier": api_key_identifier,
            }
        )
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to
        if scheduled_expire_time is not UNSET:
            field_dict["scheduledExpireTime"] = scheduled_expire_time
        if valid is not UNSET:
            field_dict["valid"] = valid
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if parent_identifier is not UNSET:
            field_dict["parentIdentifier"] = parent_identifier
        if api_key_type is not UNSET:
            field_dict["apiKeyType"] = api_key_type
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if ssh_key_content is not UNSET:
            field_dict["sshKeyContent"] = ssh_key_content
        if ssh_key_usage is not UNSET:
            field_dict["sshKeyUsage"] = ssh_key_usage
        if content is not UNSET:
            field_dict["content"] = content
        if pgp_key_usage is not UNSET:
            field_dict["pgpKeyUsage"] = pgp_key_usage
        if pgp_key_id is not UNSET:
            field_dict["pgpKeyId"] = pgp_key_id
        if pgp_primary_user_id is not UNSET:
            field_dict["pgpPrimaryUserId"] = pgp_primary_user_id
        if pgp_key_algorithm is not UNSET:
            field_dict["pgpKeyAlgorithm"] = pgp_key_algorithm
        if pgp_identities is not UNSET:
            field_dict["pgpIdentities"] = pgp_identities
        if pgp_primary_identity is not UNSET:
            field_dict["pgpPrimaryIdentity"] = pgp_primary_identity
        if pgp_parent_key_id is not UNSET:
            field_dict["pgpParentKeyId"] = pgp_parent_key_id
        if pgp_is_sub_key is not UNSET:
            field_dict["pgpIsSubKey"] = pgp_is_sub_key
        if revocation_reason is not UNSET:
            field_dict["revocationReason"] = revocation_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pgp_key_identity import PGPKeyIdentity
        from ..models.token_tags import TokenTags

        d = dict(src_dict)
        identifier = d.pop("identifier")

        name = d.pop("name")

        api_key_identifier = d.pop("apiKeyIdentifier")

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        scheduled_expire_time = d.pop("scheduledExpireTime", UNSET)

        valid = d.pop("valid", UNSET)

        account_identifier = d.pop("accountIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        parent_identifier = d.pop("parentIdentifier", UNSET)

        _api_key_type = d.pop("apiKeyType", UNSET)
        api_key_type: TokenApiKeyType | Unset
        if isinstance(_api_key_type, Unset):
            api_key_type = UNSET
        else:
            api_key_type = check_token_api_key_type(_api_key_type)

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: TokenTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = TokenTags.from_dict(_tags)

        ssh_key_content = d.pop("sshKeyContent", UNSET)

        _ssh_key_usage = d.pop("sshKeyUsage", UNSET)
        ssh_key_usage: list[TokenSshKeyUsageItem] | Unset = UNSET
        if _ssh_key_usage is not UNSET:
            ssh_key_usage = []
            for ssh_key_usage_item_data in _ssh_key_usage:
                ssh_key_usage_item = check_token_ssh_key_usage_item(ssh_key_usage_item_data)

                ssh_key_usage.append(ssh_key_usage_item)

        content = d.pop("content", UNSET)

        _pgp_key_usage = d.pop("pgpKeyUsage", UNSET)
        pgp_key_usage: list[TokenPgpKeyUsageItem] | Unset = UNSET
        if _pgp_key_usage is not UNSET:
            pgp_key_usage = []
            for pgp_key_usage_item_data in _pgp_key_usage:
                pgp_key_usage_item = check_token_pgp_key_usage_item(pgp_key_usage_item_data)

                pgp_key_usage.append(pgp_key_usage_item)

        pgp_key_id = d.pop("pgpKeyId", UNSET)

        pgp_primary_user_id = d.pop("pgpPrimaryUserId", UNSET)

        pgp_key_algorithm = d.pop("pgpKeyAlgorithm", UNSET)

        _pgp_identities = d.pop("pgpIdentities", UNSET)
        pgp_identities: list[PGPKeyIdentity] | Unset = UNSET
        if _pgp_identities is not UNSET:
            pgp_identities = []
            for pgp_identities_item_data in _pgp_identities:
                pgp_identities_item = PGPKeyIdentity.from_dict(pgp_identities_item_data)

                pgp_identities.append(pgp_identities_item)

        _pgp_primary_identity = d.pop("pgpPrimaryIdentity", UNSET)
        pgp_primary_identity: PGPKeyIdentity | Unset
        if isinstance(_pgp_primary_identity, Unset):
            pgp_primary_identity = UNSET
        else:
            pgp_primary_identity = PGPKeyIdentity.from_dict(_pgp_primary_identity)

        pgp_parent_key_id = d.pop("pgpParentKeyId", UNSET)

        pgp_is_sub_key = d.pop("pgpIsSubKey", UNSET)

        _revocation_reason = d.pop("revocationReason", UNSET)
        revocation_reason: TokenRevocationReason | Unset
        if isinstance(_revocation_reason, Unset):
            revocation_reason = UNSET
        else:
            revocation_reason = check_token_revocation_reason(_revocation_reason)

        token = cls(
            identifier=identifier,
            name=name,
            api_key_identifier=api_key_identifier,
            valid_from=valid_from,
            valid_to=valid_to,
            scheduled_expire_time=scheduled_expire_time,
            valid=valid,
            account_identifier=account_identifier,
            project_identifier=project_identifier,
            org_identifier=org_identifier,
            parent_identifier=parent_identifier,
            api_key_type=api_key_type,
            description=description,
            tags=tags,
            ssh_key_content=ssh_key_content,
            ssh_key_usage=ssh_key_usage,
            content=content,
            pgp_key_usage=pgp_key_usage,
            pgp_key_id=pgp_key_id,
            pgp_primary_user_id=pgp_primary_user_id,
            pgp_key_algorithm=pgp_key_algorithm,
            pgp_identities=pgp_identities,
            pgp_primary_identity=pgp_primary_identity,
            pgp_parent_key_id=pgp_parent_key_id,
            pgp_is_sub_key=pgp_is_sub_key,
            revocation_reason=revocation_reason,
        )

        token.additional_properties = d
        return token

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
