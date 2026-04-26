from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.project_modules_item import ProjectModulesItem, check_project_modules_item
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.project_tags import ProjectTags


T = TypeVar("T", bound="Project")


@_attrs_define
class Project:
    """This is the Project Entity details defined in Harness

    Attributes:
        org_identifier (str | Unset): Organization Identifier for the Entity.
        identifier (str | Unset): Project Identifier for the Entity.
        name (str | Unset): Project Name for the entity
        color (str | Unset): Color
        modules (list[ProjectModulesItem] | Unset): List of modules
        description (str | Unset): Description
        tags (ProjectTags | Unset): Tags
    """

    org_identifier: str | Unset = UNSET
    identifier: str | Unset = UNSET
    name: str | Unset = UNSET
    color: str | Unset = UNSET
    modules: list[ProjectModulesItem] | Unset = UNSET
    description: str | Unset = UNSET
    tags: ProjectTags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_identifier = self.org_identifier

        identifier = self.identifier

        name = self.name

        color = self.color

        modules: list[str] | Unset = UNSET
        if not isinstance(self.modules, Unset):
            modules = []
            for modules_item_data in self.modules:
                modules_item: str = modules_item_data
                modules.append(modules_item)

        description = self.description

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if name is not UNSET:
            field_dict["name"] = name
        if color is not UNSET:
            field_dict["color"] = color
        if modules is not UNSET:
            field_dict["modules"] = modules
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.project_tags import ProjectTags

        d = dict(src_dict)
        org_identifier = d.pop("orgIdentifier", UNSET)

        identifier = d.pop("identifier", UNSET)

        name = d.pop("name", UNSET)

        color = d.pop("color", UNSET)

        _modules = d.pop("modules", UNSET)
        modules: list[ProjectModulesItem] | Unset = UNSET
        if _modules is not UNSET:
            modules = []
            for modules_item_data in _modules:
                modules_item = check_project_modules_item(modules_item_data)

                modules.append(modules_item)

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: ProjectTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = ProjectTags.from_dict(_tags)

        project = cls(
            org_identifier=org_identifier,
            identifier=identifier,
            name=name,
            color=color,
            modules=modules,
            description=description,
            tags=tags,
        )

        project.additional_properties = d
        return project

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
