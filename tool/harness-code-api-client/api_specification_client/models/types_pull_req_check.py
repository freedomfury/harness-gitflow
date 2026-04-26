from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_check import TypesCheck


T = TypeVar("T", bound="TypesPullReqCheck")


@_attrs_define
class TypesPullReqCheck:
    """
    Attributes:
        bypassable (bool | Unset):
        check (TypesCheck | Unset):
        required (bool | Unset):
    """

    bypassable: bool | Unset = UNSET
    check: TypesCheck | Unset = UNSET
    required: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bypassable = self.bypassable

        check: dict[str, Any] | Unset = UNSET
        if not isinstance(self.check, Unset):
            check = self.check.to_dict()

        required = self.required

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bypassable is not UNSET:
            field_dict["bypassable"] = bypassable
        if check is not UNSET:
            field_dict["check"] = check
        if required is not UNSET:
            field_dict["required"] = required

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_check import TypesCheck

        d = dict(src_dict)
        bypassable = d.pop("bypassable", UNSET)

        _check = d.pop("check", UNSET)
        check: TypesCheck | Unset
        if isinstance(_check, Unset):
            check = UNSET
        else:
            check = TypesCheck.from_dict(_check)

        required = d.pop("required", UNSET)

        types_pull_req_check = cls(
            bypassable=bypassable,
            check=check,
            required=required,
        )

        types_pull_req_check.additional_properties = d
        return types_pull_req_check

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
