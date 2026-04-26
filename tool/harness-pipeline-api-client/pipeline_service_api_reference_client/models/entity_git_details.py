from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EntityGitDetails")


@_attrs_define
class EntityGitDetails:
    """This contains Validity Details of the Entity

    Attributes:
        valid (bool | Unset): Indicates if the Entity is valid
        invalid_yaml (str | Unset): This has the Git File content if the entity is invalid
    """

    valid: bool | Unset = UNSET
    invalid_yaml: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        valid = self.valid

        invalid_yaml = self.invalid_yaml

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if valid is not UNSET:
            field_dict["valid"] = valid
        if invalid_yaml is not UNSET:
            field_dict["invalidYaml"] = invalid_yaml

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        valid = d.pop("valid", UNSET)

        invalid_yaml = d.pop("invalidYaml", UNSET)

        entity_git_details = cls(
            valid=valid,
            invalid_yaml=invalid_yaml,
        )

        entity_git_details.additional_properties = d
        return entity_git_details

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
