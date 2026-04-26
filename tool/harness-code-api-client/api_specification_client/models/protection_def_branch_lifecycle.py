from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProtectionDefBranchLifecycle")


@_attrs_define
class ProtectionDefBranchLifecycle:
    """
    Attributes:
        create_forbidden (bool | Unset):
        delete_forbidden (bool | Unset):
        update_forbidden (bool | Unset):
        update_force_forbidden (bool | Unset):
    """

    create_forbidden: bool | Unset = UNSET
    delete_forbidden: bool | Unset = UNSET
    update_forbidden: bool | Unset = UNSET
    update_force_forbidden: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_forbidden = self.create_forbidden

        delete_forbidden = self.delete_forbidden

        update_forbidden = self.update_forbidden

        update_force_forbidden = self.update_force_forbidden

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_forbidden is not UNSET:
            field_dict["create_forbidden"] = create_forbidden
        if delete_forbidden is not UNSET:
            field_dict["delete_forbidden"] = delete_forbidden
        if update_forbidden is not UNSET:
            field_dict["update_forbidden"] = update_forbidden
        if update_force_forbidden is not UNSET:
            field_dict["update_force_forbidden"] = update_force_forbidden

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        create_forbidden = d.pop("create_forbidden", UNSET)

        delete_forbidden = d.pop("delete_forbidden", UNSET)

        update_forbidden = d.pop("update_forbidden", UNSET)

        update_force_forbidden = d.pop("update_force_forbidden", UNSET)

        protection_def_branch_lifecycle = cls(
            create_forbidden=create_forbidden,
            delete_forbidden=delete_forbidden,
            update_forbidden=update_forbidden,
            update_force_forbidden=update_force_forbidden,
        )

        protection_def_branch_lifecycle.additional_properties = d
        return protection_def_branch_lifecycle

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
