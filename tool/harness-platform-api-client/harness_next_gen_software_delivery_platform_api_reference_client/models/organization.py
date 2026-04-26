from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.organization_tags import OrganizationTags


T = TypeVar("T", bound="Organization")


@_attrs_define
class Organization:
    """This has details of the Organization as defined in Harness.

    Attributes:
        identifier (str | Unset): Identifier of the Organization
        name (str | Unset): Name of the Organization
        description (str | Unset): Description of the Organization.
        tags (OrganizationTags | Unset): Tags for the Organization.
    """

    identifier: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    tags: OrganizationTags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        name = self.name

        description = self.description

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.organization_tags import OrganizationTags

        d = dict(src_dict)
        identifier = d.pop("identifier", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: OrganizationTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = OrganizationTags.from_dict(_tags)

        organization = cls(
            identifier=identifier,
            name=name,
            description=description,
            tags=tags,
        )

        organization.additional_properties = d
        return organization

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
