from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CustomDeploymentRefreshYamlDTO")


@_attrs_define
class CustomDeploymentRefreshYamlDTO:
    """
    Attributes:
        refreshed_yaml (str):
    """

    refreshed_yaml: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        refreshed_yaml = self.refreshed_yaml

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "refreshedYaml": refreshed_yaml,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        refreshed_yaml = d.pop("refreshedYaml")

        custom_deployment_refresh_yaml_dto = cls(
            refreshed_yaml=refreshed_yaml,
        )

        custom_deployment_refresh_yaml_dto.additional_properties = d
        return custom_deployment_refresh_yaml_dto

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
