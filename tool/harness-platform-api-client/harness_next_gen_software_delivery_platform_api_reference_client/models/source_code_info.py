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
    from ..models.parser_source_code_info import ParserSourceCodeInfo
    from ..models.source_code_info_all_fields import SourceCodeInfoAllFields
    from ..models.source_code_info_all_fields_raw import SourceCodeInfoAllFieldsRaw
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="SourceCodeInfo")


@_attrs_define
class SourceCodeInfo:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        parser_for_type (ParserSourceCodeInfo | Unset):
        serialized_size (int | Unset):
        location_list (list[Location] | Unset):
        location_count (int | Unset):
        location_or_builder_list (list[LocationOrBuilder] | Unset):
        default_instance_for_type (SourceCodeInfo | Unset):
        initialized (bool | Unset):
        initialization_error_string (str | Unset):
        all_fields (SourceCodeInfoAllFields | Unset):
        descriptor_for_type (Descriptor | Unset):
        all_fields_raw (SourceCodeInfoAllFieldsRaw | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    parser_for_type: ParserSourceCodeInfo | Unset = UNSET
    serialized_size: int | Unset = UNSET
    location_list: list[Location] | Unset = UNSET
    location_count: int | Unset = UNSET
    location_or_builder_list: list[LocationOrBuilder] | Unset = UNSET
    default_instance_for_type: SourceCodeInfo | Unset = UNSET
    initialized: bool | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    all_fields: SourceCodeInfoAllFields | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    all_fields_raw: SourceCodeInfoAllFieldsRaw | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

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

        initialized = self.initialized

        initialization_error_string = self.initialization_error_string

        all_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields, Unset):
            all_fields = self.all_fields.to_dict()

        descriptor_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.descriptor_for_type, Unset):
            descriptor_for_type = self.descriptor_for_type.to_dict()

        all_fields_raw: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields_raw, Unset):
            all_fields_raw = self.all_fields_raw.to_dict()

        memoized_serialized_size = self.memoized_serialized_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unknown_fields is not UNSET:
            field_dict["unknownFields"] = unknown_fields
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if location_list is not UNSET:
            field_dict["locationList"] = location_list
        if location_count is not UNSET:
            field_dict["locationCount"] = location_count
        if location_or_builder_list is not UNSET:
            field_dict["locationOrBuilderList"] = location_or_builder_list
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if initialization_error_string is not UNSET:
            field_dict["initializationErrorString"] = initialization_error_string
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if descriptor_for_type is not UNSET:
            field_dict["descriptorForType"] = descriptor_for_type
        if all_fields_raw is not UNSET:
            field_dict["allFieldsRaw"] = all_fields_raw
        if memoized_serialized_size is not UNSET:
            field_dict["memoizedSerializedSize"] = memoized_serialized_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.descriptor import Descriptor
        from ..models.location import Location
        from ..models.location_or_builder import LocationOrBuilder
        from ..models.parser_source_code_info import ParserSourceCodeInfo
        from ..models.source_code_info_all_fields import SourceCodeInfoAllFields
        from ..models.source_code_info_all_fields_raw import SourceCodeInfoAllFieldsRaw
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserSourceCodeInfo | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserSourceCodeInfo.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

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
        default_instance_for_type: SourceCodeInfo | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = SourceCodeInfo.from_dict(_default_instance_for_type)

        initialized = d.pop("initialized", UNSET)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: SourceCodeInfoAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = SourceCodeInfoAllFields.from_dict(_all_fields)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        _all_fields_raw = d.pop("allFieldsRaw", UNSET)
        all_fields_raw: SourceCodeInfoAllFieldsRaw | Unset
        if isinstance(_all_fields_raw, Unset):
            all_fields_raw = UNSET
        else:
            all_fields_raw = SourceCodeInfoAllFieldsRaw.from_dict(_all_fields_raw)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        source_code_info = cls(
            unknown_fields=unknown_fields,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            location_list=location_list,
            location_count=location_count,
            location_or_builder_list=location_or_builder_list,
            default_instance_for_type=default_instance_for_type,
            initialized=initialized,
            initialization_error_string=initialization_error_string,
            all_fields=all_fields,
            descriptor_for_type=descriptor_for_type,
            all_fields_raw=all_fields_raw,
            memoized_serialized_size=memoized_serialized_size,
        )

        source_code_info.additional_properties = d
        return source_code_info

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
