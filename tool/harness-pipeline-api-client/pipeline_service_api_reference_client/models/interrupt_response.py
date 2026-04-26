from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.interrupt_response_type import InterruptResponseType, check_interrupt_response_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="InterruptResponse")


@_attrs_define
class InterruptResponse:
    """Contains the ID and type of the interrupt issued along with the execution id.

    Attributes:
        id (str | Unset):
        type_ (InterruptResponseType | Unset):
        plan_execution_id (str | Unset):
    """

    id: str | Unset = UNSET
    type_: InterruptResponseType | Unset = UNSET
    plan_execution_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        plan_execution_id = self.plan_execution_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if plan_execution_id is not UNSET:
            field_dict["planExecutionId"] = plan_execution_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: InterruptResponseType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_interrupt_response_type(_type_)

        plan_execution_id = d.pop("planExecutionId", UNSET)

        interrupt_response = cls(
            id=id,
            type_=type_,
            plan_execution_id=plan_execution_id,
        )

        interrupt_response.additional_properties = d
        return interrupt_response

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
