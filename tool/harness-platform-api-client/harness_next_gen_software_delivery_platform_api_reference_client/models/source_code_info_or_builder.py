from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.descriptor import Descriptor
    from ..models.location import Location
    from ..models.location_or_builder import LocationOrBuilder
    from ..models.message import Message
    from ..models.source_code_info_or_builder_all_fields import SourceCodeInfoOrBuilderAllFields
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="SourceCodeInfoOrBuilder")


@_attrs_define
class SourceCodeInfoOrBuilder:
    """
    Attributes:
        location_list (list[Location] | Unset):
        location_count (int | Unset):
        location_or_builder_list (list[LocationOrBuilder] | Unset):
        default_instance_for_type (Message | Unset):
        initialization_error_string (str | Unset):
        all_fields (SourceCodeInfoOrBuilderAllFields | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        descriptor_for_type (Descriptor | Unset):
        initialized (bool | Unset):
    """

    location_list: list[Location] | Unset = UNSET
    location_count: int | Unset = UNSET
    location_or_builder_list: list[LocationOrBuilder] | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    all_fields: SourceCodeInfoOrBuilderAllFields | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        location_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.location_list, Unset):
            location_list = []
            for location_list_item_data in self.location_list:
                location_list_item = location_list_item_data.to_dict()
                location_list.append(location_list_item)

        location_count = self.location_count

        location_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.location_or_builder_list, Unset):
            location_or_builder_list = []
            for location_or_builder_list_item_data in self.location_or_builder_list:
                location_or_builder_list_item = location_or_builder_list_item_data.to_dict()
                location_or_builder_list.append(location_or_builder_list_item)

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        initialization_error_string = self.initialization_error_string

        all_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields, Unset):
            all_fields = self.all_fields.to_dict()

        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        descriptor_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.descriptor_for_type, Unset):
            descriptor_for_type = self.descriptor_for_type.to_dict()

        initialized = self.initialized

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if location_list is not UNSET:
            field_dict["locationList"] = location_list
        if location_count is not UNSET:
            field_dict["locationCount"] = location_count
        if location_or_builder_list is not UNSET:
            field_dict["locationOrBuilderList"] = location_or_builder_list
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if initialization_error_string is not UNSET:
            field_dict["initializationErrorString"] = initialization_error_string
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if unknown_fields is not UNSET:
            field_dict["unknownFields"] = unknown_fields
        if descriptor_for_type is not UNSET:
            field_dict["descriptorForType"] = descriptor_for_type
        if initialized is not UNSET:
            field_dict["initialized"] = initialized

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.descriptor import Descriptor
        from ..models.location import Location
        from ..models.location_or_builder import LocationOrBuilder
        from ..models.message import Message
        from ..models.source_code_info_or_builder_all_fields import SourceCodeInfoOrBuilderAllFields
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _location_list = d.pop("locationList", UNSET)
        location_list: list[Location] | Unset = UNSET
        if _location_list is not UNSET:
            location_list = []
            for location_list_item_data in _location_list:
                location_list_item = Location.from_dict(location_list_item_data)

                location_list.append(location_list_item)

        location_count = d.pop("locationCount", UNSET)

        _location_or_builder_list = d.pop("locationOrBuilderList", UNSET)
        location_or_builder_list: list[LocationOrBuilder] | Unset = UNSET
        if _location_or_builder_list is not UNSET:
            location_or_builder_list = []
            for location_or_builder_list_item_data in _location_or_builder_list:
                location_or_builder_list_item = LocationOrBuilder.from_dict(location_or_builder_list_item_data)

                location_or_builder_list.append(location_or_builder_list_item)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: Message | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = Message.from_dict(_default_instance_for_type)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: SourceCodeInfoOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = SourceCodeInfoOrBuilderAllFields.from_dict(_all_fields)

        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        initialized = d.pop("initialized", UNSET)

        source_code_info_or_builder = cls(
            location_list=location_list,
            location_count=location_count,
            location_or_builder_list=location_or_builder_list,
            default_instance_for_type=default_instance_for_type,
            initialization_error_string=initialization_error_string,
            all_fields=all_fields,
            unknown_fields=unknown_fields,
            descriptor_for_type=descriptor_for_type,
            initialized=initialized,
        )

        source_code_info_or_builder.additional_properties = d
        return source_code_info_or_builder

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
