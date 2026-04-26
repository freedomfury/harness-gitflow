from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="TriggerIssuer")


@_attrs_define
class TriggerIssuer:
    """
    Attributes:
        trigger_ref (str):
        abort_prev_concurrent_execution (bool):
    """

    trigger_ref: str
    abort_prev_concurrent_execution: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trigger_ref = self.trigger_ref

        abort_prev_concurrent_execution = self.abort_prev_concurrent_execution

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "triggerRef": trigger_ref,
                "abortPrevConcurrentExecution": abort_prev_concurrent_execution,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trigger_ref = d.pop("triggerRef")

        abort_prev_concurrent_execution = d.pop("abortPrevConcurrentExecution")

        trigger_issuer = cls(
            trigger_ref=trigger_ref,
            abort_prev_concurrent_execution=abort_prev_concurrent_execution,
        )

        trigger_issuer.additional_properties = d
        return trigger_issuer

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
