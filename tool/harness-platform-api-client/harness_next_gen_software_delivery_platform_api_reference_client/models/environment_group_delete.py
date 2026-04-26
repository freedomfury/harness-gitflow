from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EnvironmentGroupDelete")


@_attrs_define
class EnvironmentGroupDelete:
    """This is the view of Environment Group Delete Response defined in Harness

    Attributes:
        deleted (bool | Unset): Value true, when the Entity is deleted
        account_id (str | Unset): Account Identifier for the Entity.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        identifier (str | Unset): Identifier for the Entity.
    """

    deleted: bool | Unset = UNSET
    account_id: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleted = self.deleted

        account_id = self.account_id

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        identifier = self.identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if identifier is not UNSET:
            field_dict["identifier"] = identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deleted = d.pop("deleted", UNSET)

        account_id = d.pop("accountId", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        identifier = d.pop("identifier", UNSET)

        environment_group_delete = cls(
            deleted=deleted,
            account_id=account_id,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            identifier=identifier,
        )

        environment_group_delete.additional_properties = d
        return environment_group_delete

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
