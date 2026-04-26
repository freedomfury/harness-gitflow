from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pipeline_filter_properties_module_properties_additional_property import (
        PipelineFilterPropertiesModulePropertiesAdditionalProperty,
    )


T = TypeVar("T", bound="PipelineFilterPropertiesModuleProperties")


@_attrs_define
class PipelineFilterPropertiesModuleProperties:
    """These are the Module Properties on which the filter will be applied.

    Attributes:
        empty (bool | Unset):
    """

    empty: bool | Unset = UNSET
    additional_properties: dict[str, PipelineFilterPropertiesModulePropertiesAdditionalProperty] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:
        empty = self.empty

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        field_dict.update({})
        if empty is not UNSET:
            field_dict["empty"] = empty

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.pipeline_filter_properties_module_properties_additional_property import (
            PipelineFilterPropertiesModulePropertiesAdditionalProperty,
        )

        d = dict(src_dict)
        empty = d.pop("empty", UNSET)

        pipeline_filter_properties_module_properties = cls(
            empty=empty,
        )

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = PipelineFilterPropertiesModulePropertiesAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        pipeline_filter_properties_module_properties.additional_properties = additional_properties
        return pipeline_filter_properties_module_properties

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> PipelineFilterPropertiesModulePropertiesAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: PipelineFilterPropertiesModulePropertiesAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
