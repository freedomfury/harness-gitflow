from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.message import Message
    from ..models.method_descriptor_proto_or_builder_all_fields import MethodDescriptorProtoOrBuilderAllFields
    from ..models.method_options import MethodOptions
    from ..models.method_options_or_builder import MethodOptionsOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="MethodDescriptorProtoOrBuilder")


@_attrs_define
class MethodDescriptorProtoOrBuilder:
    """
    Attributes:
        input_type_bytes (ByteString | Unset):
        output_type_bytes (ByteString | Unset):
        client_streaming (bool | Unset):
        server_streaming (bool | Unset):
        name (str | Unset):
        options (MethodOptions | Unset):
        output_type (str | Unset):
        input_type (str | Unset):
        options_or_builder (MethodOptionsOrBuilder | Unset):
        name_bytes (ByteString | Unset):
        all_fields (MethodDescriptorProtoOrBuilderAllFields | Unset):
        default_instance_for_type (Message | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        initialized (bool | Unset):
    """

    input_type_bytes: ByteString | Unset = UNSET
    output_type_bytes: ByteString | Unset = UNSET
    client_streaming: bool | Unset = UNSET
    server_streaming: bool | Unset = UNSET
    name: str | Unset = UNSET
    options: MethodOptions | Unset = UNSET
    output_type: str | Unset = UNSET
    input_type: str | Unset = UNSET
    options_or_builder: MethodOptionsOrBuilder | Unset = UNSET
    name_bytes: ByteString | Unset = UNSET
    all_fields: MethodDescriptorProtoOrBuilderAllFields | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        input_type_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_type_bytes, Unset):
            input_type_bytes = self.input_type_bytes.to_dict()

        output_type_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output_type_bytes, Unset):
            output_type_bytes = self.output_type_bytes.to_dict()

        client_streaming = self.client_streaming

        server_streaming = self.server_streaming

        name = self.name

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        output_type = self.output_type

        input_type = self.input_type

        options_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options_or_builder, Unset):
            options_or_builder = self.options_or_builder.to_dict()

        name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name_bytes, Unset):
            name_bytes = self.name_bytes.to_dict()

        all_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields, Unset):
            all_fields = self.all_fields.to_dict()

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        initialization_error_string = self.initialization_error_string

        descriptor_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.descriptor_for_type, Unset):
            descriptor_for_type = self.descriptor_for_type.to_dict()

        initialized = self.initialized

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if input_type_bytes is not UNSET:
            field_dict["inputTypeBytes"] = input_type_bytes
        if output_type_bytes is not UNSET:
            field_dict["outputTypeBytes"] = output_type_bytes
        if client_streaming is not UNSET:
            field_dict["clientStreaming"] = client_streaming
        if server_streaming is not UNSET:
            field_dict["serverStreaming"] = server_streaming
        if name is not UNSET:
            field_dict["name"] = name
        if options is not UNSET:
            field_dict["options"] = options
        if output_type is not UNSET:
            field_dict["outputType"] = output_type
        if input_type is not UNSET:
            field_dict["inputType"] = input_type
        if options_or_builder is not UNSET:
            field_dict["optionsOrBuilder"] = options_or_builder
        if name_bytes is not UNSET:
            field_dict["nameBytes"] = name_bytes
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if unknown_fields is not UNSET:
            field_dict["unknownFields"] = unknown_fields
        if initialization_error_string is not UNSET:
            field_dict["initializationErrorString"] = initialization_error_string
        if descriptor_for_type is not UNSET:
            field_dict["descriptorForType"] = descriptor_for_type
        if initialized is not UNSET:
            field_dict["initialized"] = initialized

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.message import Message
        from ..models.method_descriptor_proto_or_builder_all_fields import MethodDescriptorProtoOrBuilderAllFields
        from ..models.method_options import MethodOptions
        from ..models.method_options_or_builder import MethodOptionsOrBuilder
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
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

        name = d.pop("name", UNSET)

        _options = d.pop("options", UNSET)
        options: MethodOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = MethodOptions.from_dict(_options)

        output_type = d.pop("outputType", UNSET)

        input_type = d.pop("inputType", UNSET)

        _options_or_builder = d.pop("optionsOrBuilder", UNSET)
        options_or_builder: MethodOptionsOrBuilder | Unset
        if isinstance(_options_or_builder, Unset):
            options_or_builder = UNSET
        else:
            options_or_builder = MethodOptionsOrBuilder.from_dict(_options_or_builder)

        _name_bytes = d.pop("nameBytes", UNSET)
        name_bytes: ByteString | Unset
        if isinstance(_name_bytes, Unset):
            name_bytes = UNSET
        else:
            name_bytes = ByteString.from_dict(_name_bytes)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: MethodDescriptorProtoOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = MethodDescriptorProtoOrBuilderAllFields.from_dict(_all_fields)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: Message | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = Message.from_dict(_default_instance_for_type)

        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        initialized = d.pop("initialized", UNSET)

        method_descriptor_proto_or_builder = cls(
            input_type_bytes=input_type_bytes,
            output_type_bytes=output_type_bytes,
            client_streaming=client_streaming,
            server_streaming=server_streaming,
            name=name,
            options=options,
            output_type=output_type,
            input_type=input_type,
            options_or_builder=options_or_builder,
            name_bytes=name_bytes,
            all_fields=all_fields,
            default_instance_for_type=default_instance_for_type,
            unknown_fields=unknown_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            initialized=initialized,
        )

        method_descriptor_proto_or_builder.additional_properties = d
        return method_descriptor_proto_or_builder

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
