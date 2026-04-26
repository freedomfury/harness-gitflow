from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.interrupt_effect_dto_interrupt_type import (
    InterruptEffectDTOInterruptType,
    check_interrupt_effect_dto_interrupt_type,
)

if TYPE_CHECKING:
    from ..models.interrupt_config import InterruptConfig


T = TypeVar("T", bound="InterruptEffectDTO")


@_attrs_define
class InterruptEffectDTO:
    """
    Attributes:
        interrupt_id (str):
        took_effect_at (int):
        interrupt_type (InterruptEffectDTOInterruptType):
        interrupt_config (InterruptConfig):
    """

    interrupt_id: str
    took_effect_at: int
    interrupt_type: InterruptEffectDTOInterruptType
    interrupt_config: InterruptConfig
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        interrupt_id = self.interrupt_id

        took_effect_at = self.took_effect_at

        interrupt_type: str = self.interrupt_type

        interrupt_config = self.interrupt_config.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "interruptId": interrupt_id,
                "tookEffectAt": took_effect_at,
                "interruptType": interrupt_type,
                "interruptConfig": interrupt_config,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.interrupt_config import InterruptConfig

        d = dict(src_dict)
        interrupt_id = d.pop("interruptId")

        took_effect_at = d.pop("tookEffectAt")

        interrupt_type = check_interrupt_effect_dto_interrupt_type(d.pop("interruptType"))

        interrupt_config = InterruptConfig.from_dict(d.pop("interruptConfig"))

        interrupt_effect_dto = cls(
            interrupt_id=interrupt_id,
            took_effect_at=took_effect_at,
            interrupt_type=interrupt_type,
            interrupt_config=interrupt_config,
        )

        interrupt_effect_dto.additional_properties = d
        return interrupt_effect_dto

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
