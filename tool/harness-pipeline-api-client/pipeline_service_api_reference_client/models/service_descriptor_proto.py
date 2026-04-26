from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.method_descriptor_proto import MethodDescriptorProto
    from ..models.method_descriptor_proto_or_builder import MethodDescriptorProtoOrBuilder
    from ..models.parser_service_descriptor_proto import ParserServiceDescriptorProto
    from ..models.service_descriptor_proto_all_fields import ServiceDescriptorProtoAllFields
    from ..models.service_options import ServiceOptions
    from ..models.service_options_or_builder import ServiceOptionsOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="ServiceDescriptorProto")


@_attrs_define
class ServiceDescriptorProto:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        name (str | Unset):
        initialized (bool | Unset):
        options (ServiceOptions | Unset):
        default_instance_for_type (ServiceDescriptorProto | Unset):
        parser_for_type (ParserServiceDescriptorProto | Unset):
        serialized_size (int | Unset):
        options_or_builder (ServiceOptionsOrBuilder | Unset):
        name_bytes (ByteString | Unset):
        method_count (int | Unset):
        method_or_builder_list (list[MethodDescriptorProtoOrBuilder] | Unset):
        method_list (list[MethodDescriptorProto] | Unset):
        all_fields (ServiceDescriptorProtoAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    name: str | Unset = UNSET
    initialized: bool | Unset = UNSET
    options: ServiceOptions | Unset = UNSET
    default_instance_for_type: ServiceDescriptorProto | Unset = UNSET
    parser_for_type: ParserServiceDescriptorProto | Unset = UNSET
    serialized_size: int | Unset = UNSET
    options_or_builder: ServiceOptionsOrBuilder | Unset = UNSET
    name_bytes: ByteString | Unset = UNSET
    method_count: int | Unset = UNSET
    method_or_builder_list: list[MethodDescriptorProtoOrBuilder] | Unset = UNSET
    method_list: list[MethodDescriptorProto] | Unset = UNSET
    all_fields: ServiceDescriptorProtoAllFields | Unset = UNSET
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

        method_count = self.method_count

        method_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.method_or_builder_list, Unset):
            method_or_builder_list = []
            for method_or_builder_list_item_data in self.method_or_builder_list:
                method_or_builder_list_item = method_or_builder_list_item_data.to_dict()
                method_or_builder_list.append(method_or_builder_list_item)

        method_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.method_list, Unset):
            method_list = []
            for method_list_item_data in self.method_list:
                method_list_item = method_list_item_data.to_dict()
                method_list.append(method_list_item)

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
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if options_or_builder is not UNSET:
            field_dict["optionsOrBuilder"] = options_or_builder
        if name_bytes is not UNSET:
            field_dict["nameBytes"] = name_bytes
        if method_count is not UNSET:
            field_dict["methodCount"] = method_count
        if method_or_builder_list is not UNSET:
            field_dict["methodOrBuilderList"] = method_or_builder_list
        if method_list is not UNSET:
            field_dict["methodList"] = method_list
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
        from ..models.method_descriptor_proto import MethodDescriptorProto
        from ..models.method_descriptor_proto_or_builder import MethodDescriptorProtoOrBuilder
        from ..models.parser_service_descriptor_proto import ParserServiceDescriptorProto
        from ..models.service_descriptor_proto_all_fields import ServiceDescriptorProtoAllFields
        from ..models.service_options import ServiceOptions
        from ..models.service_options_or_builder import ServiceOptionsOrBuilder
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
        options: ServiceOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = ServiceOptions.from_dict(_options)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: ServiceDescriptorProto | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = ServiceDescriptorProto.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserServiceDescriptorProto | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserServiceDescriptorProto.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _options_or_builder = d.pop("optionsOrBuilder", UNSET)
        options_or_builder: ServiceOptionsOrBuilder | Unset
        if isinstance(_options_or_builder, Unset):
            options_or_builder = UNSET
        else:
            options_or_builder = ServiceOptionsOrBuilder.from_dict(_options_or_builder)

        _name_bytes = d.pop("nameBytes", UNSET)
        name_bytes: ByteString | Unset
        if isinstance(_name_bytes, Unset):
            name_bytes = UNSET
        else:
            name_bytes = ByteString.from_dict(_name_bytes)

        method_count = d.pop("methodCount", UNSET)

        _method_or_builder_list = d.pop("methodOrBuilderList", UNSET)
        method_or_builder_list: list[MethodDescriptorProtoOrBuilder] | Unset = UNSET
        if _method_or_builder_list is not UNSET:
            method_or_builder_list = []
            for method_or_builder_list_item_data in _method_or_builder_list:
                method_or_builder_list_item = MethodDescriptorProtoOrBuilder.from_dict(method_or_builder_list_item_data)

                method_or_builder_list.append(method_or_builder_list_item)

        _method_list = d.pop("methodList", UNSET)
        method_list: list[MethodDescriptorProto] | Unset = UNSET
        if _method_list is not UNSET:
            method_list = []
            for method_list_item_data in _method_list:
                method_list_item = MethodDescriptorProto.from_dict(method_list_item_data)

                method_list.append(method_list_item)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: ServiceDescriptorProtoAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = ServiceDescriptorProtoAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        service_descriptor_proto = cls(
            unknown_fields=unknown_fields,
            name=name,
            initialized=initialized,
            options=options,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            options_or_builder=options_or_builder,
            name_bytes=name_bytes,
            method_count=method_count,
            method_or_builder_list=method_or_builder_list,
            method_list=method_list,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        service_descriptor_proto.additional_properties = d
        return service_descriptor_proto

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
