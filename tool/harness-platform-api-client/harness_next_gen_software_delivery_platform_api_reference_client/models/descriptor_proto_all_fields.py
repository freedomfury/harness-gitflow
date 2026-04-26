from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.descriptor_proto_all_fields_additional_property import DescriptorProtoAllFieldsAdditionalProperty


T = TypeVar("T", bound="DescriptorProtoAllFields")


@_attrs_define
class DescriptorProtoAllFields:
    """ """

    additional_properties: dict[str, DescriptorProtoAllFieldsAdditionalProperty] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop.to_dict()

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.descriptor_proto_all_fields_additional_property import DescriptorProtoAllFieldsAdditionalProperty

        d = dict(src_dict)
        descriptor_proto_all_fields = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = DescriptorProtoAllFieldsAdditionalProperty.from_dict(prop_dict)

            additional_properties[prop_name] = additional_property

        descriptor_proto_all_fields.additional_properties = additional_properties
        return descriptor_proto_all_fields

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> DescriptorProtoAllFieldsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: DescriptorProtoAllFieldsAdditionalProperty) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
