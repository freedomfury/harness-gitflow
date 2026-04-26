from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.protection_repo_target_filter import ProtectionRepoTargetFilter


T = TypeVar("T", bound="ProtectionRepoTargetType0")


@_attrs_define
class ProtectionRepoTargetType0:
    """
    Attributes:
        exclude (ProtectionRepoTargetFilter | Unset):
        include (ProtectionRepoTargetFilter | Unset):
    """

    exclude: ProtectionRepoTargetFilter | Unset = UNSET
    include: ProtectionRepoTargetFilter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        exclude: dict[str, Any] | Unset = UNSET
        if not isinstance(self.exclude, Unset):
            exclude = self.exclude.to_dict()

        include: dict[str, Any] | Unset = UNSET
        if not isinstance(self.include, Unset):
            include = self.include.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if exclude is not UNSET:
            field_dict["exclude"] = exclude
        if include is not UNSET:
            field_dict["include"] = include

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.protection_repo_target_filter import ProtectionRepoTargetFilter

        d = dict(src_dict)
        _exclude = d.pop("exclude", UNSET)
        exclude: ProtectionRepoTargetFilter | Unset
        if isinstance(_exclude, Unset):
            exclude = UNSET
        else:
            exclude = ProtectionRepoTargetFilter.from_dict(_exclude)

        _include = d.pop("include", UNSET)
        include: ProtectionRepoTargetFilter | Unset
        if isinstance(_include, Unset):
            include = UNSET
        else:
            include = ProtectionRepoTargetFilter.from_dict(_include)

        protection_repo_target_type_0 = cls(
            exclude=exclude,
            include=include,
        )

        protection_repo_target_type_0.additional_properties = d
        return protection_repo_target_type_0

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
