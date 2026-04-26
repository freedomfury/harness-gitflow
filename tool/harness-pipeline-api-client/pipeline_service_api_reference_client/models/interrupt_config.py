from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.issued_by import IssuedBy
    from ..models.retry_interrupt_config import RetryInterruptConfig


T = TypeVar("T", bound="InterruptConfig")


@_attrs_define
class InterruptConfig:
    """
    Attributes:
        issued_by (IssuedBy):
        retry_interrupt_config (RetryInterruptConfig | Unset):
    """

    issued_by: IssuedBy
    retry_interrupt_config: RetryInterruptConfig | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        issued_by = self.issued_by.to_dict()

        retry_interrupt_config: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retry_interrupt_config, Unset):
            retry_interrupt_config = self.retry_interrupt_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issuedBy": issued_by,
            }
        )
        if retry_interrupt_config is not UNSET:
            field_dict["retryInterruptConfig"] = retry_interrupt_config

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.issued_by import IssuedBy
        from ..models.retry_interrupt_config import RetryInterruptConfig

        d = dict(src_dict)
        issued_by = IssuedBy.from_dict(d.pop("issuedBy"))

        _retry_interrupt_config = d.pop("retryInterruptConfig", UNSET)
        retry_interrupt_config: RetryInterruptConfig | Unset
        if isinstance(_retry_interrupt_config, Unset):
            retry_interrupt_config = UNSET
        else:
            retry_interrupt_config = RetryInterruptConfig.from_dict(_retry_interrupt_config)

        interrupt_config = cls(
            issued_by=issued_by,
            retry_interrupt_config=retry_interrupt_config,
        )

        interrupt_config.additional_properties = d
        return interrupt_config

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
