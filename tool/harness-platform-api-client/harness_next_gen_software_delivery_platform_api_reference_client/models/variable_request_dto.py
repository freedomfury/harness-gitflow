from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.variable_dto import VariableDTO


T = TypeVar("T", bound="VariableRequestDTO")


@_attrs_define
class VariableRequestDTO:
    """
    Attributes:
        variable (VariableDTO | Unset):
    """

    variable: VariableDTO | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variable: dict[str, Any] | Unset = UNSET
        if not isinstance(self.variable, Unset):
            variable = self.variable.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if variable is not UNSET:
            field_dict["variable"] = variable

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.variable_dto import VariableDTO

        d = dict(src_dict)
        _variable = d.pop("variable", UNSET)
        variable: VariableDTO | Unset
        if isinstance(_variable, Unset):
            variable = UNSET
        else:
            variable = VariableDTO.from_dict(_variable)

        variable_request_dto = cls(
            variable=variable,
        )

        variable_request_dto.additional_properties = d
        return variable_request_dto

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
