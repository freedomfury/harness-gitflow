from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ScopeName")


@_attrs_define
class ScopeName:
    """
    Attributes:
        account_identifier (str | Unset):
        org_name (str | Unset):
        org_identifier (str | Unset):
        project_name (str | Unset):
        project_identifier (str | Unset):
    """

    account_identifier: str | Unset = UNSET
    org_name: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_name: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_identifier = self.account_identifier

        org_name = self.org_name

        org_identifier = self.org_identifier

        project_name = self.project_name

        project_identifier = self.project_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if org_name is not UNSET:
            field_dict["orgName"] = org_name
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_name is not UNSET:
            field_dict["projectName"] = project_name
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_identifier = d.pop("accountIdentifier", UNSET)

        org_name = d.pop("orgName", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_name = d.pop("projectName", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        scope_name = cls(
            account_identifier=account_identifier,
            org_name=org_name,
            org_identifier=org_identifier,
            project_name=project_name,
            project_identifier=project_identifier,
        )

        scope_name.additional_properties = d
        return scope_name

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
