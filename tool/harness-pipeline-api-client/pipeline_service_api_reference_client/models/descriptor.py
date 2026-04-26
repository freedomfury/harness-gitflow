from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.descriptor_proto import DescriptorProto
    from ..models.enum_descriptor import EnumDescriptor
    from ..models.field_descriptor import FieldDescriptor
    from ..models.file_descriptor import FileDescriptor
    from ..models.message_options import MessageOptions
    from ..models.oneof_descriptor import OneofDescriptor


T = TypeVar("T", bound="Descriptor")


@_attrs_define
class Descriptor:
    """
    Attributes:
        index (int | Unset):
        proto (DescriptorProto | Unset):
        options (MessageOptions | Unset):
        full_name (str | Unset):
        file (FileDescriptor | Unset):
        containing_type (Descriptor | Unset):
        nested_types (list[Descriptor] | Unset):
        enum_types (list[EnumDescriptor] | Unset):
        fields (list[FieldDescriptor] | Unset):
        extensions (list[FieldDescriptor] | Unset):
        oneofs (list[OneofDescriptor] | Unset):
        name (str | Unset):
        extendable (bool | Unset):
        real_oneofs (list[OneofDescriptor] | Unset):
    """

    index: int | Unset = UNSET
    proto: DescriptorProto | Unset = UNSET
    options: MessageOptions | Unset = UNSET
    full_name: str | Unset = UNSET
    file: FileDescriptor | Unset = UNSET
    containing_type: Descriptor | Unset = UNSET
    nested_types: list[Descriptor] | Unset = UNSET
    enum_types: list[EnumDescriptor] | Unset = UNSET
    fields: list[FieldDescriptor] | Unset = UNSET
    extensions: list[FieldDescriptor] | Unset = UNSET
    oneofs: list[OneofDescriptor] | Unset = UNSET
    name: str | Unset = UNSET
    extendable: bool | Unset = UNSET
    real_oneofs: list[OneofDescriptor] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index = self.index

        proto: dict[str, Any] | Unset = UNSET
        if not isinstance(self.proto, Unset):
            proto = self.proto.to_dict()

        options: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options, Unset):
            options = self.options.to_dict()

        full_name = self.full_name

        file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        containing_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.containing_type, Unset):
            containing_type = self.containing_type.to_dict()

        nested_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nested_types, Unset):
            nested_types = []
            for nested_types_item_data in self.nested_types:
                nested_types_item = nested_types_item_data.to_dict()
                nested_types.append(nested_types_item)

        enum_types: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.enum_types, Unset):
            enum_types = []
            for enum_types_item_data in self.enum_types:
                enum_types_item = enum_types_item_data.to_dict()
                enum_types.append(enum_types_item)

        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        extensions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.extensions, Unset):
            extensions = []
            for extensions_item_data in self.extensions:
                extensions_item = extensions_item_data.to_dict()
                extensions.append(extensions_item)

        oneofs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.oneofs, Unset):
            oneofs = []
            for oneofs_item_data in self.oneofs:
                oneofs_item = oneofs_item_data.to_dict()
                oneofs.append(oneofs_item)

        name = self.name

        extendable = self.extendable

        real_oneofs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.real_oneofs, Unset):
            real_oneofs = []
            for real_oneofs_item_data in self.real_oneofs:
                real_oneofs_item = real_oneofs_item_data.to_dict()
                real_oneofs.append(real_oneofs_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if index is not UNSET:
            field_dict["index"] = index
        if proto is not UNSET:
            field_dict["proto"] = proto
        if options is not UNSET:
            field_dict["options"] = options
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if file is not UNSET:
            field_dict["file"] = file
        if containing_type is not UNSET:
            field_dict["containingType"] = containing_type
        if nested_types is not UNSET:
            field_dict["nestedTypes"] = nested_types
        if enum_types is not UNSET:
            field_dict["enumTypes"] = enum_types
        if fields is not UNSET:
            field_dict["fields"] = fields
        if extensions is not UNSET:
            field_dict["extensions"] = extensions
        if oneofs is not UNSET:
            field_dict["oneofs"] = oneofs
        if name is not UNSET:
            field_dict["name"] = name
        if extendable is not UNSET:
            field_dict["extendable"] = extendable
        if real_oneofs is not UNSET:
            field_dict["realOneofs"] = real_oneofs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.descriptor_proto import DescriptorProto
        from ..models.enum_descriptor import EnumDescriptor
        from ..models.field_descriptor import FieldDescriptor
        from ..models.file_descriptor import FileDescriptor
        from ..models.message_options import MessageOptions
        from ..models.oneof_descriptor import OneofDescriptor

        d = dict(src_dict)
        index = d.pop("index", UNSET)

        _proto = d.pop("proto", UNSET)
        proto: DescriptorProto | Unset
        if isinstance(_proto, Unset):
            proto = UNSET
        else:
            proto = DescriptorProto.from_dict(_proto)

        _options = d.pop("options", UNSET)
        options: MessageOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = MessageOptions.from_dict(_options)

        full_name = d.pop("fullName", UNSET)

        _file = d.pop("file", UNSET)
        file: FileDescriptor | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = FileDescriptor.from_dict(_file)

        _containing_type = d.pop("containingType", UNSET)
        containing_type: Descriptor | Unset
        if isinstance(_containing_type, Unset):
            containing_type = UNSET
        else:
            containing_type = Descriptor.from_dict(_containing_type)

        _nested_types = d.pop("nestedTypes", UNSET)
        nested_types: list[Descriptor] | Unset = UNSET
        if _nested_types is not UNSET:
            nested_types = []
            for nested_types_item_data in _nested_types:
                nested_types_item = Descriptor.from_dict(nested_types_item_data)

                nested_types.append(nested_types_item)

        _enum_types = d.pop("enumTypes", UNSET)
        enum_types: list[EnumDescriptor] | Unset = UNSET
        if _enum_types is not UNSET:
            enum_types = []
            for enum_types_item_data in _enum_types:
                enum_types_item = EnumDescriptor.from_dict(enum_types_item_data)

                enum_types.append(enum_types_item)

        _fields = d.pop("fields", UNSET)
        fields: list[FieldDescriptor] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = FieldDescriptor.from_dict(fields_item_data)

                fields.append(fields_item)

        _extensions = d.pop("extensions", UNSET)
        extensions: list[FieldDescriptor] | Unset = UNSET
        if _extensions is not UNSET:
            extensions = []
            for extensions_item_data in _extensions:
                extensions_item = FieldDescriptor.from_dict(extensions_item_data)

                extensions.append(extensions_item)

        _oneofs = d.pop("oneofs", UNSET)
        oneofs: list[OneofDescriptor] | Unset = UNSET
        if _oneofs is not UNSET:
            oneofs = []
            for oneofs_item_data in _oneofs:
                oneofs_item = OneofDescriptor.from_dict(oneofs_item_data)

                oneofs.append(oneofs_item)

        name = d.pop("name", UNSET)

        extendable = d.pop("extendable", UNSET)

        _real_oneofs = d.pop("realOneofs", UNSET)
        real_oneofs: list[OneofDescriptor] | Unset = UNSET
        if _real_oneofs is not UNSET:
            real_oneofs = []
            for real_oneofs_item_data in _real_oneofs:
                real_oneofs_item = OneofDescriptor.from_dict(real_oneofs_item_data)

                real_oneofs.append(real_oneofs_item)

        descriptor = cls(
            index=index,
            proto=proto,
            options=options,
            full_name=full_name,
            file=file,
            containing_type=containing_type,
            nested_types=nested_types,
            enum_types=enum_types,
            fields=fields,
            extensions=extensions,
            oneofs=oneofs,
            name=name,
            extendable=extendable,
            real_oneofs=real_oneofs,
        )

        descriptor.additional_properties = d
        return descriptor

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
