from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.service_request_tags import ServiceRequestTags


T = TypeVar("T", bound="ServiceRequest")


@_attrs_define
class ServiceRequest:
    """Service Request details defined in Harness.

    Attributes:
        identifier (str | Unset): Identifier of the Service Request.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        name (str | Unset): Name of the Service Request.
        description (str | Unset): Description of the entity
        tags (ServiceRequestTags | Unset): Tags
        yaml (str | Unset): YAML for the Service Request
    """

    identifier: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    tags: ServiceRequestTags | Unset = UNSET
    yaml: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        name = self.name

        description = self.description

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        yaml = self.yaml

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if yaml is not UNSET:
            field_dict["yaml"] = yaml

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.service_request_tags import ServiceRequestTags

        d = dict(src_dict)
        identifier = d.pop("identifier", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: ServiceRequestTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = ServiceRequestTags.from_dict(_tags)

        yaml = d.pop("yaml", UNSET)

        service_request = cls(
            identifier=identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            name=name,
            description=description,
            tags=tags,
            yaml=yaml,
        )

        service_request.additional_properties = d
        return service_request

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
