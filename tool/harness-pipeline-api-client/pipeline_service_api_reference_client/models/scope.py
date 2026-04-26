from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Scope")


@_attrs_define
class Scope:
    """
    Attributes:
        account_identifier (str):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        parent_unique_id (str | Unset):
    """

    account_identifier: str
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    parent_unique_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_identifier = self.account_identifier

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        parent_unique_id = self.parent_unique_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountIdentifier": account_identifier,
            }
        )
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if parent_unique_id is not UNSET:
            field_dict["parentUniqueId"] = parent_unique_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_identifier = d.pop("accountIdentifier")

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        parent_unique_id = d.pop("parentUniqueId", UNSET)

        scope = cls(
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            parent_unique_id=parent_unique_id,
        )

        scope.additional_properties = d
        return scope

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
