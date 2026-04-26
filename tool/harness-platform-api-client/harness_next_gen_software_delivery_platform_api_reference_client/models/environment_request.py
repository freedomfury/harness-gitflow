from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.environment_request_type import EnvironmentRequestType, check_environment_request_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.environment_request_tags import EnvironmentRequestTags


T = TypeVar("T", bound="EnvironmentRequest")


@_attrs_define
class EnvironmentRequest:
    """This is the Environment entity defined in Harness

    Attributes:
        type_ (EnvironmentRequestType): Specify the environment type whether production or Preproduction.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        identifier (str | Unset): Identifier of the Environment.
        tags (EnvironmentRequestTags | Unset): Tags
        name (str | Unset): Name of the Environment.
        description (str | Unset): Description of the entity
        color (str | Unset): Color of the Environment.
        yaml (str | Unset): Yaml of this entity.
    """

    type_: EnvironmentRequestType
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    identifier: str | Unset = UNSET
    tags: EnvironmentRequestTags | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    color: str | Unset = UNSET
    yaml: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        identifier = self.identifier

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        name = self.name

        description = self.description

        color = self.color

        yaml = self.yaml

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if tags is not UNSET:
            field_dict["tags"] = tags
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if color is not UNSET:
            field_dict["color"] = color
        if yaml is not UNSET:
            field_dict["yaml"] = yaml

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.environment_request_tags import EnvironmentRequestTags

        d = dict(src_dict)
        type_ = check_environment_request_type(d.pop("type"))

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        identifier = d.pop("identifier", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: EnvironmentRequestTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = EnvironmentRequestTags.from_dict(_tags)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        color = d.pop("color", UNSET)

        yaml = d.pop("yaml", UNSET)

        environment_request = cls(
            type_=type_,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            identifier=identifier,
            tags=tags,
            name=name,
            description=description,
            color=color,
            yaml=yaml,
        )

        environment_request.additional_properties = d
        return environment_request

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
