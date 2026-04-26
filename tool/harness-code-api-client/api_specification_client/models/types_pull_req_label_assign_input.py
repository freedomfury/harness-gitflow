from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesPullReqLabelAssignInput")


@_attrs_define
class TypesPullReqLabelAssignInput:
    """
    Attributes:
        label_id (int | Unset):
        value (str | Unset):
        value_id (int | None | Unset):
    """

    label_id: int | Unset = UNSET
    value: str | Unset = UNSET
    value_id: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        label_id = self.label_id

        value = self.value

        value_id: int | None | Unset
        if isinstance(self.value_id, Unset):
            value_id = UNSET
        else:
            value_id = self.value_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if label_id is not UNSET:
            field_dict["label_id"] = label_id
        if value is not UNSET:
            field_dict["value"] = value
        if value_id is not UNSET:
            field_dict["value_id"] = value_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        label_id = d.pop("label_id", UNSET)

        value = d.pop("value", UNSET)

        def _parse_value_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        value_id = _parse_value_id(d.pop("value_id", UNSET))

        types_pull_req_label_assign_input = cls(
            label_id=label_id,
            value=value,
            value_id=value_id,
        )

        types_pull_req_label_assign_input.additional_properties = d
        return types_pull_req_label_assign_input

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
