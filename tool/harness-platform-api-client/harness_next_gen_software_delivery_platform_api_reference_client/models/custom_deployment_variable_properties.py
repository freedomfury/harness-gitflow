from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CustomDeploymentVariableProperties")


@_attrs_define
class CustomDeploymentVariableProperties:
    """
    Attributes:
        fqn (str):
        variable_name (str):
        local_name (str | Unset):
        alias_fqn (str | Unset):
        visible (bool | Unset):
    """

    fqn: str
    variable_name: str
    local_name: str | Unset = UNSET
    alias_fqn: str | Unset = UNSET
    visible: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        fqn = self.fqn

        variable_name = self.variable_name

        local_name = self.local_name

        alias_fqn = self.alias_fqn

        visible = self.visible

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "fqn": fqn,
                "variableName": variable_name,
            }
        )
        if local_name is not UNSET:
            field_dict["localName"] = local_name
        if alias_fqn is not UNSET:
            field_dict["aliasFqn"] = alias_fqn
        if visible is not UNSET:
            field_dict["visible"] = visible

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        fqn = d.pop("fqn")

        variable_name = d.pop("variableName")

        local_name = d.pop("localName", UNSET)

        alias_fqn = d.pop("aliasFqn", UNSET)

        visible = d.pop("visible", UNSET)

        custom_deployment_variable_properties = cls(
            fqn=fqn,
            variable_name=variable_name,
            local_name=local_name,
            alias_fqn=alias_fqn,
            visible=visible,
        )

        custom_deployment_variable_properties.additional_properties = d
        return custom_deployment_variable_properties

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
