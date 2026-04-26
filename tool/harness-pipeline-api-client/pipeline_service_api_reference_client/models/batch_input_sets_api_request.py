from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BatchInputSetsAPIRequest")


@_attrs_define
class BatchInputSetsAPIRequest:
    """
    Attributes:
        pipeline_identifiers (list[str] | Unset):
    """

    pipeline_identifiers: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        pipeline_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.pipeline_identifiers, Unset):
            pipeline_identifiers = self.pipeline_identifiers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if pipeline_identifiers is not UNSET:
            field_dict["pipelineIdentifiers"] = pipeline_identifiers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        pipeline_identifiers = cast(list[str], d.pop("pipelineIdentifiers", UNSET))

        batch_input_sets_api_request = cls(
            pipeline_identifiers=pipeline_identifiers,
        )

        batch_input_sets_api_request.additional_properties = d
        return batch_input_sets_api_request

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
