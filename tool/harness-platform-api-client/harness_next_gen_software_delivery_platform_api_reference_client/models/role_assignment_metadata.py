from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RoleAssignmentMetadata")


@_attrs_define
class RoleAssignmentMetadata:
    """This has information of Role like name, id, resource group name, etc.

    Attributes:
        identifier (str | Unset):
        role_identifier (str | Unset):
        role_name (str | Unset):
        role_scope_level (str | Unset):
        resource_group_identifier (str | Unset):
        resource_group_name (str | Unset):
        managed_role (bool | Unset):
        managed_role_assignment (bool | Unset):
    """

    identifier: str | Unset = UNSET
    role_identifier: str | Unset = UNSET
    role_name: str | Unset = UNSET
    role_scope_level: str | Unset = UNSET
    resource_group_identifier: str | Unset = UNSET
    resource_group_name: str | Unset = UNSET
    managed_role: bool | Unset = UNSET
    managed_role_assignment: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        role_identifier = self.role_identifier

        role_name = self.role_name

        role_scope_level = self.role_scope_level

        resource_group_identifier = self.resource_group_identifier

        resource_group_name = self.resource_group_name

        managed_role = self.managed_role

        managed_role_assignment = self.managed_role_assignment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if role_identifier is not UNSET:
            field_dict["roleIdentifier"] = role_identifier
        if role_name is not UNSET:
            field_dict["roleName"] = role_name
        if role_scope_level is not UNSET:
            field_dict["roleScopeLevel"] = role_scope_level
        if resource_group_identifier is not UNSET:
            field_dict["resourceGroupIdentifier"] = resource_group_identifier
        if resource_group_name is not UNSET:
            field_dict["resourceGroupName"] = resource_group_name
        if managed_role is not UNSET:
            field_dict["managedRole"] = managed_role
        if managed_role_assignment is not UNSET:
            field_dict["managedRoleAssignment"] = managed_role_assignment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = d.pop("identifier", UNSET)

        role_identifier = d.pop("roleIdentifier", UNSET)

        role_name = d.pop("roleName", UNSET)

        role_scope_level = d.pop("roleScopeLevel", UNSET)

        resource_group_identifier = d.pop("resourceGroupIdentifier", UNSET)

        resource_group_name = d.pop("resourceGroupName", UNSET)

        managed_role = d.pop("managedRole", UNSET)

        managed_role_assignment = d.pop("managedRoleAssignment", UNSET)

        role_assignment_metadata = cls(
            identifier=identifier,
            role_identifier=role_identifier,
            role_name=role_name,
            role_scope_level=role_scope_level,
            resource_group_identifier=resource_group_identifier,
            resource_group_name=resource_group_name,
            managed_role=managed_role,
            managed_role_assignment=managed_role_assignment,
        )

        role_assignment_metadata.additional_properties = d
        return role_assignment_metadata

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
