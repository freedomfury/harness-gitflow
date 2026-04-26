from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.enum_descriptor_proto_all_fields import EnumDescriptorProtoAllFields
    from ..models.enum_options import EnumOptions
    from ..models.enum_options_or_builder import EnumOptionsOrBuilder
    from ..models.enum_reserved_range import EnumReservedRange
    from ..models.enum_reserved_range_or_builder import EnumReservedRangeOrBuilder
    from ..models.enum_value_descriptor_proto import EnumValueDescriptorProto
    from ..models.enum_value_descriptor_proto_or_builder import EnumValueDescriptorProtoOrBuilder
    from ..models.parser_enum_descriptor_proto import ParserEnumDescriptorProto
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="EnumDescriptorProto")


@_attrs_define
class EnumDescriptorProto:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        name (str | Unset):
        initialized (bool | Unset):
        options (EnumOptions | Unset):
        default_instance_for_type (EnumDescriptorProto | Unset):
        reserved_range_list (list[EnumReservedRange] | Unset):
        reserved_name_list (list[str] | Unset):
        parser_for_type (ParserEnumDescriptorProto | Unset):
        serialized_size (int | Unset):
        options_or_builder (EnumOptionsOrBuilder | Unset):
        name_bytes (ByteString | Unset):
        reserved_range_count (int | Unset):
        reserved_range_or_builder_list (list[EnumReservedRangeOrBuilder] | Unset):
        reserved_name_count (int | Unset):
        value_count (int | Unset):
        value_or_builder_list (list[EnumValueDescriptorProtoOrBuilder] | Unset):
        value_list (list[EnumValueDescriptorProto] | Unset):
        all_fields (EnumDescriptorProtoAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    name: str | Unset = UNSET
    initialized: bool | Unset = UNSET
    options: EnumOptions | Unset = UNSET
    default_instance_for_type: EnumDescriptorProto | Unset = UNSET
    reserved_range_list: list[EnumReservedRange] | Unset = UNSET
    reserved_name_list: list[str] | Unset = UNSET
    parser_for_type: ParserEnumDescriptorProto | Unset = UNSET
    serialized_size: int | Unset = UNSET
    options_or_builder: EnumOptionsOrBuilder | Unset = UNSET
    name_bytes: ByteString | Unset = UNSET
    reserved_range_count: int | Unset = UNSET
    reserved_range_or_builder_list: list[EnumReservedRangeOrBuilder] | Unset = UNSET
    reserved_name_count: int | Unset = UNSET
    value_count: int | Unset = UNSET
    value_or_builder_list: list[EnumValueDescriptorProtoOrBuilder] | Unset = UNSET
    value_list: list[EnumValueDescriptorProto] | Unset = UNSET
    all_fields: EnumDescriptorProtoAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        name = self.name

        initialized = self.initialized

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        reserved_range_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reserved_range_list, Unset):
            reserved_range_list = []
            for reserved_range_list_item_data in self.reserved_range_list:
                reserved_range_list_item = reserved_range_list_item_data.to_dict()
                reserved_range_list.append(reserved_range_list_item)

        reserved_name_list: list[str] | Unset = UNSET
        if not isinstance(self.reserved_name_list, Unset):
            reserved_name_list = self.reserved_name_list

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        options_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options_or_builder, Unset):
            options_or_builder = self.options_or_builder.to_dict()

        name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name_bytes, Unset):
            name_bytes = self.name_bytes.to_dict()

        reserved_range_count = self.reserved_range_count

        reserved_range_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reserved_range_or_builder_list, Unset):
            reserved_range_or_builder_list = []
            for reserved_range_or_builder_list_item_data in self.reserved_range_or_builder_list:
                reserved_range_or_builder_list_item = reserved_range_or_builder_list_item_data.to_dict()
                reserved_range_or_builder_list.append(reserved_range_or_builder_list_item)

        reserved_name_count = self.reserved_name_count

        value_count = self.value_count

        value_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.value_or_builder_list, Unset):
            value_or_builder_list = []
            for value_or_builder_list_item_data in self.value_or_builder_list:
                value_or_builder_list_item = value_or_builder_list_item_data.to_dict()
                value_or_builder_list.append(value_or_builder_list_item)

        value_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.value_list, Unset):
            value_list = []
            for value_list_item_data in self.value_list:
                value_list_item = value_list_item_data.to_dict()
                value_list.append(value_list_item)

        all_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields, Unset):
            all_fields = self.all_fields.to_dict()

        initialization_error_string = self.initialization_error_string

        descriptor_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.descriptor_for_type, Unset):
            descriptor_for_type = self.descriptor_for_type.to_dict()

        memoized_serialized_size = self.memoized_serialized_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unknown_fields is not UNSET:
            field_dict["unknownFields"] = unknown_fields
        if name is not UNSET:
            field_dict["name"] = name
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if options is not UNSET:
            field_dict["options"] = options
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if reserved_range_list is not UNSET:
            field_dict["reservedRangeList"] = reserved_range_list
        if reserved_name_list is not UNSET:
            field_dict["reservedNameList"] = reserved_name_list
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if options_or_builder is not UNSET:
            field_dict["optionsOrBuilder"] = options_or_builder
        if name_bytes is not UNSET:
            field_dict["nameBytes"] = name_bytes
        if reserved_range_count is not UNSET:
            field_dict["reservedRangeCount"] = reserved_range_count
        if reserved_range_or_builder_list is not UNSET:
            field_dict["reservedRangeOrBuilderList"] = reserved_range_or_builder_list
        if reserved_name_count is not UNSET:
            field_dict["reservedNameCount"] = reserved_name_count
        if value_count is not UNSET:
            field_dict["valueCount"] = value_count
        if value_or_builder_list is not UNSET:
            field_dict["valueOrBuilderList"] = value_or_builder_list
        if value_list is not UNSET:
            field_dict["valueList"] = value_list
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if initialization_error_string is not UNSET:
            field_dict["initializationErrorString"] = initialization_error_string
        if descriptor_for_type is not UNSET:
            field_dict["descriptorForType"] = descriptor_for_type
        if memoized_serialized_size is not UNSET:
            field_dict["memoizedSerializedSize"] = memoized_serialized_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.enum_descriptor_proto_all_fields import EnumDescriptorProtoAllFields
        from ..models.enum_options import EnumOptions
        from ..models.enum_options_or_builder import EnumOptionsOrBuilder
        from ..models.enum_reserved_range import EnumReservedRange
        from ..models.enum_reserved_range_or_builder import EnumReservedRangeOrBuilder
        from ..models.enum_value_descriptor_proto import EnumValueDescriptorProto
        from ..models.enum_value_descriptor_proto_or_builder import EnumValueDescriptorProtoOrBuilder
        from ..models.parser_enum_descriptor_proto import ParserEnumDescriptorProto
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        name = d.pop("name", UNSET)

        initialized = d.pop("initialized", UNSET)

        _options = d.pop("options", UNSET)
        options: EnumOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = EnumOptions.from_dict(_options)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: EnumDescriptorProto | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = EnumDescriptorProto.from_dict(_default_instance_for_type)

        _reserved_range_list = d.pop("reservedRangeList", UNSET)
        reserved_range_list: list[EnumReservedRange] | Unset = UNSET
        if _reserved_range_list is not UNSET:
            reserved_range_list = []
            for reserved_range_list_item_data in _reserved_range_list:
                reserved_range_list_item = EnumReservedRange.from_dict(reserved_range_list_item_data)

                reserved_range_list.append(reserved_range_list_item)

        reserved_name_list = cast(list[str], d.pop("reservedNameList", UNSET))

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserEnumDescriptorProto | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserEnumDescriptorProto.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _options_or_builder = d.pop("optionsOrBuilder", UNSET)
        options_or_builder: EnumOptionsOrBuilder | Unset
        if isinstance(_options_or_builder, Unset):
            options_or_builder = UNSET
        else:
            options_or_builder = EnumOptionsOrBuilder.from_dict(_options_or_builder)

        _name_bytes = d.pop("nameBytes", UNSET)
        name_bytes: ByteString | Unset
        if isinstance(_name_bytes, Unset):
            name_bytes = UNSET
        else:
            name_bytes = ByteString.from_dict(_name_bytes)

        reserved_range_count = d.pop("reservedRangeCount", UNSET)

        _reserved_range_or_builder_list = d.pop("reservedRangeOrBuilderList", UNSET)
        reserved_range_or_builder_list: list[EnumReservedRangeOrBuilder] | Unset = UNSET
        if _reserved_range_or_builder_list is not UNSET:
            reserved_range_or_builder_list = []
            for reserved_range_or_builder_list_item_data in _reserved_range_or_builder_list:
                reserved_range_or_builder_list_item = EnumReservedRangeOrBuilder.from_dict(
                    reserved_range_or_builder_list_item_data
                )

                reserved_range_or_builder_list.append(reserved_range_or_builder_list_item)

        reserved_name_count = d.pop("reservedNameCount", UNSET)

        value_count = d.pop("valueCount", UNSET)

        _value_or_builder_list = d.pop("valueOrBuilderList", UNSET)
        value_or_builder_list: list[EnumValueDescriptorProtoOrBuilder] | Unset = UNSET
        if _value_or_builder_list is not UNSET:
            value_or_builder_list = []
            for value_or_builder_list_item_data in _value_or_builder_list:
                value_or_builder_list_item = EnumValueDescriptorProtoOrBuilder.from_dict(
                    value_or_builder_list_item_data
                )

                value_or_builder_list.append(value_or_builder_list_item)

        _value_list = d.pop("valueList", UNSET)
        value_list: list[EnumValueDescriptorProto] | Unset = UNSET
        if _value_list is not UNSET:
            value_list = []
            for value_list_item_data in _value_list:
                value_list_item = EnumValueDescriptorProto.from_dict(value_list_item_data)

                value_list.append(value_list_item)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: EnumDescriptorProtoAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = EnumDescriptorProtoAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        enum_descriptor_proto = cls(
            unknown_fields=unknown_fields,
            name=name,
            initialized=initialized,
            options=options,
            default_instance_for_type=default_instance_for_type,
            reserved_range_list=reserved_range_list,
            reserved_name_list=reserved_name_list,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            options_or_builder=options_or_builder,
            name_bytes=name_bytes,
            reserved_range_count=reserved_range_count,
            reserved_range_or_builder_list=reserved_range_or_builder_list,
            reserved_name_count=reserved_name_count,
            value_count=value_count,
            value_or_builder_list=value_or_builder_list,
            value_list=value_list,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        enum_descriptor_proto.additional_properties = d
        return enum_descriptor_proto

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
