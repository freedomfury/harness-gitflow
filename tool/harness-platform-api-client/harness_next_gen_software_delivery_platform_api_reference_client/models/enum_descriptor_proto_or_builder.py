from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.enum_descriptor_proto_or_builder_all_fields import EnumDescriptorProtoOrBuilderAllFields
    from ..models.enum_options import EnumOptions
    from ..models.enum_options_or_builder import EnumOptionsOrBuilder
    from ..models.enum_reserved_range import EnumReservedRange
    from ..models.enum_reserved_range_or_builder import EnumReservedRangeOrBuilder
    from ..models.enum_value_descriptor_proto import EnumValueDescriptorProto
    from ..models.enum_value_descriptor_proto_or_builder import EnumValueDescriptorProtoOrBuilder
    from ..models.message import Message
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="EnumDescriptorProtoOrBuilder")


@_attrs_define
class EnumDescriptorProtoOrBuilder:
    """
    Attributes:
        reserved_range_list (list[EnumReservedRange] | Unset):
        reserved_name_list (list[str] | Unset):
        options_or_builder (EnumOptionsOrBuilder | Unset):
        value_list (list[EnumValueDescriptorProto] | Unset):
        value_count (int | Unset):
        value_or_builder_list (list[EnumValueDescriptorProtoOrBuilder] | Unset):
        reserved_range_count (int | Unset):
        reserved_range_or_builder_list (list[EnumReservedRangeOrBuilder] | Unset):
        reserved_name_count (int | Unset):
        name (str | Unset):
        name_bytes (ByteString | Unset):
        options (EnumOptions | Unset):
        initialization_error_string (str | Unset):
        all_fields (EnumDescriptorProtoOrBuilderAllFields | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        descriptor_for_type (Descriptor | Unset):
        default_instance_for_type (Message | Unset):
        initialized (bool | Unset):
    """

    reserved_range_list: list[EnumReservedRange] | Unset = UNSET
    reserved_name_list: list[str] | Unset = UNSET
    options_or_builder: EnumOptionsOrBuilder | Unset = UNSET
    value_list: list[EnumValueDescriptorProto] | Unset = UNSET
    value_count: int | Unset = UNSET
    value_or_builder_list: list[EnumValueDescriptorProtoOrBuilder] | Unset = UNSET
    reserved_range_count: int | Unset = UNSET
    reserved_range_or_builder_list: list[EnumReservedRangeOrBuilder] | Unset = UNSET
    reserved_name_count: int | Unset = UNSET
    name: str | Unset = UNSET
    name_bytes: ByteString | Unset = UNSET
    options: EnumOptions | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    all_fields: EnumDescriptorProtoOrBuilderAllFields | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reserved_range_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reserved_range_list, Unset):
            reserved_range_list = []
            for reserved_range_list_item_data in self.reserved_range_list:
                reserved_range_list_item = reserved_range_list_item_data.to_dict()
                reserved_range_list.append(reserved_range_list_item)

        reserved_name_list: list[str] | Unset = UNSET
        if not isinstance(self.reserved_name_list, Unset):
            reserved_name_list = self.reserved_name_list

        options_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options_or_builder, Unset):
            options_or_builder = self.options_or_builder.to_dict()

        value_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.value_list, Unset):
            value_list = []
            for value_list_item_data in self.value_list:
                value_list_item = value_list_item_data.to_dict()
                value_list.append(value_list_item)

        value_count = self.value_count

        value_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.value_or_builder_list, Unset):
            value_or_builder_list = []
            for value_or_builder_list_item_data in self.value_or_builder_list:
                value_or_builder_list_item = value_or_builder_list_item_data.to_dict()
                value_or_builder_list.append(value_or_builder_list_item)

        reserved_range_count = self.reserved_range_count

        reserved_range_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reserved_range_or_builder_list, Unset):
            reserved_range_or_builder_list = []
            for reserved_range_or_builder_list_item_data in self.reserved_range_or_builder_list:
                reserved_range_or_builder_list_item = reserved_range_or_builder_list_item_data.to_dict()
                reserved_range_or_builder_list.append(reserved_range_or_builder_list_item)

        reserved_name_count = self.reserved_name_count

        name = self.name

        name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name_bytes, Unset):
            name_bytes = self.name_bytes.to_dict()

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

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

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        initialized = self.initialized

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reserved_range_list is not UNSET:
            field_dict["reservedRangeList"] = reserved_range_list
        if reserved_name_list is not UNSET:
            field_dict["reservedNameList"] = reserved_name_list
        if options_or_builder is not UNSET:
            field_dict["optionsOrBuilder"] = options_or_builder
        if value_list is not UNSET:
            field_dict["valueList"] = value_list
        if value_count is not UNSET:
            field_dict["valueCount"] = value_count
        if value_or_builder_list is not UNSET:
            field_dict["valueOrBuilderList"] = value_or_builder_list
        if reserved_range_count is not UNSET:
            field_dict["reservedRangeCount"] = reserved_range_count
        if reserved_range_or_builder_list is not UNSET:
            field_dict["reservedRangeOrBuilderList"] = reserved_range_or_builder_list
        if reserved_name_count is not UNSET:
            field_dict["reservedNameCount"] = reserved_name_count
        if name is not UNSET:
            field_dict["name"] = name
        if name_bytes is not UNSET:
            field_dict["nameBytes"] = name_bytes
        if options is not UNSET:
            field_dict["options"] = options
        if initialization_error_string is not UNSET:
            field_dict["initializationErrorString"] = initialization_error_string
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if unknown_fields is not UNSET:
            field_dict["unknownFields"] = unknown_fields
        if descriptor_for_type is not UNSET:
            field_dict["descriptorForType"] = descriptor_for_type
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if initialized is not UNSET:
            field_dict["initialized"] = initialized

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.enum_descriptor_proto_or_builder_all_fields import EnumDescriptorProtoOrBuilderAllFields
        from ..models.enum_options import EnumOptions
        from ..models.enum_options_or_builder import EnumOptionsOrBuilder
        from ..models.enum_reserved_range import EnumReservedRange
        from ..models.enum_reserved_range_or_builder import EnumReservedRangeOrBuilder
        from ..models.enum_value_descriptor_proto import EnumValueDescriptorProto
        from ..models.enum_value_descriptor_proto_or_builder import EnumValueDescriptorProtoOrBuilder
        from ..models.message import Message
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _reserved_range_list = d.pop("reservedRangeList", UNSET)
        reserved_range_list: list[EnumReservedRange] | Unset = UNSET
        if _reserved_range_list is not UNSET:
            reserved_range_list = []
            for reserved_range_list_item_data in _reserved_range_list:
                reserved_range_list_item = EnumReservedRange.from_dict(reserved_range_list_item_data)

                reserved_range_list.append(reserved_range_list_item)

        reserved_name_list = cast(list[str], d.pop("reservedNameList", UNSET))

        _options_or_builder = d.pop("optionsOrBuilder", UNSET)
        options_or_builder: EnumOptionsOrBuilder | Unset
        if isinstance(_options_or_builder, Unset):
            options_or_builder = UNSET
        else:
            options_or_builder = EnumOptionsOrBuilder.from_dict(_options_or_builder)

        _value_list = d.pop("valueList", UNSET)
        value_list: list[EnumValueDescriptorProto] | Unset = UNSET
        if _value_list is not UNSET:
            value_list = []
            for value_list_item_data in _value_list:
                value_list_item = EnumValueDescriptorProto.from_dict(value_list_item_data)

                value_list.append(value_list_item)

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

        name = d.pop("name", UNSET)

        _name_bytes = d.pop("nameBytes", UNSET)
        name_bytes: ByteString | Unset
        if isinstance(_name_bytes, Unset):
            name_bytes = UNSET
        else:
            name_bytes = ByteString.from_dict(_name_bytes)

        _options = d.pop("options", UNSET)
        options: EnumOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = EnumOptions.from_dict(_options)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: EnumDescriptorProtoOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = EnumDescriptorProtoOrBuilderAllFields.from_dict(_all_fields)

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

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: Message | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = Message.from_dict(_default_instance_for_type)

        initialized = d.pop("initialized", UNSET)

        enum_descriptor_proto_or_builder = cls(
            reserved_range_list=reserved_range_list,
            reserved_name_list=reserved_name_list,
            options_or_builder=options_or_builder,
            value_list=value_list,
            value_count=value_count,
            value_or_builder_list=value_or_builder_list,
            reserved_range_count=reserved_range_count,
            reserved_range_or_builder_list=reserved_range_or_builder_list,
            reserved_name_count=reserved_name_count,
            name=name,
            name_bytes=name_bytes,
            options=options,
            initialization_error_string=initialization_error_string,
            all_fields=all_fields,
            unknown_fields=unknown_fields,
            descriptor_for_type=descriptor_for_type,
            default_instance_for_type=default_instance_for_type,
            initialized=initialized,
        )

        enum_descriptor_proto_or_builder.additional_properties = d
        return enum_descriptor_proto_or_builder

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
