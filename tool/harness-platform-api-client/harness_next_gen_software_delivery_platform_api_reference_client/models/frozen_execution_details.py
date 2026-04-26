from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.frozen_execution_detail import FrozenExecutionDetail


T = TypeVar("T", bound="FrozenExecutionDetails")


@_attrs_define
class FrozenExecutionDetails:
    """
    Attributes:
        freeze_list (list[FrozenExecutionDetail] | Unset):
    """

    freeze_list: list[FrozenExecutionDetail] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        freeze_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.freeze_list, Unset):
            freeze_list = []
            for freeze_list_item_data in self.freeze_list:
                freeze_list_item = freeze_list_item_data.to_dict()
                freeze_list.append(freeze_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if freeze_list is not UNSET:
            field_dict["freezeList"] = freeze_list

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.frozen_execution_detail import FrozenExecutionDetail

        d = dict(src_dict)
        _freeze_list = d.pop("freezeList", UNSET)
        freeze_list: list[FrozenExecutionDetail] | Unset = UNSET
        if _freeze_list is not UNSET:
            freeze_list = []
            for freeze_list_item_data in _freeze_list:
                freeze_list_item = FrozenExecutionDetail.from_dict(freeze_list_item_data)

                freeze_list.append(freeze_list_item)

        frozen_execution_details = cls(
            freeze_list=freeze_list,
        )

        frozen_execution_details.additional_properties = d
        return frozen_execution_details

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
