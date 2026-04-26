from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.field_descriptor_java_type import FieldDescriptorJavaType, check_field_descriptor_java_type
from ..models.field_descriptor_lite_java_type import FieldDescriptorLiteJavaType, check_field_descriptor_lite_java_type
from ..models.field_descriptor_lite_type import FieldDescriptorLiteType, check_field_descriptor_lite_type
from ..models.field_descriptor_type import FieldDescriptorType, check_field_descriptor_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.descriptor import Descriptor
    from ..models.enum_descriptor import EnumDescriptor
    from ..models.field_descriptor_default_value import FieldDescriptorDefaultValue
    from ..models.field_descriptor_proto import FieldDescriptorProto
    from ..models.field_options import FieldOptions
    from ..models.file_descriptor import FileDescriptor
    from ..models.oneof_descriptor import OneofDescriptor


T = TypeVar("T", bound="FieldDescriptor")


@_attrs_define
class FieldDescriptor:
    """
    Attributes:
        index (int | Unset):
        proto (FieldDescriptorProto | Unset):
        options (FieldOptions | Unset):
        full_name (str | Unset):
        json_name (str | Unset):
        file (FileDescriptor | Unset):
        extension_scope (Descriptor | Unset):
        type_ (FieldDescriptorType | Unset):
        containing_type (Descriptor | Unset):
        message_type (Descriptor | Unset):
        containing_oneof (OneofDescriptor | Unset):
        enum_type (EnumDescriptor | Unset):
        default_value (FieldDescriptorDefaultValue | Unset):
        name (str | Unset):
        number (int | Unset):
        java_type (FieldDescriptorJavaType | Unset):
        required (bool | Unset):
        optional (bool | Unset):
        packable (bool | Unset):
        real_containing_oneof (OneofDescriptor | Unset):
        packed (bool | Unset):
        lite_type (FieldDescriptorLiteType | Unset):
        extension (bool | Unset):
        repeated (bool | Unset):
        map_field (bool | Unset):
        lite_java_type (FieldDescriptorLiteJavaType | Unset):
    """

    index: int | Unset = UNSET
    proto: FieldDescriptorProto | Unset = UNSET
    options: FieldOptions | Unset = UNSET
    full_name: str | Unset = UNSET
    json_name: str | Unset = UNSET
    file: FileDescriptor | Unset = UNSET
    extension_scope: Descriptor | Unset = UNSET
    type_: FieldDescriptorType | Unset = UNSET
    containing_type: Descriptor | Unset = UNSET
    message_type: Descriptor | Unset = UNSET
    containing_oneof: OneofDescriptor | Unset = UNSET
    enum_type: EnumDescriptor | Unset = UNSET
    default_value: FieldDescriptorDefaultValue | Unset = UNSET
    name: str | Unset = UNSET
    number: int | Unset = UNSET
    java_type: FieldDescriptorJavaType | Unset = UNSET
    required: bool | Unset = UNSET
    optional: bool | Unset = UNSET
    packable: bool | Unset = UNSET
    real_containing_oneof: OneofDescriptor | Unset = UNSET
    packed: bool | Unset = UNSET
    lite_type: FieldDescriptorLiteType | Unset = UNSET
    extension: bool | Unset = UNSET
    repeated: bool | Unset = UNSET
    map_field: bool | Unset = UNSET
    lite_java_type: FieldDescriptorLiteJavaType | Unset = UNSET
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

        json_name = self.json_name

        file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        extension_scope: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extension_scope, Unset):
            extension_scope = self.extension_scope.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        containing_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.containing_type, Unset):
            containing_type = self.containing_type.to_dict()

        message_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.message_type, Unset):
            message_type = self.message_type.to_dict()

        containing_oneof: dict[str, Any] | Unset = UNSET
        if not isinstance(self.containing_oneof, Unset):
            containing_oneof = self.containing_oneof.to_dict()

        enum_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.enum_type, Unset):
            enum_type = self.enum_type.to_dict()

        default_value: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_value, Unset):
            default_value = self.default_value.to_dict()

        name = self.name

        number = self.number

        java_type: str | Unset = UNSET
        if not isinstance(self.java_type, Unset):
            java_type = self.java_type

        required = self.required

        optional = self.optional

        packable = self.packable

        real_containing_oneof: dict[str, Any] | Unset = UNSET
        if not isinstance(self.real_containing_oneof, Unset):
            real_containing_oneof = self.real_containing_oneof.to_dict()

        packed = self.packed

        lite_type: str | Unset = UNSET
        if not isinstance(self.lite_type, Unset):
            lite_type = self.lite_type

        extension = self.extension

        repeated = self.repeated

        map_field = self.map_field

        lite_java_type: str | Unset = UNSET
        if not isinstance(self.lite_java_type, Unset):
            lite_java_type = self.lite_java_type

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
        if json_name is not UNSET:
            field_dict["jsonName"] = json_name
        if file is not UNSET:
            field_dict["file"] = file
        if extension_scope is not UNSET:
            field_dict["extensionScope"] = extension_scope
        if type_ is not UNSET:
            field_dict["type"] = type_
        if containing_type is not UNSET:
            field_dict["containingType"] = containing_type
        if message_type is not UNSET:
            field_dict["messageType"] = message_type
        if containing_oneof is not UNSET:
            field_dict["containingOneof"] = containing_oneof
        if enum_type is not UNSET:
            field_dict["enumType"] = enum_type
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if name is not UNSET:
            field_dict["name"] = name
        if number is not UNSET:
            field_dict["number"] = number
        if java_type is not UNSET:
            field_dict["javaType"] = java_type
        if required is not UNSET:
            field_dict["required"] = required
        if optional is not UNSET:
            field_dict["optional"] = optional
        if packable is not UNSET:
            field_dict["packable"] = packable
        if real_containing_oneof is not UNSET:
            field_dict["realContainingOneof"] = real_containing_oneof
        if packed is not UNSET:
            field_dict["packed"] = packed
        if lite_type is not UNSET:
            field_dict["liteType"] = lite_type
        if extension is not UNSET:
            field_dict["extension"] = extension
        if repeated is not UNSET:
            field_dict["repeated"] = repeated
        if map_field is not UNSET:
            field_dict["mapField"] = map_field
        if lite_java_type is not UNSET:
            field_dict["liteJavaType"] = lite_java_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.descriptor import Descriptor
        from ..models.enum_descriptor import EnumDescriptor
        from ..models.field_descriptor_default_value import FieldDescriptorDefaultValue
        from ..models.field_descriptor_proto import FieldDescriptorProto
        from ..models.field_options import FieldOptions
        from ..models.file_descriptor import FileDescriptor
        from ..models.oneof_descriptor import OneofDescriptor

        d = dict(src_dict)
        index = d.pop("index", UNSET)

        _proto = d.pop("proto", UNSET)
        proto: FieldDescriptorProto | Unset
        if isinstance(_proto, Unset):
            proto = UNSET
        else:
            proto = FieldDescriptorProto.from_dict(_proto)

        _options = d.pop("options", UNSET)
        options: FieldOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = FieldOptions.from_dict(_options)

        full_name = d.pop("fullName", UNSET)

        json_name = d.pop("jsonName", UNSET)

        _file = d.pop("file", UNSET)
        file: FileDescriptor | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = FileDescriptor.from_dict(_file)

        _extension_scope = d.pop("extensionScope", UNSET)
        extension_scope: Descriptor | Unset
        if isinstance(_extension_scope, Unset):
            extension_scope = UNSET
        else:
            extension_scope = Descriptor.from_dict(_extension_scope)

        _type_ = d.pop("type", UNSET)
        type_: FieldDescriptorType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_field_descriptor_type(_type_)

        _containing_type = d.pop("containingType", UNSET)
        containing_type: Descriptor | Unset
        if isinstance(_containing_type, Unset):
            containing_type = UNSET
        else:
            containing_type = Descriptor.from_dict(_containing_type)

        _message_type = d.pop("messageType", UNSET)
        message_type: Descriptor | Unset
        if isinstance(_message_type, Unset):
            message_type = UNSET
        else:
            message_type = Descriptor.from_dict(_message_type)

        _containing_oneof = d.pop("containingOneof", UNSET)
        containing_oneof: OneofDescriptor | Unset
        if isinstance(_containing_oneof, Unset):
            containing_oneof = UNSET
        else:
            containing_oneof = OneofDescriptor.from_dict(_containing_oneof)

        _enum_type = d.pop("enumType", UNSET)
        enum_type: EnumDescriptor | Unset
        if isinstance(_enum_type, Unset):
            enum_type = UNSET
        else:
            enum_type = EnumDescriptor.from_dict(_enum_type)

        _default_value = d.pop("defaultValue", UNSET)
        default_value: FieldDescriptorDefaultValue | Unset
        if isinstance(_default_value, Unset):
            default_value = UNSET
        else:
            default_value = FieldDescriptorDefaultValue.from_dict(_default_value)

        name = d.pop("name", UNSET)

        number = d.pop("number", UNSET)

        _java_type = d.pop("javaType", UNSET)
        java_type: FieldDescriptorJavaType | Unset
        if isinstance(_java_type, Unset):
            java_type = UNSET
        else:
            java_type = check_field_descriptor_java_type(_java_type)

        required = d.pop("required", UNSET)

        optional = d.pop("optional", UNSET)

        packable = d.pop("packable", UNSET)

        _real_containing_oneof = d.pop("realContainingOneof", UNSET)
        real_containing_oneof: OneofDescriptor | Unset
        if isinstance(_real_containing_oneof, Unset):
            real_containing_oneof = UNSET
        else:
            real_containing_oneof = OneofDescriptor.from_dict(_real_containing_oneof)

        packed = d.pop("packed", UNSET)

        _lite_type = d.pop("liteType", UNSET)
        lite_type: FieldDescriptorLiteType | Unset
        if isinstance(_lite_type, Unset):
            lite_type = UNSET
        else:
            lite_type = check_field_descriptor_lite_type(_lite_type)

        extension = d.pop("extension", UNSET)

        repeated = d.pop("repeated", UNSET)

        map_field = d.pop("mapField", UNSET)

        _lite_java_type = d.pop("liteJavaType", UNSET)
        lite_java_type: FieldDescriptorLiteJavaType | Unset
        if isinstance(_lite_java_type, Unset):
            lite_java_type = UNSET
        else:
            lite_java_type = check_field_descriptor_lite_java_type(_lite_java_type)

        field_descriptor = cls(
            index=index,
            proto=proto,
            options=options,
            full_name=full_name,
            json_name=json_name,
            file=file,
            extension_scope=extension_scope,
            type_=type_,
            containing_type=containing_type,
            message_type=message_type,
            containing_oneof=containing_oneof,
            enum_type=enum_type,
            default_value=default_value,
            name=name,
            number=number,
            java_type=java_type,
            required=required,
            optional=optional,
            packable=packable,
            real_containing_oneof=real_containing_oneof,
            packed=packed,
            lite_type=lite_type,
            extension=extension,
            repeated=repeated,
            map_field=map_field,
            lite_java_type=lite_java_type,
        )

        field_descriptor.additional_properties = d
        return field_descriptor

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
