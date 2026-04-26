from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.descriptor import Descriptor
    from ..models.enum_descriptor import EnumDescriptor
    from ..models.field_descriptor import FieldDescriptor
    from ..models.file_descriptor_proto import FileDescriptorProto
    from ..models.file_options import FileOptions
    from ..models.service_descriptor import ServiceDescriptor


T = TypeVar("T", bound="FileDescriptor")


@_attrs_define
class FileDescriptor:
    """
    Attributes:
        proto (FileDescriptorProto | Unset):
        options (FileOptions | Unset):
        message_types (list[Descriptor] | Unset):
        enum_types (list[EnumDescriptor] | Unset):
        services (list[ServiceDescriptor] | Unset):
        extensions (list[FieldDescriptor] | Unset):
        dependencies (list[FileDescriptor] | Unset):
        public_dependencies (list[FileDescriptor] | Unset):
        name (str | Unset):
        package (str | Unset):
        file (FileDescriptor | Unset):
        full_name (str | Unset):
    """

    proto: FileDescriptorProto | Unset = UNSET
    options: FileOptions | Unset = UNSET
    message_types: list[Descriptor] | Unset = UNSET
    enum_types: list[EnumDescriptor] | Unset = UNSET
    services: list[ServiceDescriptor] | Unset = UNSET
    extensions: list[FieldDescriptor] | Unset = UNSET
    dependencies: list[FileDescriptor] | Unset = UNSET
    public_dependencies: list[FileDescriptor] | Unset = UNSET
    name: str | Unset = UNSET
    package: str | Unset = UNSET
    file: FileDescriptor | Unset = UNSET
    full_name: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        proto: dict[str, Any] | Unset = UNSET
        if not isinstance(self.proto, Unset):
            proto = self.proto.to_dict()

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        message_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.message_types, Unset):
            message_types = []
            for message_types_item_data in self.message_types:
                message_types_item = message_types_item_data.to_dict()
                message_types.append(message_types_item)

        enum_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.enum_types, Unset):
            enum_types = []
            for enum_types_item_data in self.enum_types:
                enum_types_item = enum_types_item_data.to_dict()
                enum_types.append(enum_types_item)

        services: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.services, Unset):
            services = []
            for services_item_data in self.services:
                services_item = services_item_data.to_dict()
                services.append(services_item)

        extensions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = []
            for extensions_item_data in self.extensions:
                extensions_item = extensions_item_data.to_dict()
                extensions.append(extensions_item)

        dependencies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.dependencies, Unset):
            dependencies = []
            for dependencies_item_data in self.dependencies:
                dependencies_item = dependencies_item_data.to_dict()
                dependencies.append(dependencies_item)

        public_dependencies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.public_dependencies, Unset):
            public_dependencies = []
            for public_dependencies_item_data in self.public_dependencies:
                public_dependencies_item = public_dependencies_item_data.to_dict()
                public_dependencies.append(public_dependencies_item)

        name = self.name

        package = self.package

        file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        full_name = self.full_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if proto is not UNSET:
            field_dict["proto"] = proto
        if options is not UNSET:
            field_dict["options"] = options
        if message_types is not UNSET:
            field_dict["messageTypes"] = message_types
        if enum_types is not UNSET:
            field_dict["enumTypes"] = enum_types
        if services is not UNSET:
            field_dict["services"] = services
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if dependencies is not UNSET:
            field_dict["dependencies"] = dependencies
        if public_dependencies is not UNSET:
            field_dict["publicDependencies"] = public_dependencies
        if name is not UNSET:
            field_dict["name"] = name
        if package is not UNSET:
            field_dict["package"] = package
        if file is not UNSET:
            field_dict["file"] = file
        if full_name is not UNSET:
            field_dict["fullName"] = full_name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.descriptor import Descriptor
        from ..models.enum_descriptor import EnumDescriptor
        from ..models.field_descriptor import FieldDescriptor
        from ..models.file_descriptor_proto import FileDescriptorProto
        from ..models.file_options import FileOptions
        from ..models.service_descriptor import ServiceDescriptor

        d = dict(src_dict)
        _proto = d.pop("proto", UNSET)
        proto: FileDescriptorProto | Unset
        if isinstance(_proto, Unset):
            proto = UNSET
        else:
            proto = FileDescriptorProto.from_dict(_proto)

        _options = d.pop("options", UNSET)
        options: FileOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = FileOptions.from_dict(_options)

        _message_types = d.pop("messageTypes", UNSET)
        message_types: list[Descriptor] | Unset = UNSET
        if _message_types is not UNSET:
            message_types = []
            for message_types_item_data in _message_types:
                message_types_item = Descriptor.from_dict(message_types_item_data)

                message_types.append(message_types_item)

        _enum_types = d.pop("enumTypes", UNSET)
        enum_types: list[EnumDescriptor] | Unset = UNSET
        if _enum_types is not UNSET:
            enum_types = []
            for enum_types_item_data in _enum_types:
                enum_types_item = EnumDescriptor.from_dict(enum_types_item_data)

                enum_types.append(enum_types_item)

        _services = d.pop("services", UNSET)
        services: list[ServiceDescriptor] | Unset = UNSET
        if _services is not UNSET:
            services = []
            for services_item_data in _services:
                services_item = ServiceDescriptor.from_dict(services_item_data)

                services.append(services_item)

        _extensions = d.pop("extensions", UNSET)
        extensions: list[FieldDescriptor] | Unset = UNSET
        if _extensions is not UNSET:
            extensions = []
            for extensions_item_data in _extensions:
                extensions_item = FieldDescriptor.from_dict(extensions_item_data)

                extensions.append(extensions_item)

        _dependencies = d.pop("dependencies", UNSET)
        dependencies: list[FileDescriptor] | Unset = UNSET
        if _dependencies is not UNSET:
            dependencies = []
            for dependencies_item_data in _dependencies:
                dependencies_item = FileDescriptor.from_dict(dependencies_item_data)

                dependencies.append(dependencies_item)

        _public_dependencies = d.pop("publicDependencies", UNSET)
        public_dependencies: list[FileDescriptor] | Unset = UNSET
        if _public_dependencies is not UNSET:
            public_dependencies = []
            for public_dependencies_item_data in _public_dependencies:
                public_dependencies_item = FileDescriptor.from_dict(public_dependencies_item_data)

                public_dependencies.append(public_dependencies_item)

        name = d.pop("name", UNSET)

        package = d.pop("package", UNSET)

        _file = d.pop("file", UNSET)
        file: FileDescriptor | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = FileDescriptor.from_dict(_file)

        full_name = d.pop("fullName", UNSET)

        file_descriptor = cls(
            proto=proto,
            options=options,
            message_types=message_types,
            enum_types=enum_types,
            services=services,
            extensions=extensions,
            dependencies=dependencies,
            public_dependencies=public_dependencies,
            name=name,
            package=package,
            file=file,
            full_name=full_name,
        )

        file_descriptor.additional_properties = d
        return file_descriptor

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
