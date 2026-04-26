from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceOverrideRequest")


@_attrs_define
class ServiceOverrideRequest:
    """This is the Service Override Request entity defined in Harness

    Attributes:
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        environment_identifier (str | Unset): Environment Identifier for the Entity.
        service_identifier (str | Unset): Service Identifier for the Entity.
        yaml (str | Unset): Yaml for the Service Override entity
    """

    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    environment_identifier: str | Unset = UNSET
    service_identifier: str | Unset = UNSET
    yaml: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        environment_identifier = self.environment_identifier

        service_identifier = self.service_identifier

        yaml = self.yaml

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if environment_identifier is not UNSET:
            field_dict["environmentIdentifier"] = environment_identifier
        if service_identifier is not UNSET:
            field_dict["serviceIdentifier"] = service_identifier
        if yaml is not UNSET:
            field_dict["yaml"] = yaml

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        environment_identifier = d.pop("environmentIdentifier", UNSET)

        service_identifier = d.pop("serviceIdentifier", UNSET)

        yaml = d.pop("yaml", UNSET)

        service_override_request = cls(
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            environment_identifier=environment_identifier,
            service_identifier=service_identifier,
            yaml=yaml,
        )

        service_override_request.additional_properties = d
        return service_override_request

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
