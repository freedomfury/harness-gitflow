from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.infrastructure_request_type import InfrastructureRequestType, check_infrastructure_request_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.infrastructure_request_tags import InfrastructureRequestTags


T = TypeVar("T", bound="InfrastructureRequest")


@_attrs_define
class InfrastructureRequest:
    """This is the InfrastructureRequest entity defined in Harness

    Attributes:
        yaml (str): yaml spec of the infrastructure. Just yaml alone is sufficient to create an infrastructure.
        identifier (str | Unset): identifier of the infrastructure
        org_identifier (str | Unset): organisation identifier of the infrastructure
        project_identifier (str | Unset): project identifier of the infrastructure
        environment_ref (str | Unset): environment reference of the infrastructure
        name (str | Unset): name of the infrastructure
        description (str | Unset): description of the infrastructure
        tags (InfrastructureRequestTags | Unset): tags associated with the infrastructure
        type_ (InfrastructureRequestType | Unset): type of the infrastructure
    """

    yaml: str
    identifier: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    environment_ref: str | Unset = UNSET
    name: str | Unset = UNSET
    description: str | Unset = UNSET
    tags: InfrastructureRequestTags | Unset = UNSET
    type_: InfrastructureRequestType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        yaml = self.yaml

        identifier = self.identifier

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        environment_ref = self.environment_ref

        name = self.name

        description = self.description

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "yaml": yaml,
            }
        )
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if environment_ref is not UNSET:
            field_dict["environmentRef"] = environment_ref
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.infrastructure_request_tags import InfrastructureRequestTags

        d = dict(src_dict)
        yaml = d.pop("yaml")

        identifier = d.pop("identifier", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        environment_ref = d.pop("environmentRef", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: InfrastructureRequestTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = InfrastructureRequestTags.from_dict(_tags)

        _type_ = d.pop("type", UNSET)
        type_: InfrastructureRequestType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_infrastructure_request_type(_type_)

        infrastructure_request = cls(
            yaml=yaml,
            identifier=identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            environment_ref=environment_ref,
            name=name,
            description=description,
            tags=tags,
            type_=type_,
        )

        infrastructure_request.additional_properties = d
        return infrastructure_request

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
