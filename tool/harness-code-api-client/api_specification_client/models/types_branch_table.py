from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesBranchTable")


@_attrs_define
class TypesBranchTable:
    """
    Attributes:
        created (int | Unset):
        created_by (int | Unset):
        last_created_pull_req_id (int | None | Unset):
        name (str | Unset):
        updated (int | Unset):
        updated_by (int | Unset):
    """

    created: int | Unset = UNSET
    created_by: int | Unset = UNSET
    last_created_pull_req_id: int | None | Unset = UNSET
    name: str | Unset = UNSET
    updated: int | Unset = UNSET
    updated_by: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        created_by = self.created_by

        last_created_pull_req_id: int | None | Unset
        if isinstance(self.last_created_pull_req_id, Unset):
            last_created_pull_req_id = UNSET
        else:
            last_created_pull_req_id = self.last_created_pull_req_id

        name = self.name

        updated = self.updated

        updated_by = self.updated_by

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if last_created_pull_req_id is not UNSET:
            field_dict["last_created_pull_req_id"] = last_created_pull_req_id
        if name is not UNSET:
            field_dict["name"] = name
        if updated is not UNSET:
            field_dict["updated"] = updated
        if updated_by is not UNSET:
            field_dict["updated_by"] = updated_by

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        created = d.pop("created", UNSET)

        created_by = d.pop("created_by", UNSET)

        def _parse_last_created_pull_req_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        last_created_pull_req_id = _parse_last_created_pull_req_id(d.pop("last_created_pull_req_id", UNSET))

        name = d.pop("name", UNSET)

        updated = d.pop("updated", UNSET)

        updated_by = d.pop("updated_by", UNSET)

        types_branch_table = cls(
            created=created,
            created_by=created_by,
            last_created_pull_req_id=last_created_pull_req_id,
            name=name,
            updated=updated,
            updated_by=updated_by,
        )

        types_branch_table.additional_properties = d
        return types_branch_table

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
