from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.key_key_scheme import KeyKeyScheme, check_key_key_scheme
from ..models.key_key_usage_item import KeyKeyUsageItem, check_key_key_usage_item
from ..models.key_revocation_reason import KeyRevocationReason, check_key_revocation_reason
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.key_tags import KeyTags
    from ..models.pgp_key_identity import PGPKeyIdentity


T = TypeVar("T", bound="Key")


@_attrs_define
class Key:
    """This has the Key details defined in Harness.

    Attributes:
        identifier (str): Identifier of the Key
        name (str): Name of the key
        valid_from (int | Unset): This is the time from which the key is valid. The time is in milliseconds.
        valid_to (int | Unset): This is the time till which the key is valid. The time is in milliseconds.
        account_identifier (str | Unset): Account Identifier for the Entity.
        parent_identifier (str | Unset): This is the ID of the Parent entity from which the Token inherits its role
            bindings.
        description (str | Unset): Description of the key
        tags (KeyTags | Unset): Tags for the key
        key (str | Unset): Public key value
        key_usage (list[KeyKeyUsageItem] | Unset): Keys can be used to authenticate, sign, encrypt, or certify
        key_id (str | Unset): Key ID: Last 8 bytes of the fingerprint
        primary_user_id (str | Unset): Primary user ID associated with the key
        key_algorithm (str | Unset): Key algorithm (RSA, DSA, ECDSA, EdDSA)
        key_scheme (KeyKeyScheme | Unset): Key scheme: ssh (default) or pgp
        identities (list[PGPKeyIdentity] | Unset): Key identities (name and email pairs, PGP only)
        primary_identity (PGPKeyIdentity | Unset): Primary identity associated with the PGP key
        parent_key_id (str | Unset): For subkeys: the keyId of the parent/master key. Null for primary keys.
        is_sub_key (bool | Unset): Indicates if this is a subkey (true) or a primary/master key (false)
        revocation_reason (KeyRevocationReason | Unset): Revocation reason if the key has been revoked
    """

    identifier: str
    name: str
    valid_from: int | Unset = UNSET
    valid_to: int | Unset = UNSET
    account_identifier: str | Unset = UNSET
    parent_identifier: str | Unset = UNSET
    description: str | Unset = UNSET
    tags: KeyTags | Unset = UNSET
    key: str | Unset = UNSET
    key_usage: list[KeyKeyUsageItem] | Unset = UNSET
    key_id: str | Unset = UNSET
    primary_user_id: str | Unset = UNSET
    key_algorithm: str | Unset = UNSET
    key_scheme: KeyKeyScheme | Unset = UNSET
    identities: list[PGPKeyIdentity] | Unset = UNSET
    primary_identity: PGPKeyIdentity | Unset = UNSET
    parent_key_id: str | Unset = UNSET
    is_sub_key: bool | Unset = UNSET
    revocation_reason: KeyRevocationReason | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        name = self.name

        valid_from = self.valid_from

        valid_to = self.valid_to

        account_identifier = self.account_identifier

        parent_identifier = self.parent_identifier

        description = self.description

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        key = self.key

        key_usage: list[str] | Unset = UNSET
        if not isinstance(self.key_usage, Unset):
            key_usage = []
            for key_usage_item_data in self.key_usage:
                key_usage_item: str = key_usage_item_data
                key_usage.append(key_usage_item)

        key_id = self.key_id

        primary_user_id = self.primary_user_id

        key_algorithm = self.key_algorithm

        key_scheme: str | Unset = UNSET
        if not isinstance(self.key_scheme, Unset):
            key_scheme = self.key_scheme

        identities: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.identities, Unset):
            identities = []
            for identities_item_data in self.identities:
                identities_item = identities_item_data.to_dict()
                identities.append(identities_item)

        primary_identity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.primary_identity, Unset):
            primary_identity = self.primary_identity.to_dict()

        parent_key_id = self.parent_key_id

        is_sub_key = self.is_sub_key

        revocation_reason: str | Unset = UNSET
        if not isinstance(self.revocation_reason, Unset):
            revocation_reason = self.revocation_reason

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "name": name,
            }
        )
        if valid_from is not UNSET:
            field_dict["validFrom"] = valid_from
        if valid_to is not UNSET:
            field_dict["validTo"] = valid_to
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if parent_identifier is not UNSET:
            field_dict["parentIdentifier"] = parent_identifier
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if key is not UNSET:
            field_dict["key"] = key
        if key_usage is not UNSET:
            field_dict["keyUsage"] = key_usage
        if key_id is not UNSET:
            field_dict["keyId"] = key_id
        if primary_user_id is not UNSET:
            field_dict["primaryUserId"] = primary_user_id
        if key_algorithm is not UNSET:
            field_dict["keyAlgorithm"] = key_algorithm
        if key_scheme is not UNSET:
            field_dict["keyScheme"] = key_scheme
        if identities is not UNSET:
            field_dict["identities"] = identities
        if primary_identity is not UNSET:
            field_dict["primaryIdentity"] = primary_identity
        if parent_key_id is not UNSET:
            field_dict["parentKeyId"] = parent_key_id
        if is_sub_key is not UNSET:
            field_dict["isSubKey"] = is_sub_key
        if revocation_reason is not UNSET:
            field_dict["revocationReason"] = revocation_reason

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.key_tags import KeyTags
        from ..models.pgp_key_identity import PGPKeyIdentity

        d = dict(src_dict)
        identifier = d.pop("identifier")

        name = d.pop("name")

        valid_from = d.pop("validFrom", UNSET)

        valid_to = d.pop("validTo", UNSET)

        account_identifier = d.pop("accountIdentifier", UNSET)

        parent_identifier = d.pop("parentIdentifier", UNSET)

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: KeyTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = KeyTags.from_dict(_tags)

        key = d.pop("key", UNSET)

        _key_usage = d.pop("keyUsage", UNSET)
        key_usage: list[KeyKeyUsageItem] | Unset = UNSET
        if _key_usage is not UNSET:
            key_usage = []
            for key_usage_item_data in _key_usage:
                key_usage_item = check_key_key_usage_item(key_usage_item_data)

                key_usage.append(key_usage_item)

        key_id = d.pop("keyId", UNSET)

        primary_user_id = d.pop("primaryUserId", UNSET)

        key_algorithm = d.pop("keyAlgorithm", UNSET)

        _key_scheme = d.pop("keyScheme", UNSET)
        key_scheme: KeyKeyScheme | Unset
        if isinstance(_key_scheme, Unset):
            key_scheme = UNSET
        else:
            key_scheme = check_key_key_scheme(_key_scheme)

        _identities = d.pop("identities", UNSET)
        identities: list[PGPKeyIdentity] | Unset = UNSET
        if _identities is not UNSET:
            identities = []
            for identities_item_data in _identities:
                identities_item = PGPKeyIdentity.from_dict(identities_item_data)

                identities.append(identities_item)

        _primary_identity = d.pop("primaryIdentity", UNSET)
        primary_identity: PGPKeyIdentity | Unset
        if isinstance(_primary_identity, Unset):
            primary_identity = UNSET
        else:
            primary_identity = PGPKeyIdentity.from_dict(_primary_identity)

        parent_key_id = d.pop("parentKeyId", UNSET)

        is_sub_key = d.pop("isSubKey", UNSET)

        _revocation_reason = d.pop("revocationReason", UNSET)
        revocation_reason: KeyRevocationReason | Unset
        if isinstance(_revocation_reason, Unset):
            revocation_reason = UNSET
        else:
            revocation_reason = check_key_revocation_reason(_revocation_reason)

        key = cls(
            identifier=identifier,
            name=name,
            valid_from=valid_from,
            valid_to=valid_to,
            account_identifier=account_identifier,
            parent_identifier=parent_identifier,
            description=description,
            tags=tags,
            key=key,
            key_usage=key_usage,
            key_id=key_id,
            primary_user_id=primary_user_id,
            key_algorithm=key_algorithm,
            key_scheme=key_scheme,
            identities=identities,
            primary_identity=primary_identity,
            parent_key_id=parent_key_id,
            is_sub_key=is_sub_key,
            revocation_reason=revocation_reason,
        )

        key.additional_properties = d
        return key

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
