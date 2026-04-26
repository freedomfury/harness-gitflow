from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesForkSyncConflict")


@_attrs_define
class TypesForkSyncConflict:
    """
    Attributes:
        conflict_files (list[str] | None | Unset):
        message (str | Unset):
    """

    conflict_files: list[str] | None | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        conflict_files: list[str] | None | Unset
        if isinstance(self.conflict_files, Unset):
            conflict_files = UNSET
        elif isinstance(self.conflict_files, list):
            conflict_files = self.conflict_files

        else:
            conflict_files = self.conflict_files

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if conflict_files is not UNSET:
            field_dict["conflict_files"] = conflict_files
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_conflict_files(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                conflict_files_type_0 = cast(list[str], data)

                return conflict_files_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        conflict_files = _parse_conflict_files(d.pop("conflict_files", UNSET))

        message = d.pop("message", UNSET)

        types_fork_sync_conflict = cls(
            conflict_files=conflict_files,
            message=message,
        )

        types_fork_sync_conflict.additional_properties = d
        return types_fork_sync_conflict

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
