from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnvironmentGroupRequest")


@_attrs_define
class EnvironmentGroupRequest:
    """This is the EnvironmentGroupRequest entity defined in Harness

    Attributes:
        yaml (str): Yaml of the Environment Group.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        identifier (str | Unset): Identifier of the Environment Group.
        color (str | Unset): Color of the Environment Group.
    """

    yaml: str
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    identifier: str | Unset = UNSET
    color: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        yaml = self.yaml

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        identifier = self.identifier

        color = self.color

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "yaml": yaml,
            }
        )
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if color is not UNSET:
            field_dict["color"] = color

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        yaml = d.pop("yaml")

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        identifier = d.pop("identifier", UNSET)

        color = d.pop("color", UNSET)

        environment_group_request = cls(
            yaml=yaml,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            identifier=identifier,
            color=color,
        )

        environment_group_request.additional_properties = d
        return environment_group_request

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
