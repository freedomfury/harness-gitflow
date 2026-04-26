from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.method_descriptor_proto_all_fields import MethodDescriptorProtoAllFields
    from ..models.method_options import MethodOptions
    from ..models.method_options_or_builder import MethodOptionsOrBuilder
    from ..models.parser_method_descriptor_proto import ParserMethodDescriptorProto
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="MethodDescriptorProto")


@_attrs_define
class MethodDescriptorProto:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        input_type_bytes (ByteString | Unset):
        output_type_bytes (ByteString | Unset):
        client_streaming (bool | Unset):
        server_streaming (bool | Unset):
        input_type (str | Unset):
        options_or_builder (MethodOptionsOrBuilder | Unset):
        name (str | Unset):
        parser_for_type (ParserMethodDescriptorProto | Unset):
        serialized_size (int | Unset):
        output_type (str | Unset):
        name_bytes (ByteString | Unset):
        default_instance_for_type (MethodDescriptorProto | Unset):
        initialized (bool | Unset):
        options (MethodOptions | Unset):
        initialization_error_string (str | Unset):
        all_fields (MethodDescriptorProtoAllFields | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    input_type_bytes: ByteString | Unset = UNSET
    output_type_bytes: ByteString | Unset = UNSET
    client_streaming: bool | Unset = UNSET
    server_streaming: bool | Unset = UNSET
    input_type: str | Unset = UNSET
    options_or_builder: MethodOptionsOrBuilder | Unset = UNSET
    name: str | Unset = UNSET
    parser_for_type: ParserMethodDescriptorProto | Unset = UNSET
    serialized_size: int | Unset = UNSET
    output_type: str | Unset = UNSET
    name_bytes: ByteString | Unset = UNSET
    default_instance_for_type: MethodDescriptorProto | Unset = UNSET
    initialized: bool | Unset = UNSET
    options: MethodOptions | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    all_fields: MethodDescriptorProtoAllFields | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        input_type_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_type_bytes, Unset):
            input_type_bytes = self.input_type_bytes.to_dict()

        output_type_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output_type_bytes, Unset):
            output_type_bytes = self.output_type_bytes.to_dict()

        client_streaming = self.client_streaming

        server_streaming = self.server_streaming

        input_type = self.input_type

        options_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options_or_builder, Unset):
            options_or_builder = self.options_or_builder.to_dict()

        name = self.name

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        output_type = self.output_type

        name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name_bytes, Unset):
            name_bytes = self.name_bytes.to_dict()

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        initialized = self.initialized

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        initialization_error_string = self.initialization_error_string

        all_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields, Unset):
            all_fields = self.all_fields.to_dict()

        descriptor_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.descriptor_for_type, Unset):
            descriptor_for_type = self.descriptor_for_type.to_dict()

        memoized_serialized_size = self.memoized_serialized_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unknown_fields is not UNSET:
            field_dict["unknownFields"] = unknown_fields
        if input_type_bytes is not UNSET:
            field_dict["inputTypeBytes"] = input_type_bytes
        if output_type_bytes is not UNSET:
            field_dict["outputTypeBytes"] = output_type_bytes
        if client_streaming is not UNSET:
            field_dict["clientStreaming"] = client_streaming
        if server_streaming is not UNSET:
            field_dict["serverStreaming"] = server_streaming
        if input_type is not UNSET:
            field_dict["inputType"] = input_type
        if options_or_builder is not UNSET:
            field_dict["optionsOrBuilder"] = options_or_builder
        if name is not UNSET:
            field_dict["name"] = name
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if output_type is not UNSET:
            field_dict["outputType"] = output_type
        if name_bytes is not UNSET:
            field_dict["nameBytes"] = name_bytes
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if options is not UNSET:
            field_dict["options"] = options
        if initialization_error_string is not UNSET:
            field_dict["initializationErrorString"] = initialization_error_string
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if descriptor_for_type is not UNSET:
            field_dict["descriptorForType"] = descriptor_for_type
        if memoized_serialized_size is not UNSET:
            field_dict["memoizedSerializedSize"] = memoized_serialized_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.method_descriptor_proto_all_fields import MethodDescriptorProtoAllFields
        from ..models.method_options import MethodOptions
        from ..models.method_options_or_builder import MethodOptionsOrBuilder
        from ..models.parser_method_descriptor_proto import ParserMethodDescriptorProto
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        _input_type_bytes = d.pop("inputTypeBytes", UNSET)
        input_type_bytes: ByteString | Unset
        if isinstance(_input_type_bytes, Unset):
            input_type_bytes = UNSET
        else:
            input_type_bytes = ByteString.from_dict(_input_type_bytes)

        _output_type_bytes = d.pop("outputTypeBytes", UNSET)
        output_type_bytes: ByteString | Unset
        if isinstance(_output_type_bytes, Unset):
            output_type_bytes = UNSET
        else:
            output_type_bytes = ByteString.from_dict(_output_type_bytes)

        client_streaming = d.pop("clientStreaming", UNSET)

        server_streaming = d.pop("serverStreaming", UNSET)

        input_type = d.pop("inputType", UNSET)

        _options_or_builder = d.pop("optionsOrBuilder", UNSET)
        options_or_builder: MethodOptionsOrBuilder | Unset
        if isinstance(_options_or_builder, Unset):
            options_or_builder = UNSET
        else:
            options_or_builder = MethodOptionsOrBuilder.from_dict(_options_or_builder)

        name = d.pop("name", UNSET)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserMethodDescriptorProto | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserMethodDescriptorProto.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        output_type = d.pop("outputType", UNSET)

        _name_bytes = d.pop("nameBytes", UNSET)
        name_bytes: ByteString | Unset
        if isinstance(_name_bytes, Unset):
            name_bytes = UNSET
        else:
            name_bytes = ByteString.from_dict(_name_bytes)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: MethodDescriptorProto | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = MethodDescriptorProto.from_dict(_default_instance_for_type)

        initialized = d.pop("initialized", UNSET)

        _options = d.pop("options", UNSET)
        options: MethodOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = MethodOptions.from_dict(_options)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: MethodDescriptorProtoAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = MethodDescriptorProtoAllFields.from_dict(_all_fields)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        method_descriptor_proto = cls(
            unknown_fields=unknown_fields,
            input_type_bytes=input_type_bytes,
            output_type_bytes=output_type_bytes,
            client_streaming=client_streaming,
            server_streaming=server_streaming,
            input_type=input_type,
            options_or_builder=options_or_builder,
            name=name,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            output_type=output_type,
            name_bytes=name_bytes,
            default_instance_for_type=default_instance_for_type,
            initialized=initialized,
            options=options,
            initialization_error_string=initialization_error_string,
            all_fields=all_fields,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        method_descriptor_proto.additional_properties = d
        return method_descriptor_proto

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
