from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.usererror_error_values import UsererrorErrorValues


T = TypeVar("T", bound="UsererrorError")


@_attrs_define
class UsererrorError:
    """
    Attributes:
        message (str | Unset):
        values (UsererrorErrorValues | Unset):
    """

    message: str | Unset = UNSET
    values: UsererrorErrorValues | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        message = self.message

        values: dict[str, Any] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = self.values.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if values is not UNSET:
            field_dict["values"] = values

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.usererror_error_values import UsererrorErrorValues

        d = dict(src_dict)
        message = d.pop("message", UNSET)

        _values = d.pop("values", UNSET)
        values: UsererrorErrorValues | Unset
        if isinstance(_values, Unset):
            values = UNSET
        else:
            values = UsererrorErrorValues.from_dict(_values)

        usererror_error = cls(
            message=message,
            values=values,
        )

        usererror_error.additional_properties = d
        return usererror_error

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
