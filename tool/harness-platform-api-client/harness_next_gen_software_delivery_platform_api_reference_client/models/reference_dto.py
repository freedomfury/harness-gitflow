from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReferenceDTO")


@_attrs_define
class ReferenceDTO:
    """
    Attributes:
        name (str | Unset):
        display_name (str | Unset):
        identifier (str | Unset):
        project_identifier (str | Unset):
        org_identifier (str | Unset):
        account_identifier (str | Unset):
        count (int | Unset):
    """

    name: str | Unset = UNSET
    display_name: str | Unset = UNSET
    identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    account_identifier: str | Unset = UNSET
    count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        display_name = self.display_name

        identifier = self.identifier

        project_identifier = self.project_identifier

        org_identifier = self.org_identifier

        account_identifier = self.account_identifier

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if count is not UNSET:
            field_dict["count"] = count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        identifier = d.pop("identifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        account_identifier = d.pop("accountIdentifier", UNSET)

        count = d.pop("count", UNSET)

        reference_dto = cls(
            name=name,
            display_name=display_name,
            identifier=identifier,
            project_identifier=project_identifier,
            org_identifier=org_identifier,
            account_identifier=account_identifier,
            count=count,
        )

        reference_dto.additional_properties = d
        return reference_dto

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
