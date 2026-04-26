from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NameValuePairWithDefault")


@_attrs_define
class NameValuePairWithDefault:
    """
    Attributes:
        name (str):
        value (str):
        type_ (str):
        use_as_default (bool | Unset):
    """

    name: str
    value: str
    type_: str
    use_as_default: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        value = self.value

        type_ = self.type_

        use_as_default = self.use_as_default

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "value": value,
                "type": type_,
            }
        )
        if use_as_default is not UNSET:
            field_dict["useAsDefault"] = use_as_default

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        value = d.pop("value")

        type_ = d.pop("type")

        use_as_default = d.pop("useAsDefault", UNSET)

        name_value_pair_with_default = cls(
            name=name,
            value=value,
            type_=type_,
            use_as_default=use_as_default,
        )

        name_value_pair_with_default.additional_properties = d
        return name_value_pair_with_default

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
