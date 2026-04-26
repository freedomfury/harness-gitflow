from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.entity_detail_type import EntityDetailType, check_entity_detail_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_git_metadata import EntityGitMetadata
    from ..models.entity_reference import EntityReference


T = TypeVar("T", bound="EntityDetail")


@_attrs_define
class EntityDetail:
    """
    Attributes:
        type_ (EntityDetailType | Unset):
        entity_ref (EntityReference | Unset):
        name (str | Unset):
        entity_git_metadata (EntityGitMetadata | Unset):
    """

    type_: EntityDetailType | Unset = UNSET
    entity_ref: EntityReference | Unset = UNSET
    name: str | Unset = UNSET
    entity_git_metadata: EntityGitMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        entity_ref: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity_ref, Unset):
            entity_ref = self.entity_ref.to_dict()

        name = self.name

        entity_git_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity_git_metadata, Unset):
            entity_git_metadata = self.entity_git_metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type_ is not UNSET:
            field_dict["type"] = type_
        if entity_ref is not UNSET:
            field_dict["entityRef"] = entity_ref
        if name is not UNSET:
            field_dict["name"] = name
        if entity_git_metadata is not UNSET:
            field_dict["entityGitMetadata"] = entity_git_metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_git_metadata import EntityGitMetadata
        from ..models.entity_reference import EntityReference

        d = dict(src_dict)
        _type_ = d.pop("type", UNSET)
        type_: EntityDetailType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_entity_detail_type(_type_)

        _entity_ref = d.pop("entityRef", UNSET)
        entity_ref: EntityReference | Unset
        if isinstance(_entity_ref, Unset):
            entity_ref = UNSET
        else:
            entity_ref = EntityReference.from_dict(_entity_ref)

        name = d.pop("name", UNSET)

        _entity_git_metadata = d.pop("entityGitMetadata", UNSET)
        entity_git_metadata: EntityGitMetadata | Unset
        if isinstance(_entity_git_metadata, Unset):
            entity_git_metadata = UNSET
        else:
            entity_git_metadata = EntityGitMetadata.from_dict(_entity_git_metadata)

        entity_detail = cls(
            type_=type_,
            entity_ref=entity_ref,
            name=name,
            entity_git_metadata=entity_git_metadata,
        )

        entity_detail.additional_properties = d
        return entity_detail

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
