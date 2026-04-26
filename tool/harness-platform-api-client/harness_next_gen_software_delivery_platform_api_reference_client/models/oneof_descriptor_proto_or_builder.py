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
    from ..models.oneof_descriptor_proto_or_builder_all_fields import OneofDescriptorProtoOrBuilderAllFields
    from ..models.oneof_options import OneofOptions
    from ..models.oneof_options_or_builder import OneofOptionsOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="OneofDescriptorProtoOrBuilder")


@_attrs_define
class OneofDescriptorProtoOrBuilder:
    """
    Attributes:
        options_or_builder (OneofOptionsOrBuilder | Unset):
        name (str | Unset):
        name_bytes (ByteString | Unset):
        options (OneofOptions | Unset):
        initialization_error_string (str | Unset):
        all_fields (OneofDescriptorProtoOrBuilderAllFields | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        descriptor_for_type (Descriptor | Unset):
        default_instance_for_type (Message | Unset):
        initialized (bool | Unset):
    """

    options_or_builder: OneofOptionsOrBuilder | Unset = UNSET
    name: str | Unset = UNSET
    name_bytes: ByteString | Unset = UNSET
    options: OneofOptions | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    all_fields: OneofDescriptorProtoOrBuilderAllFields | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        options_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.options_or_builder, Unset):
            options_or_builder = self.options_or_builder.to_dict()

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
        if options_or_builder is not UNSET:
            field_dict["optionsOrBuilder"] = options_or_builder
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
        from ..models.message import Message
        from ..models.oneof_descriptor_proto_or_builder_all_fields import OneofDescriptorProtoOrBuilderAllFields
        from ..models.oneof_options import OneofOptions
        from ..models.oneof_options_or_builder import OneofOptionsOrBuilder
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _options_or_builder = d.pop("optionsOrBuilder", UNSET)
        options_or_builder: OneofOptionsOrBuilder | Unset
        if isinstance(_options_or_builder, Unset):
            options_or_builder = UNSET
        else:
            options_or_builder = OneofOptionsOrBuilder.from_dict(_options_or_builder)

        name = d.pop("name", UNSET)

        _name_bytes = d.pop("nameBytes", UNSET)
        name_bytes: ByteString | Unset
        if isinstance(_name_bytes, Unset):
            name_bytes = UNSET
        else:
            name_bytes = ByteString.from_dict(_name_bytes)

        _options = d.pop("options", UNSET)
        options: OneofOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = OneofOptions.from_dict(_options)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: OneofDescriptorProtoOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = OneofDescriptorProtoOrBuilderAllFields.from_dict(_all_fields)

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

        oneof_descriptor_proto_or_builder = cls(
            options_or_builder=options_or_builder,
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

        oneof_descriptor_proto_or_builder.additional_properties = d
        return oneof_descriptor_proto_or_builder

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
