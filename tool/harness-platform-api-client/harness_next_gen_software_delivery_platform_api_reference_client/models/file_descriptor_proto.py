from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.file_descriptor_proto_edition import FileDescriptorProtoEdition, check_file_descriptor_proto_edition
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.descriptor_proto import DescriptorProto
    from ..models.descriptor_proto_or_builder import DescriptorProtoOrBuilder
    from ..models.enum_descriptor_proto import EnumDescriptorProto
    from ..models.enum_descriptor_proto_or_builder import EnumDescriptorProtoOrBuilder
    from ..models.field_descriptor_proto import FieldDescriptorProto
    from ..models.field_descriptor_proto_or_builder import FieldDescriptorProtoOrBuilder
    from ..models.file_descriptor_proto_all_fields import FileDescriptorProtoAllFields
    from ..models.file_options import FileOptions
    from ..models.file_options_or_builder import FileOptionsOrBuilder
    from ..models.parser_file_descriptor_proto import ParserFileDescriptorProto
    from ..models.service_descriptor_proto import ServiceDescriptorProto
    from ..models.service_descriptor_proto_or_builder import ServiceDescriptorProtoOrBuilder
    from ..models.source_code_info import SourceCodeInfo
    from ..models.source_code_info_or_builder import SourceCodeInfoOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="FileDescriptorProto")


@_attrs_define
class FileDescriptorProto:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        public_dependency_count (int | Unset):
        dependency_count (int | Unset):
        message_type_count (int | Unset):
        service_count (int | Unset):
        enum_type_count (int | Unset):
        extension_count (int | Unset):
        extension_list (list[FieldDescriptorProto] | Unset):
        extension_or_builder_list (list[FieldDescriptorProtoOrBuilder] | Unset):
        options_or_builder (FileOptionsOrBuilder | Unset):
        source_code_info (SourceCodeInfo | Unset):
        source_code_info_or_builder (SourceCodeInfoOrBuilder | Unset):
        syntax_bytes (ByteString | Unset):
        name (str | Unset):
        package (str | Unset):
        parser_for_type (ParserFileDescriptorProto | Unset):
        serialized_size (int | Unset):
        edition (FileDescriptorProtoEdition | Unset):
        name_bytes (ByteString | Unset):
        package_bytes (ByteString | Unset):
        dependency_list (list[str] | Unset):
        public_dependency_list (list[int] | Unset):
        weak_dependency_list (list[int] | Unset):
        weak_dependency_count (int | Unset):
        message_type_list (list[DescriptorProto] | Unset):
        message_type_or_builder_list (list[DescriptorProtoOrBuilder] | Unset):
        enum_type_list (list[EnumDescriptorProto] | Unset):
        enum_type_or_builder_list (list[EnumDescriptorProtoOrBuilder] | Unset):
        service_list (list[ServiceDescriptorProto] | Unset):
        service_or_builder_list (list[ServiceDescriptorProtoOrBuilder] | Unset):
        syntax (str | Unset):
        default_instance_for_type (FileDescriptorProto | Unset):
        initialized (bool | Unset):
        options (FileOptions | Unset):
        initialization_error_string (str | Unset):
        all_fields (FileDescriptorProtoAllFields | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    public_dependency_count: int | Unset = UNSET
    dependency_count: int | Unset = UNSET
    message_type_count: int | Unset = UNSET
    service_count: int | Unset = UNSET
    enum_type_count: int | Unset = UNSET
    extension_count: int | Unset = UNSET
    extension_list: list[FieldDescriptorProto] | Unset = UNSET
    extension_or_builder_list: list[FieldDescriptorProtoOrBuilder] | Unset = UNSET
    options_or_builder: FileOptionsOrBuilder | Unset = UNSET
    source_code_info: SourceCodeInfo | Unset = UNSET
    source_code_info_or_builder: SourceCodeInfoOrBuilder | Unset = UNSET
    syntax_bytes: ByteString | Unset = UNSET
    name: str | Unset = UNSET
    package: str | Unset = UNSET
    parser_for_type: ParserFileDescriptorProto | Unset = UNSET
    serialized_size: int | Unset = UNSET
    edition: FileDescriptorProtoEdition | Unset = UNSET
    name_bytes: ByteString | Unset = UNSET
    package_bytes: ByteString | Unset = UNSET
    dependency_list: list[str] | Unset = UNSET
    public_dependency_list: list[int] | Unset = UNSET
    weak_dependency_list: list[int] | Unset = UNSET
    weak_dependency_count: int | Unset = UNSET
    message_type_list: list[DescriptorProto] | Unset = UNSET
    message_type_or_builder_list: list[DescriptorProtoOrBuilder] | Unset = UNSET
    enum_type_list: list[EnumDescriptorProto] | Unset = UNSET
    enum_type_or_builder_list: list[EnumDescriptorProtoOrBuilder] | Unset = UNSET
    service_list: list[ServiceDescriptorProto] | Unset = UNSET
    service_or_builder_list: list[ServiceDescriptorProtoOrBuilder] | Unset = UNSET
    syntax: str | Unset = UNSET
    default_instance_for_type: FileDescriptorProto | Unset = UNSET
    initialized: bool | Unset = UNSET
    options: FileOptions | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    all_fields: FileDescriptorProtoAllFields | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        public_dependency_count = self.public_dependency_count

        dependency_count = self.dependency_count

        message_type_count = self.message_type_count

        service_count = self.service_count

        enum_type_count = self.enum_type_count

        extension_count = self.extension_count

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

        source_code_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_code_info, Unset):
            source_code_info = self.source_code_info.to_dict()

        source_code_info_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_code_info_or_builder, Unset):
            source_code_info_or_builder = self.source_code_info_or_builder.to_dict()

        syntax_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.syntax_bytes, Unset):
            syntax_bytes = self.syntax_bytes.to_dict()

        name = self.name

        package = self.package

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        edition: str | Unset = UNSET
        if not isinstance(self.edition, Unset):
            edition = self.edition

        name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name_bytes, Unset):
            name_bytes = self.name_bytes.to_dict()

        package_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.package_bytes, Unset):
            package_bytes = self.package_bytes.to_dict()

        dependency_list: list[str] | Unset = UNSET
        if not isinstance(self.dependency_list, Unset):
            dependency_list = self.dependency_list

        public_dependency_list: list[int] | Unset = UNSET
        if not isinstance(self.public_dependency_list, Unset):
            public_dependency_list = self.public_dependency_list

        weak_dependency_list: list[int] | Unset = UNSET
        if not isinstance(self.weak_dependency_list, Unset):
            weak_dependency_list = self.weak_dependency_list

        weak_dependency_count = self.weak_dependency_count

        message_type_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.message_type_list, Unset):
            message_type_list = []
            for message_type_list_item_data in self.message_type_list:
                message_type_list_item = message_type_list_item_data.to_dict()
                message_type_list.append(message_type_list_item)

        message_type_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.message_type_or_builder_list, Unset):
            message_type_or_builder_list = []
            for message_type_or_builder_list_item_data in self.message_type_or_builder_list:
                message_type_or_builder_list_item = message_type_or_builder_list_item_data.to_dict()
                message_type_or_builder_list.append(message_type_or_builder_list_item)

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

        service_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.service_list, Unset):
            service_list = []
            for service_list_item_data in self.service_list:
                service_list_item = service_list_item_data.to_dict()
                service_list.append(service_list_item)

        service_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.service_or_builder_list, Unset):
            service_or_builder_list = []
            for service_or_builder_list_item_data in self.service_or_builder_list:
                service_or_builder_list_item = service_or_builder_list_item_data.to_dict()
                service_or_builder_list.append(service_or_builder_list_item)

        syntax = self.syntax

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
        if public_dependency_count is not UNSET:
            field_dict["publicDependencyCount"] = public_dependency_count
        if dependency_count is not UNSET:
            field_dict["dependencyCount"] = dependency_count
        if message_type_count is not UNSET:
            field_dict["messageTypeCount"] = message_type_count
        if service_count is not UNSET:
            field_dict["serviceCount"] = service_count
        if enum_type_count is not UNSET:
            field_dict["enumTypeCount"] = enum_type_count
        if extension_count is not UNSET:
            field_dict["extensionCount"] = extension_count
        if extension_list is not UNSET:
            field_dict["extensionList"] = extension_list
        if extension_or_builder_list is not UNSET:
            field_dict["extensionOrBuilderList"] = extension_or_builder_list
        if options_or_builder is not UNSET:
            field_dict["optionsOrBuilder"] = options_or_builder
        if source_code_info is not UNSET:
            field_dict["sourceCodeInfo"] = source_code_info
        if source_code_info_or_builder is not UNSET:
            field_dict["sourceCodeInfoOrBuilder"] = source_code_info_or_builder
        if syntax_bytes is not UNSET:
            field_dict["syntaxBytes"] = syntax_bytes
        if name is not UNSET:
            field_dict["name"] = name
        if package is not UNSET:
            field_dict["package"] = package
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if edition is not UNSET:
            field_dict["edition"] = edition
        if name_bytes is not UNSET:
            field_dict["nameBytes"] = name_bytes
        if package_bytes is not UNSET:
            field_dict["packageBytes"] = package_bytes
        if dependency_list is not UNSET:
            field_dict["dependencyList"] = dependency_list
        if public_dependency_list is not UNSET:
            field_dict["publicDependencyList"] = public_dependency_list
        if weak_dependency_list is not UNSET:
            field_dict["weakDependencyList"] = weak_dependency_list
        if weak_dependency_count is not UNSET:
            field_dict["weakDependencyCount"] = weak_dependency_count
        if message_type_list is not UNSET:
            field_dict["messageTypeList"] = message_type_list
        if message_type_or_builder_list is not UNSET:
            field_dict["messageTypeOrBuilderList"] = message_type_or_builder_list
        if enum_type_list is not UNSET:
            field_dict["enumTypeList"] = enum_type_list
        if enum_type_or_builder_list is not UNSET:
            field_dict["enumTypeOrBuilderList"] = enum_type_or_builder_list
        if service_list is not UNSET:
            field_dict["serviceList"] = service_list
        if service_or_builder_list is not UNSET:
            field_dict["serviceOrBuilderList"] = service_or_builder_list
        if syntax is not UNSET:
            field_dict["syntax"] = syntax
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
        from ..models.descriptor_proto import DescriptorProto
        from ..models.descriptor_proto_or_builder import DescriptorProtoOrBuilder
        from ..models.enum_descriptor_proto import EnumDescriptorProto
        from ..models.enum_descriptor_proto_or_builder import EnumDescriptorProtoOrBuilder
        from ..models.field_descriptor_proto import FieldDescriptorProto
        from ..models.field_descriptor_proto_or_builder import FieldDescriptorProtoOrBuilder
        from ..models.file_descriptor_proto_all_fields import FileDescriptorProtoAllFields
        from ..models.file_options import FileOptions
        from ..models.file_options_or_builder import FileOptionsOrBuilder
        from ..models.parser_file_descriptor_proto import ParserFileDescriptorProto
        from ..models.service_descriptor_proto import ServiceDescriptorProto
        from ..models.service_descriptor_proto_or_builder import ServiceDescriptorProtoOrBuilder
        from ..models.source_code_info import SourceCodeInfo
        from ..models.source_code_info_or_builder import SourceCodeInfoOrBuilder
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        public_dependency_count = d.pop("publicDependencyCount", UNSET)

        dependency_count = d.pop("dependencyCount", UNSET)

        message_type_count = d.pop("messageTypeCount", UNSET)

        service_count = d.pop("serviceCount", UNSET)

        enum_type_count = d.pop("enumTypeCount", UNSET)

        extension_count = d.pop("extensionCount", UNSET)

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
        options_or_builder: FileOptionsOrBuilder | Unset
        if isinstance(_options_or_builder, Unset):
            options_or_builder = UNSET
        else:
            options_or_builder = FileOptionsOrBuilder.from_dict(_options_or_builder)

        _source_code_info = d.pop("sourceCodeInfo", UNSET)
        source_code_info: SourceCodeInfo | Unset
        if isinstance(_source_code_info, Unset):
            source_code_info = UNSET
        else:
            source_code_info = SourceCodeInfo.from_dict(_source_code_info)

        _source_code_info_or_builder = d.pop("sourceCodeInfoOrBuilder", UNSET)
        source_code_info_or_builder: SourceCodeInfoOrBuilder | Unset
        if isinstance(_source_code_info_or_builder, Unset):
            source_code_info_or_builder = UNSET
        else:
            source_code_info_or_builder = SourceCodeInfoOrBuilder.from_dict(_source_code_info_or_builder)

        _syntax_bytes = d.pop("syntaxBytes", UNSET)
        syntax_bytes: ByteString | Unset
        if isinstance(_syntax_bytes, Unset):
            syntax_bytes = UNSET
        else:
            syntax_bytes = ByteString.from_dict(_syntax_bytes)

        name = d.pop("name", UNSET)

        package = d.pop("package", UNSET)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserFileDescriptorProto | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserFileDescriptorProto.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _edition = d.pop("edition", UNSET)
        edition: FileDescriptorProtoEdition | Unset
        if isinstance(_edition, Unset):
            edition = UNSET
        else:
            edition = check_file_descriptor_proto_edition(_edition)

        _name_bytes = d.pop("nameBytes", UNSET)
        name_bytes: ByteString | Unset
        if isinstance(_name_bytes, Unset):
            name_bytes = UNSET
        else:
            name_bytes = ByteString.from_dict(_name_bytes)

        _package_bytes = d.pop("packageBytes", UNSET)
        package_bytes: ByteString | Unset
        if isinstance(_package_bytes, Unset):
            package_bytes = UNSET
        else:
            package_bytes = ByteString.from_dict(_package_bytes)

        dependency_list = cast(list[str], d.pop("dependencyList", UNSET))

        public_dependency_list = cast(list[int], d.pop("publicDependencyList", UNSET))

        weak_dependency_list = cast(list[int], d.pop("weakDependencyList", UNSET))

        weak_dependency_count = d.pop("weakDependencyCount", UNSET)

        _message_type_list = d.pop("messageTypeList", UNSET)
        message_type_list: list[DescriptorProto] | Unset = UNSET
        if _message_type_list is not UNSET:
            message_type_list = []
            for message_type_list_item_data in _message_type_list:
                message_type_list_item = DescriptorProto.from_dict(message_type_list_item_data)

                message_type_list.append(message_type_list_item)

        _message_type_or_builder_list = d.pop("messageTypeOrBuilderList", UNSET)
        message_type_or_builder_list: list[DescriptorProtoOrBuilder] | Unset = UNSET
        if _message_type_or_builder_list is not UNSET:
            message_type_or_builder_list = []
            for message_type_or_builder_list_item_data in _message_type_or_builder_list:
                message_type_or_builder_list_item = DescriptorProtoOrBuilder.from_dict(
                    message_type_or_builder_list_item_data
                )

                message_type_or_builder_list.append(message_type_or_builder_list_item)

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

        _service_list = d.pop("serviceList", UNSET)
        service_list: list[ServiceDescriptorProto] | Unset = UNSET
        if _service_list is not UNSET:
            service_list = []
            for service_list_item_data in _service_list:
                service_list_item = ServiceDescriptorProto.from_dict(service_list_item_data)

                service_list.append(service_list_item)

        _service_or_builder_list = d.pop("serviceOrBuilderList", UNSET)
        service_or_builder_list: list[ServiceDescriptorProtoOrBuilder] | Unset = UNSET
        if _service_or_builder_list is not UNSET:
            service_or_builder_list = []
            for service_or_builder_list_item_data in _service_or_builder_list:
                service_or_builder_list_item = ServiceDescriptorProtoOrBuilder.from_dict(
                    service_or_builder_list_item_data
                )

                service_or_builder_list.append(service_or_builder_list_item)

        syntax = d.pop("syntax", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: FileDescriptorProto | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = FileDescriptorProto.from_dict(_default_instance_for_type)

        initialized = d.pop("initialized", UNSET)

        _options = d.pop("options", UNSET)
        options: FileOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = FileOptions.from_dict(_options)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: FileDescriptorProtoAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = FileDescriptorProtoAllFields.from_dict(_all_fields)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        file_descriptor_proto = cls(
            unknown_fields=unknown_fields,
            public_dependency_count=public_dependency_count,
            dependency_count=dependency_count,
            message_type_count=message_type_count,
            service_count=service_count,
            enum_type_count=enum_type_count,
            extension_count=extension_count,
            extension_list=extension_list,
            extension_or_builder_list=extension_or_builder_list,
            options_or_builder=options_or_builder,
            source_code_info=source_code_info,
            source_code_info_or_builder=source_code_info_or_builder,
            syntax_bytes=syntax_bytes,
            name=name,
            package=package,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            edition=edition,
            name_bytes=name_bytes,
            package_bytes=package_bytes,
            dependency_list=dependency_list,
            public_dependency_list=public_dependency_list,
            weak_dependency_list=weak_dependency_list,
            weak_dependency_count=weak_dependency_count,
            message_type_list=message_type_list,
            message_type_or_builder_list=message_type_or_builder_list,
            enum_type_list=enum_type_list,
            enum_type_or_builder_list=enum_type_or_builder_list,
            service_list=service_list,
            service_or_builder_list=service_or_builder_list,
            syntax=syntax,
            default_instance_for_type=default_instance_for_type,
            initialized=initialized,
            options=options,
            initialization_error_string=initialization_error_string,
            all_fields=all_fields,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        file_descriptor_proto.additional_properties = d
        return file_descriptor_proto

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
