from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.custom_deployment_variable_response_dto_metadata_map import (
        CustomDeploymentVariableResponseDTOMetadataMap,
    )


T = TypeVar("T", bound="CustomDeploymentVariableResponseDTO")


@_attrs_define
class CustomDeploymentVariableResponseDTO:
    """
    Attributes:
        yaml (str):
        metadata_map (CustomDeploymentVariableResponseDTOMetadataMap):
    """

    yaml: str
    metadata_map: CustomDeploymentVariableResponseDTOMetadataMap
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        yaml = self.yaml

        metadata_map = self.metadata_map.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "yaml": yaml,
                "metadataMap": metadata_map,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom_deployment_variable_response_dto_metadata_map import (
            CustomDeploymentVariableResponseDTOMetadataMap,
        )

        d = dict(src_dict)
        yaml = d.pop("yaml")

        metadata_map = CustomDeploymentVariableResponseDTOMetadataMap.from_dict(d.pop("metadataMap"))

        custom_deployment_variable_response_dto = cls(
            yaml=yaml,
            metadata_map=metadata_map,
        )

        custom_deployment_variable_response_dto.additional_properties = d
        return custom_deployment_variable_response_dto

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
