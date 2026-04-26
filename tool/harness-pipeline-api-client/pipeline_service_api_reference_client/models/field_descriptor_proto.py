from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_descriptor_proto_label import FieldDescriptorProtoLabel, check_field_descriptor_proto_label
from ..models.field_descriptor_proto_type import FieldDescriptorProtoType, check_field_descriptor_proto_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.field_descriptor_proto_all_fields import FieldDescriptorProtoAllFields
    from ..models.field_options import FieldOptions
    from ..models.field_options_or_builder import FieldOptionsOrBuilder
    from ..models.parser_field_descriptor_proto import ParserFieldDescriptorProto
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="FieldDescriptorProto")


@_attrs_define
class FieldDescriptorProto:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        label (FieldDescriptorProtoLabel | Unset):
        name (str | Unset):
        type_name (str | Unset):
        type_ (FieldDescriptorProtoType | Unset):
        default_value (str | Unset):
        number (int | Unset):
        initialized (bool | Unset):
        options (FieldOptions | Unset):
        default_instance_for_type (FieldDescriptorProto | Unset):
        parser_for_type (ParserFieldDescriptorProto | Unset):
        serialized_size (int | Unset):
        options_or_builder (FieldOptionsOrBuilder | Unset):
        name_bytes (ByteString | Unset):
        json_name (str | Unset):
        proto_3_optional (bool | Unset):
        oneof_index (int | Unset):
        extendee (str | Unset):
        extendee_bytes (ByteString | Unset):
        default_value_bytes (ByteString | Unset):
        json_name_bytes (ByteString | Unset):
        type_name_bytes (ByteString | Unset):
        all_fields (FieldDescriptorProtoAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    label: FieldDescriptorProtoLabel | Unset = UNSET
    name: str | Unset = UNSET
    type_name: str | Unset = UNSET
    type_: FieldDescriptorProtoType | Unset = UNSET
    default_value: str | Unset = UNSET
    number: int | Unset = UNSET
    initialized: bool | Unset = UNSET
    options: FieldOptions | Unset = UNSET
    default_instance_for_type: FieldDescriptorProto | Unset = UNSET
    parser_for_type: ParserFieldDescriptorProto | Unset = UNSET
    serialized_size: int | Unset = UNSET
    options_or_builder: FieldOptionsOrBuilder | Unset = UNSET
    name_bytes: ByteString | Unset = UNSET
    json_name: str | Unset = UNSET
    proto_3_optional: bool | Unset = UNSET
    oneof_index: int | Unset = UNSET
    extendee: str | Unset = UNSET
    extendee_bytes: ByteString | Unset = UNSET
    default_value_bytes: ByteString | Unset = UNSET
    json_name_bytes: ByteString | Unset = UNSET
    type_name_bytes: ByteString | Unset = UNSET
    all_fields: FieldDescriptorProtoAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        label: str | Unset = UNSET
        if not isinstance(self.label, Unset):
            label = self.label

        name = self.name

        type_name = self.type_name

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        default_value = self.default_value

        number = self.number

        initialized = self.initialized

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

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

        json_name = self.json_name

        proto_3_optional = self.proto_3_optional

        oneof_index = self.oneof_index

        extendee = self.extendee

        extendee_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extendee_bytes, Unset):
            extendee_bytes = self.extendee_bytes.to_dict()

        default_value_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_value_bytes, Unset):
            default_value_bytes = self.default_value_bytes.to_dict()

        json_name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.json_name_bytes, Unset):
            json_name_bytes = self.json_name_bytes.to_dict()

        type_name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_name_bytes, Unset):
            type_name_bytes = self.type_name_bytes.to_dict()

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
        if label is not UNSET:
            field_dict["label"] = label
        if name is not UNSET:
            field_dict["name"] = name
        if type_name is not UNSET:
            field_dict["typeName"] = type_name
        if type_ is not UNSET:
            field_dict["type"] = type_
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if number is not UNSET:
            field_dict["number"] = number
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if options is not UNSET:
            field_dict["options"] = options
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if options_or_builder is not UNSET:
            field_dict["optionsOrBuilder"] = options_or_builder
        if name_bytes is not UNSET:
            field_dict["nameBytes"] = name_bytes
        if json_name is not UNSET:
            field_dict["jsonName"] = json_name
        if proto_3_optional is not UNSET:
            field_dict["proto3Optional"] = proto_3_optional
        if oneof_index is not UNSET:
            field_dict["oneofIndex"] = oneof_index
        if extendee is not UNSET:
            field_dict["extendee"] = extendee
        if extendee_bytes is not UNSET:
            field_dict["extendeeBytes"] = extendee_bytes
        if default_value_bytes is not UNSET:
            field_dict["defaultValueBytes"] = default_value_bytes
        if json_name_bytes is not UNSET:
            field_dict["jsonNameBytes"] = json_name_bytes
        if type_name_bytes is not UNSET:
            field_dict["typeNameBytes"] = type_name_bytes
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
        from ..models.field_descriptor_proto_all_fields import FieldDescriptorProtoAllFields
        from ..models.field_options import FieldOptions
        from ..models.field_options_or_builder import FieldOptionsOrBuilder
        from ..models.parser_field_descriptor_proto import ParserFieldDescriptorProto
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        _label = d.pop("label", UNSET)
        label: FieldDescriptorProtoLabel | Unset
        if isinstance(_label, Unset):
            label = UNSET
        else:
            label = check_field_descriptor_proto_label(_label)

        name = d.pop("name", UNSET)

        type_name = d.pop("typeName", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: FieldDescriptorProtoType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_field_descriptor_proto_type(_type_)

        default_value = d.pop("defaultValue", UNSET)

        number = d.pop("number", UNSET)

        initialized = d.pop("initialized", UNSET)

        _options = d.pop("options", UNSET)
        options: FieldOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = FieldOptions.from_dict(_options)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: FieldDescriptorProto | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = FieldDescriptorProto.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserFieldDescriptorProto | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserFieldDescriptorProto.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _options_or_builder = d.pop("optionsOrBuilder", UNSET)
        options_or_builder: FieldOptionsOrBuilder | Unset
        if isinstance(_options_or_builder, Unset):
            options_or_builder = UNSET
        else:
            options_or_builder = FieldOptionsOrBuilder.from_dict(_options_or_builder)

        _name_bytes = d.pop("nameBytes", UNSET)
        name_bytes: ByteString | Unset
        if isinstance(_name_bytes, Unset):
            name_bytes = UNSET
        else:
            name_bytes = ByteString.from_dict(_name_bytes)

        json_name = d.pop("jsonName", UNSET)

        proto_3_optional = d.pop("proto3Optional", UNSET)

        oneof_index = d.pop("oneofIndex", UNSET)

        extendee = d.pop("extendee", UNSET)

        _extendee_bytes = d.pop("extendeeBytes", UNSET)
        extendee_bytes: ByteString | Unset
        if isinstance(_extendee_bytes, Unset):
            extendee_bytes = UNSET
        else:
            extendee_bytes = ByteString.from_dict(_extendee_bytes)

        _default_value_bytes = d.pop("defaultValueBytes", UNSET)
        default_value_bytes: ByteString | Unset
        if isinstance(_default_value_bytes, Unset):
            default_value_bytes = UNSET
        else:
            default_value_bytes = ByteString.from_dict(_default_value_bytes)

        _json_name_bytes = d.pop("jsonNameBytes", UNSET)
        json_name_bytes: ByteString | Unset
        if isinstance(_json_name_bytes, Unset):
            json_name_bytes = UNSET
        else:
            json_name_bytes = ByteString.from_dict(_json_name_bytes)

        _type_name_bytes = d.pop("typeNameBytes", UNSET)
        type_name_bytes: ByteString | Unset
        if isinstance(_type_name_bytes, Unset):
            type_name_bytes = UNSET
        else:
            type_name_bytes = ByteString.from_dict(_type_name_bytes)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: FieldDescriptorProtoAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = FieldDescriptorProtoAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        field_descriptor_proto = cls(
            unknown_fields=unknown_fields,
            label=label,
            name=name,
            type_name=type_name,
            type_=type_,
            default_value=default_value,
            number=number,
            initialized=initialized,
            options=options,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            options_or_builder=options_or_builder,
            name_bytes=name_bytes,
            json_name=json_name,
            proto_3_optional=proto_3_optional,
            oneof_index=oneof_index,
            extendee=extendee,
            extendee_bytes=extendee_bytes,
            default_value_bytes=default_value_bytes,
            json_name_bytes=json_name_bytes,
            type_name_bytes=type_name_bytes,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        field_descriptor_proto.additional_properties = d
        return field_descriptor_proto

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
