from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.governance_metadata import GovernanceMetadata
    from ..models.secret import Secret


T = TypeVar("T", bound="SecretResponse")


@_attrs_define
class SecretResponse:
    """This has details of the Secret along with its metadata.

    Attributes:
        secret (Secret): This is details of the secret entity defined in Harness.
        created_at (int | Unset): This is the time at which the Secret was created.
        updated_at (int | Unset): This is the time at which the Secret was last updated.
        draft (bool | Unset):
        governance_metadata (GovernanceMetadata | Unset): GovernanceMetadata for OPA evaluation
    """

    secret: Secret
    created_at: int | Unset = UNSET
    updated_at: int | Unset = UNSET
    draft: bool | Unset = UNSET
    governance_metadata: GovernanceMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret = self.secret.to_dict()

        created_at = self.created_at

        updated_at = self.updated_at

        draft = self.draft

        governance_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.governance_metadata, Unset):
            governance_metadata = self.governance_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "secret": secret,
            }
        )
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if updated_at is not UNSET:
            field_dict["updatedAt"] = updated_at
        if draft is not UNSET:
            field_dict["draft"] = draft
        if governance_metadata is not UNSET:
            field_dict["governanceMetadata"] = governance_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.governance_metadata import GovernanceMetadata
        from ..models.secret import Secret

        d = dict(src_dict)
        secret = Secret.from_dict(d.pop("secret"))

        created_at = d.pop("createdAt", UNSET)

        updated_at = d.pop("updatedAt", UNSET)

        draft = d.pop("draft", UNSET)

        _governance_metadata = d.pop("governanceMetadata", UNSET)
        governance_metadata: GovernanceMetadata | Unset
        if isinstance(_governance_metadata, Unset):
            governance_metadata = UNSET
        else:
            governance_metadata = GovernanceMetadata.from_dict(_governance_metadata)

        secret_response = cls(
            secret=secret,
            created_at=created_at,
            updated_at=updated_at,
            draft=draft,
            governance_metadata=governance_metadata,
        )

        secret_response.additional_properties = d
        return secret_response

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
