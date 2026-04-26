from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.entity_reference_scope import EntityReferenceScope, check_entity_reference_scope
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_reference_metadata import EntityReferenceMetadata


T = TypeVar("T", bound="EntityReference")


@_attrs_define
class EntityReference:
    """
    Attributes:
        parent_unique_id (str | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        branch (str | Unset):
        default (bool | Unset):
        metadata (EntityReferenceMetadata | Unset):
        repo_identifier (str | Unset):
        is_default (bool | Unset):
        scope (EntityReferenceScope | Unset):
        identifier (str | Unset):
        account_identifier (str | Unset):
    """

    parent_unique_id: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    branch: str | Unset = UNSET
    default: bool | Unset = UNSET
    metadata: EntityReferenceMetadata | Unset = UNSET
    repo_identifier: str | Unset = UNSET
    is_default: bool | Unset = UNSET
    scope: EntityReferenceScope | Unset = UNSET
    identifier: str | Unset = UNSET
    account_identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_unique_id = self.parent_unique_id

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        branch = self.branch

        default = self.default

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        repo_identifier = self.repo_identifier

        is_default = self.is_default

        scope: str | Unset = UNSET
        if not isinstance(self.scope, Unset):
            scope = self.scope

        identifier = self.identifier

        account_identifier = self.account_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parent_unique_id is not UNSET:
            field_dict["parentUniqueId"] = parent_unique_id
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if branch is not UNSET:
            field_dict["branch"] = branch
        if default is not UNSET:
            field_dict["default"] = default
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if repo_identifier is not UNSET:
            field_dict["repoIdentifier"] = repo_identifier
        if is_default is not UNSET:
            field_dict["isDefault"] = is_default
        if scope is not UNSET:
            field_dict["scope"] = scope
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_reference_metadata import EntityReferenceMetadata

        d = dict(src_dict)
        parent_unique_id = d.pop("parentUniqueId", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        branch = d.pop("branch", UNSET)

        default = d.pop("default", UNSET)

        _metadata = d.pop("metadata", UNSET)
        metadata: EntityReferenceMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = EntityReferenceMetadata.from_dict(_metadata)

        repo_identifier = d.pop("repoIdentifier", UNSET)

        is_default = d.pop("isDefault", UNSET)

        _scope = d.pop("scope", UNSET)
        scope: EntityReferenceScope | Unset
        if isinstance(_scope, Unset):
            scope = UNSET
        else:
            scope = check_entity_reference_scope(_scope)

        identifier = d.pop("identifier", UNSET)

        account_identifier = d.pop("accountIdentifier", UNSET)

        entity_reference = cls(
            parent_unique_id=parent_unique_id,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            branch=branch,
            default=default,
            metadata=metadata,
            repo_identifier=repo_identifier,
            is_default=is_default,
            scope=scope,
            identifier=identifier,
            account_identifier=account_identifier,
        )

        entity_reference.additional_properties = d
        return entity_reference

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
