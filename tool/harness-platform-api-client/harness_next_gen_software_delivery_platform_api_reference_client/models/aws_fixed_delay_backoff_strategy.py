from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwsFixedDelayBackoffStrategy")


@_attrs_define
class AwsFixedDelayBackoffStrategy:
    """Simple backoff strategy that always uses a fixed delay for the delay before the next retry attempt.

    Attributes:
        fixed_backoff (int | Unset):
        retry_count (int | Unset):
    """

    fixed_backoff: int | Unset = UNSET
    retry_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fixed_backoff = self.fixed_backoff

        retry_count = self.retry_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if fixed_backoff is not UNSET:
            field_dict["fixedBackoff"] = fixed_backoff
        if retry_count is not UNSET:
            field_dict["retryCount"] = retry_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fixed_backoff = d.pop("fixedBackoff", UNSET)

        retry_count = d.pop("retryCount", UNSET)

        aws_fixed_delay_backoff_strategy = cls(
            fixed_backoff=fixed_backoff,
            retry_count=retry_count,
        )

        aws_fixed_delay_backoff_strategy.additional_properties = d
        return aws_fixed_delay_backoff_strategy

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
