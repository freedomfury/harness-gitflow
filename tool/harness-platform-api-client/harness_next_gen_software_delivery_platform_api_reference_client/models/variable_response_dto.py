from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.variable_dto import VariableDTO


T = TypeVar("T", bound="VariableResponseDTO")


@_attrs_define
class VariableResponseDTO:
    """
    Attributes:
        variable (VariableDTO):
        created_at (int | Unset): Time when the Variable was first created.
        last_modified_at (int | Unset): Time when the Variable was last modified.
    """

    variable: VariableDTO
    created_at: int | Unset = UNSET
    last_modified_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        variable = self.variable.to_dict()

        created_at = self.created_at

        last_modified_at = self.last_modified_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "variable": variable,
            }
        )
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if last_modified_at is not UNSET:
            field_dict["lastModifiedAt"] = last_modified_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.variable_dto import VariableDTO

        d = dict(src_dict)
        variable = VariableDTO.from_dict(d.pop("variable"))

        created_at = d.pop("createdAt", UNSET)

        last_modified_at = d.pop("lastModifiedAt", UNSET)

        variable_response_dto = cls(
            variable=variable,
            created_at=created_at,
            last_modified_at=last_modified_at,
        )

        variable_response_dto.additional_properties = d
        return variable_response_dto

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
