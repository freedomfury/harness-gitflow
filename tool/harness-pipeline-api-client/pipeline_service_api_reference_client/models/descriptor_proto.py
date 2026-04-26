from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.descriptor_proto_all_fields import DescriptorProtoAllFields
    from ..models.descriptor_proto_or_builder import DescriptorProtoOrBuilder
    from ..models.enum_descriptor_proto import EnumDescriptorProto
    from ..models.enum_descriptor_proto_or_builder import EnumDescriptorProtoOrBuilder
    from ..models.extension_range import ExtensionRange
    from ..models.extension_range_or_builder import ExtensionRangeOrBuilder
    from ..models.field_descriptor_proto import FieldDescriptorProto
    from ..models.field_descriptor_proto_or_builder import FieldDescriptorProtoOrBuilder
    from ..models.message_options import MessageOptions
    from ..models.message_options_or_builder import MessageOptionsOrBuilder
    from ..models.oneof_descriptor_proto import OneofDescriptorProto
    from ..models.oneof_descriptor_proto_or_builder import OneofDescriptorProtoOrBuilder
    from ..models.parser_descriptor_proto import ParserDescriptorProto
    from ..models.reserved_range import ReservedRange
    from ..models.reserved_range_or_builder import ReservedRangeOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="DescriptorProto")


@_attrs_define
class DescriptorProto:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        name (str | Unset):
        initialized (bool | Unset):
        options (MessageOptions | Unset):
        field_count (int | Unset):
        default_instance_for_type (DescriptorProto | Unset):
        reserved_range_list (list[ReservedRange] | Unset):
        reserved_name_list (list[str] | Unset):
        extension_range_list (list[ExtensionRange] | Unset):
        oneof_decl_count (int | Unset):
        nested_type_count (int | Unset):
        enum_type_count (int | Unset):
        extension_count (int | Unset):
        extension_range_count (int | Unset):
        parser_for_type (ParserDescriptorProto | Unset):
        serialized_size (int | Unset):
        enum_type_list (list[EnumDescriptorProto] | Unset):
        enum_type_or_builder_list (list[EnumDescriptorProtoOrBuilder] | Unset):
        extension_list (list[FieldDescriptorProto] | Unset):
        extension_or_builder_list (list[FieldDescriptorProtoOrBuilder] | Unset):
        options_or_builder (MessageOptionsOrBuilder | Unset):
        name_bytes (ByteString | Unset):
        field_list (list[FieldDescriptorProto] | Unset):
        field_or_builder_list (list[FieldDescriptorProtoOrBuilder] | Unset):
        nested_type_list (list[DescriptorProto] | Unset):
        nested_type_or_builder_list (list[DescriptorProtoOrBuilder] | Unset):
        extension_range_or_builder_list (list[ExtensionRangeOrBuilder] | Unset):
        oneof_decl_list (list[OneofDescriptorProto] | Unset):
        oneof_decl_or_builder_list (list[OneofDescriptorProtoOrBuilder] | Unset):
        reserved_range_count (int | Unset):
        reserved_range_or_builder_list (list[ReservedRangeOrBuilder] | Unset):
        reserved_name_count (int | Unset):
        all_fields (DescriptorProtoAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    name: str | Unset = UNSET
    initialized: bool | Unset = UNSET
    options: MessageOptions | Unset = UNSET
    field_count: int | Unset = UNSET
    default_instance_for_type: DescriptorProto | Unset = UNSET
    reserved_range_list: list[ReservedRange] | Unset = UNSET
    reserved_name_list: list[str] | Unset = UNSET
    extension_range_list: list[ExtensionRange] | Unset = UNSET
    oneof_decl_count: int | Unset = UNSET
    nested_type_count: int | Unset = UNSET
    enum_type_count: int | Unset = UNSET
    extension_count: int | Unset = UNSET
    extension_range_count: int | Unset = UNSET
    parser_for_type: ParserDescriptorProto | Unset = UNSET
    serialized_size: int | Unset = UNSET
    enum_type_list: list[EnumDescriptorProto] | Unset = UNSET
    enum_type_or_builder_list: list[EnumDescriptorProtoOrBuilder] | Unset = UNSET
    extension_list: list[FieldDescriptorProto] | Unset = UNSET
    extension_or_builder_list: list[FieldDescriptorProtoOrBuilder] | Unset = UNSET
    options_or_builder: MessageOptionsOrBuilder | Unset = UNSET
    name_bytes: ByteString | Unset = UNSET
    field_list: list[FieldDescriptorProto] | Unset = UNSET
    field_or_builder_list: list[FieldDescriptorProtoOrBuilder] | Unset = UNSET
    nested_type_list: list[DescriptorProto] | Unset = UNSET
    nested_type_or_builder_list: list[DescriptorProtoOrBuilder] | Unset = UNSET
    extension_range_or_builder_list: list[ExtensionRangeOrBuilder] | Unset = UNSET
    oneof_decl_list: list[OneofDescriptorProto] | Unset = UNSET
    oneof_decl_or_builder_list: list[OneofDescriptorProtoOrBuilder] | Unset = UNSET
    reserved_range_count: int | Unset = UNSET
    reserved_range_or_builder_list: list[ReservedRangeOrBuilder] | Unset = UNSET
    reserved_name_count: int | Unset = UNSET
    all_fields: DescriptorProtoAllFields | Unset = UNSET
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

        field_count = self.field_count

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

        extension_range_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.extension_range_list, Unset):
            extension_range_list = []
            for extension_range_list_item_data in self.extension_range_list:
                extension_range_list_item = extension_range_list_item_data.to_dict()
                extension_range_list.append(extension_range_list_item)

        oneof_decl_count = self.oneof_decl_count

        nested_type_count = self.nested_type_count

        enum_type_count = self.enum_type_count

        extension_count = self.extension_count

        extension_range_count = self.extension_range_count

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        enum_type_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.enum_type_list, Unset):
            enum_type_list = []
            for enum_type_list_item_data in self.enum_type_list:
                enum_type_list_item = enum_type_list_item_data.to_dict()
                enum_type_list.append(enum_type_list_item)

        enum_type_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.enum_type_or_builder_list, Unset):
            enum_type_or_builder_list = []
            for enum_type_or_builder_list_item_data in self.enum_type_or_builder_list:
                enum_type_or_builder_list_item = enum_type_or_builder_list_item_data.to_dict()
                enum_type_or_builder_list.append(enum_type_or_builder_list_item)

        extension_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.extension_list, Unset):
            extension_list = []
            for extension_list_item_data in self.extension_list:
                extension_list_item = extension_list_item_data.to_dict()
                extension_list.append(extension_list_item)

        extension_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.extension_or_builder_list, Unset):
            extension_or_builder_list = []
            for extension_or_builder_list_item_data in self.extension_or_builder_list:
                extension_or_builder_list_item = extension_or_builder_list_item_data.to_dict()
                extension_or_builder_list.append(extension_or_builder_list_item)

        options_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options_or_builder, Unset):
            options_or_builder = self.options_or_builder.to_dict()

        name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name_bytes, Unset):
            name_bytes = self.name_bytes.to_dict()

        field_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.field_list, Unset):
            field_list = []
            for field_list_item_data in self.field_list:
                field_list_item = field_list_item_data.to_dict()
                field_list.append(field_list_item)

        field_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.field_or_builder_list, Unset):
            field_or_builder_list = []
            for field_or_builder_list_item_data in self.field_or_builder_list:
                field_or_builder_list_item = field_or_builder_list_item_data.to_dict()
                field_or_builder_list.append(field_or_builder_list_item)

        nested_type_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nested_type_list, Unset):
            nested_type_list = []
            for nested_type_list_item_data in self.nested_type_list:
                nested_type_list_item = nested_type_list_item_data.to_dict()
                nested_type_list.append(nested_type_list_item)

        nested_type_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nested_type_or_builder_list, Unset):
            nested_type_or_builder_list = []
            for nested_type_or_builder_list_item_data in self.nested_type_or_builder_list:
                nested_type_or_builder_list_item = nested_type_or_builder_list_item_data.to_dict()
                nested_type_or_builder_list.append(nested_type_or_builder_list_item)

        extension_range_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.extension_range_or_builder_list, Unset):
            extension_range_or_builder_list = []
            for extension_range_or_builder_list_item_data in self.extension_range_or_builder_list:
                extension_range_or_builder_list_item = extension_range_or_builder_list_item_data.to_dict()
                extension_range_or_builder_list.append(extension_range_or_builder_list_item)

        oneof_decl_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.oneof_decl_list, Unset):
            oneof_decl_list = []
            for oneof_decl_list_item_data in self.oneof_decl_list:
                oneof_decl_list_item = oneof_decl_list_item_data.to_dict()
                oneof_decl_list.append(oneof_decl_list_item)

        oneof_decl_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.oneof_decl_or_builder_list, Unset):
            oneof_decl_or_builder_list = []
            for oneof_decl_or_builder_list_item_data in self.oneof_decl_or_builder_list:
                oneof_decl_or_builder_list_item = oneof_decl_or_builder_list_item_data.to_dict()
                oneof_decl_or_builder_list.append(oneof_decl_or_builder_list_item)

        reserved_range_count = self.reserved_range_count

        reserved_range_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reserved_range_or_builder_list, Unset):
            reserved_range_or_builder_list = []
            for reserved_range_or_builder_list_item_data in self.reserved_range_or_builder_list:
                reserved_range_or_builder_list_item = reserved_range_or_builder_list_item_data.to_dict()
                reserved_range_or_builder_list.append(reserved_range_or_builder_list_item)

        reserved_name_count = self.reserved_name_count

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
        if field_count is not UNSET:
            field_dict["fieldCount"] = field_count
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if reserved_range_list is not UNSET:
            field_dict["reservedRangeList"] = reserved_range_list
        if reserved_name_list is not UNSET:
            field_dict["reservedNameList"] = reserved_name_list
        if extension_range_list is not UNSET:
            field_dict["extensionRangeList"] = extension_range_list
        if oneof_decl_count is not UNSET:
            field_dict["oneofDeclCount"] = oneof_decl_count
        if nested_type_count is not UNSET:
            field_dict["nestedTypeCount"] = nested_type_count
        if enum_type_count is not UNSET:
            field_dict["enumTypeCount"] = enum_type_count
        if extension_count is not UNSET:
            field_dict["extensionCount"] = extension_count
        if extension_range_count is not UNSET:
            field_dict["extensionRangeCount"] = extension_range_count
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if enum_type_list is not UNSET:
            field_dict["enumTypeList"] = enum_type_list
        if enum_type_or_builder_list is not UNSET:
            field_dict["enumTypeOrBuilderList"] = enum_type_or_builder_list
        if extension_list is not UNSET:
            field_dict["extensionList"] = extension_list
        if extension_or_builder_list is not UNSET:
            field_dict["extensionOrBuilderList"] = extension_or_builder_list
        if options_or_builder is not UNSET:
            field_dict["optionsOrBuilder"] = options_or_builder
        if name_bytes is not UNSET:
            field_dict["nameBytes"] = name_bytes
        if field_list is not UNSET:
            field_dict["fieldList"] = field_list
        if field_or_builder_list is not UNSET:
            field_dict["fieldOrBuilderList"] = field_or_builder_list
        if nested_type_list is not UNSET:
            field_dict["nestedTypeList"] = nested_type_list
        if nested_type_or_builder_list is not UNSET:
            field_dict["nestedTypeOrBuilderList"] = nested_type_or_builder_list
        if extension_range_or_builder_list is not UNSET:
            field_dict["extensionRangeOrBuilderList"] = extension_range_or_builder_list
        if oneof_decl_list is not UNSET:
            field_dict["oneofDeclList"] = oneof_decl_list
        if oneof_decl_or_builder_list is not UNSET:
            field_dict["oneofDeclOrBuilderList"] = oneof_decl_or_builder_list
        if reserved_range_count is not UNSET:
            field_dict["reservedRangeCount"] = reserved_range_count
        if reserved_range_or_builder_list is not UNSET:
            field_dict["reservedRangeOrBuilderList"] = reserved_range_or_builder_list
        if reserved_name_count is not UNSET:
            field_dict["reservedNameCount"] = reserved_name_count
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
        from ..models.descriptor_proto_all_fields import DescriptorProtoAllFields
        from ..models.descriptor_proto_or_builder import DescriptorProtoOrBuilder
        from ..models.enum_descriptor_proto import EnumDescriptorProto
        from ..models.enum_descriptor_proto_or_builder import EnumDescriptorProtoOrBuilder
        from ..models.extension_range import ExtensionRange
        from ..models.extension_range_or_builder import ExtensionRangeOrBuilder
        from ..models.field_descriptor_proto import FieldDescriptorProto
        from ..models.field_descriptor_proto_or_builder import FieldDescriptorProtoOrBuilder
        from ..models.message_options import MessageOptions
        from ..models.message_options_or_builder import MessageOptionsOrBuilder
        from ..models.oneof_descriptor_proto import OneofDescriptorProto
        from ..models.oneof_descriptor_proto_or_builder import OneofDescriptorProtoOrBuilder
        from ..models.parser_descriptor_proto import ParserDescriptorProto
        from ..models.reserved_range import ReservedRange
        from ..models.reserved_range_or_builder import ReservedRangeOrBuilder
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
        options: MessageOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = MessageOptions.from_dict(_options)

        field_count = d.pop("fieldCount", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: DescriptorProto | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = DescriptorProto.from_dict(_default_instance_for_type)

        _reserved_range_list = d.pop("reservedRangeList", UNSET)
        reserved_range_list: list[ReservedRange] | Unset = UNSET
        if _reserved_range_list is not UNSET:
            reserved_range_list = []
            for reserved_range_list_item_data in _reserved_range_list:
                reserved_range_list_item = ReservedRange.from_dict(reserved_range_list_item_data)

                reserved_range_list.append(reserved_range_list_item)

        reserved_name_list = cast(list[str], d.pop("reservedNameList", UNSET))

        _extension_range_list = d.pop("extensionRangeList", UNSET)
        extension_range_list: list[ExtensionRange] | Unset = UNSET
        if _extension_range_list is not UNSET:
            extension_range_list = []
            for extension_range_list_item_data in _extension_range_list:
                extension_range_list_item = ExtensionRange.from_dict(extension_range_list_item_data)

                extension_range_list.append(extension_range_list_item)

        oneof_decl_count = d.pop("oneofDeclCount", UNSET)

        nested_type_count = d.pop("nestedTypeCount", UNSET)

        enum_type_count = d.pop("enumTypeCount", UNSET)

        extension_count = d.pop("extensionCount", UNSET)

        extension_range_count = d.pop("extensionRangeCount", UNSET)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserDescriptorProto | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserDescriptorProto.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _enum_type_list = d.pop("enumTypeList", UNSET)
        enum_type_list: list[EnumDescriptorProto] | Unset = UNSET
        if _enum_type_list is not UNSET:
            enum_type_list = []
            for enum_type_list_item_data in _enum_type_list:
                enum_type_list_item = EnumDescriptorProto.from_dict(enum_type_list_item_data)

                enum_type_list.append(enum_type_list_item)

        _enum_type_or_builder_list = d.pop("enumTypeOrBuilderList", UNSET)
        enum_type_or_builder_list: list[EnumDescriptorProtoOrBuilder] | Unset = UNSET
        if _enum_type_or_builder_list is not UNSET:
            enum_type_or_builder_list = []
            for enum_type_or_builder_list_item_data in _enum_type_or_builder_list:
                enum_type_or_builder_list_item = EnumDescriptorProtoOrBuilder.from_dict(
                    enum_type_or_builder_list_item_data
                )

                enum_type_or_builder_list.append(enum_type_or_builder_list_item)

        _extension_list = d.pop("extensionList", UNSET)
        extension_list: list[FieldDescriptorProto] | Unset = UNSET
        if _extension_list is not UNSET:
            extension_list = []
            for extension_list_item_data in _extension_list:
                extension_list_item = FieldDescriptorProto.from_dict(extension_list_item_data)

                extension_list.append(extension_list_item)

        _extension_or_builder_list = d.pop("extensionOrBuilderList", UNSET)
        extension_or_builder_list: list[FieldDescriptorProtoOrBuilder] | Unset = UNSET
        if _extension_or_builder_list is not UNSET:
            extension_or_builder_list = []
            for extension_or_builder_list_item_data in _extension_or_builder_list:
                extension_or_builder_list_item = FieldDescriptorProtoOrBuilder.from_dict(
                    extension_or_builder_list_item_data
                )

                extension_or_builder_list.append(extension_or_builder_list_item)

        _options_or_builder = d.pop("optionsOrBuilder", UNSET)
        options_or_builder: MessageOptionsOrBuilder | Unset
        if isinstance(_options_or_builder, Unset):
            options_or_builder = UNSET
        else:
            options_or_builder = MessageOptionsOrBuilder.from_dict(_options_or_builder)

        _name_bytes = d.pop("nameBytes", UNSET)
        name_bytes: ByteString | Unset
        if isinstance(_name_bytes, Unset):
            name_bytes = UNSET
        else:
            name_bytes = ByteString.from_dict(_name_bytes)

        _field_list = d.pop("fieldList", UNSET)
        field_list: list[FieldDescriptorProto] | Unset = UNSET
        if _field_list is not UNSET:
            field_list = []
            for field_list_item_data in _field_list:
                field_list_item = FieldDescriptorProto.from_dict(field_list_item_data)

                field_list.append(field_list_item)

        _field_or_builder_list = d.pop("fieldOrBuilderList", UNSET)
        field_or_builder_list: list[FieldDescriptorProtoOrBuilder] | Unset = UNSET
        if _field_or_builder_list is not UNSET:
            field_or_builder_list = []
            for field_or_builder_list_item_data in _field_or_builder_list:
                field_or_builder_list_item = FieldDescriptorProtoOrBuilder.from_dict(field_or_builder_list_item_data)

                field_or_builder_list.append(field_or_builder_list_item)

        _nested_type_list = d.pop("nestedTypeList", UNSET)
        nested_type_list: list[DescriptorProto] | Unset = UNSET
        if _nested_type_list is not UNSET:
            nested_type_list = []
            for nested_type_list_item_data in _nested_type_list:
                nested_type_list_item = DescriptorProto.from_dict(nested_type_list_item_data)

                nested_type_list.append(nested_type_list_item)

        _nested_type_or_builder_list = d.pop("nestedTypeOrBuilderList", UNSET)
        nested_type_or_builder_list: list[DescriptorProtoOrBuilder] | Unset = UNSET
        if _nested_type_or_builder_list is not UNSET:
            nested_type_or_builder_list = []
            for nested_type_or_builder_list_item_data in _nested_type_or_builder_list:
                nested_type_or_builder_list_item = DescriptorProtoOrBuilder.from_dict(
                    nested_type_or_builder_list_item_data
                )

                nested_type_or_builder_list.append(nested_type_or_builder_list_item)

        _extension_range_or_builder_list = d.pop("extensionRangeOrBuilderList", UNSET)
        extension_range_or_builder_list: list[ExtensionRangeOrBuilder] | Unset = UNSET
        if _extension_range_or_builder_list is not UNSET:
            extension_range_or_builder_list = []
            for extension_range_or_builder_list_item_data in _extension_range_or_builder_list:
                extension_range_or_builder_list_item = ExtensionRangeOrBuilder.from_dict(
                    extension_range_or_builder_list_item_data
                )

                extension_range_or_builder_list.append(extension_range_or_builder_list_item)

        _oneof_decl_list = d.pop("oneofDeclList", UNSET)
        oneof_decl_list: list[OneofDescriptorProto] | Unset = UNSET
        if _oneof_decl_list is not UNSET:
            oneof_decl_list = []
            for oneof_decl_list_item_data in _oneof_decl_list:
                oneof_decl_list_item = OneofDescriptorProto.from_dict(oneof_decl_list_item_data)

                oneof_decl_list.append(oneof_decl_list_item)

        _oneof_decl_or_builder_list = d.pop("oneofDeclOrBuilderList", UNSET)
        oneof_decl_or_builder_list: list[OneofDescriptorProtoOrBuilder] | Unset = UNSET
        if _oneof_decl_or_builder_list is not UNSET:
            oneof_decl_or_builder_list = []
            for oneof_decl_or_builder_list_item_data in _oneof_decl_or_builder_list:
                oneof_decl_or_builder_list_item = OneofDescriptorProtoOrBuilder.from_dict(
                    oneof_decl_or_builder_list_item_data
                )

                oneof_decl_or_builder_list.append(oneof_decl_or_builder_list_item)

        reserved_range_count = d.pop("reservedRangeCount", UNSET)

        _reserved_range_or_builder_list = d.pop("reservedRangeOrBuilderList", UNSET)
        reserved_range_or_builder_list: list[ReservedRangeOrBuilder] | Unset = UNSET
        if _reserved_range_or_builder_list is not UNSET:
            reserved_range_or_builder_list = []
            for reserved_range_or_builder_list_item_data in _reserved_range_or_builder_list:
                reserved_range_or_builder_list_item = ReservedRangeOrBuilder.from_dict(
                    reserved_range_or_builder_list_item_data
                )

                reserved_range_or_builder_list.append(reserved_range_or_builder_list_item)

        reserved_name_count = d.pop("reservedNameCount", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: DescriptorProtoAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = DescriptorProtoAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        descriptor_proto = cls(
            unknown_fields=unknown_fields,
            name=name,
            initialized=initialized,
            options=options,
            field_count=field_count,
            default_instance_for_type=default_instance_for_type,
            reserved_range_list=reserved_range_list,
            reserved_name_list=reserved_name_list,
            extension_range_list=extension_range_list,
            oneof_decl_count=oneof_decl_count,
            nested_type_count=nested_type_count,
            enum_type_count=enum_type_count,
            extension_count=extension_count,
            extension_range_count=extension_range_count,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            enum_type_list=enum_type_list,
            enum_type_or_builder_list=enum_type_or_builder_list,
            extension_list=extension_list,
            extension_or_builder_list=extension_or_builder_list,
            options_or_builder=options_or_builder,
            name_bytes=name_bytes,
            field_list=field_list,
            field_or_builder_list=field_or_builder_list,
            nested_type_list=nested_type_list,
            nested_type_or_builder_list=nested_type_or_builder_list,
            extension_range_or_builder_list=extension_range_or_builder_list,
            oneof_decl_list=oneof_decl_list,
            oneof_decl_or_builder_list=oneof_decl_or_builder_list,
            reserved_range_count=reserved_range_count,
            reserved_range_or_builder_list=reserved_range_or_builder_list,
            reserved_name_count=reserved_name_count,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        descriptor_proto.additional_properties = d
        return descriptor_proto

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
