from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.input_set_summary_response import InputSetSummaryResponse


T = TypeVar("T", bound="BulkInputSetsAPIResponse")


@_attrs_define
class BulkInputSetsAPIResponse:
    """
    Attributes:
        input_sets (list[InputSetSummaryResponse] | Unset):
    """

    input_sets: list[InputSetSummaryResponse] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_sets: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.input_sets, Unset):
            input_sets = []
            for input_sets_item_data in self.input_sets:
                input_sets_item = input_sets_item_data.to_dict()
                input_sets.append(input_sets_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_sets is not UNSET:
            field_dict["inputSets"] = input_sets

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.input_set_summary_response import InputSetSummaryResponse

        d = dict(src_dict)
        _input_sets = d.pop("inputSets", UNSET)
        input_sets: list[InputSetSummaryResponse] | Unset = UNSET
        if _input_sets is not UNSET:
            input_sets = []
            for input_sets_item_data in _input_sets:
                input_sets_item = InputSetSummaryResponse.from_dict(input_sets_item_data)

                input_sets.append(input_sets_item)

        bulk_input_sets_api_response = cls(
            input_sets=input_sets,
        )

        bulk_input_sets_api_response.additional_properties = d
        return bulk_input_sets_api_response

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
