from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.recurrence_type import RecurrenceType, check_recurrence_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.recurrence_spec import RecurrenceSpec


T = TypeVar("T", bound="Recurrence")


@_attrs_define
class Recurrence:
    """
    Attributes:
        type_ (RecurrenceType):
        spec (RecurrenceSpec | Unset):
    """

    type_: RecurrenceType
    spec: RecurrenceSpec | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.recurrence_spec import RecurrenceSpec

        d = dict(src_dict)
        type_ = check_recurrence_type(d.pop("type"))

        _spec = d.pop("spec", UNSET)
        spec: RecurrenceSpec | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = RecurrenceSpec.from_dict(_spec)

        recurrence = cls(
            type_=type_,
            spec=spec,
        )

        recurrence.additional_properties = d
        return recurrence

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
