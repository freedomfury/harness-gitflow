from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.declaration_or_builder_all_fields import DeclarationOrBuilderAllFields
    from ..models.descriptor import Descriptor
    from ..models.message import Message
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="DeclarationOrBuilder")


@_attrs_define
class DeclarationOrBuilder:
    """
    Attributes:
        full_name_bytes (ByteString | Unset):
        reserved (bool | Unset):
        type_bytes (ByteString | Unset):
        type_ (str | Unset):
        number (int | Unset):
        full_name (str | Unset):
        repeated (bool | Unset):
        initialization_error_string (str | Unset):
        all_fields (DeclarationOrBuilderAllFields | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        descriptor_for_type (Descriptor | Unset):
        default_instance_for_type (Message | Unset):
        initialized (bool | Unset):
    """

    full_name_bytes: ByteString | Unset = UNSET
    reserved: bool | Unset = UNSET
    type_bytes: ByteString | Unset = UNSET
    type_: str | Unset = UNSET
    number: int | Unset = UNSET
    full_name: str | Unset = UNSET
    repeated: bool | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    all_fields: DeclarationOrBuilderAllFields | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        full_name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.full_name_bytes, Unset):
            full_name_bytes = self.full_name_bytes.to_dict()

        reserved = self.reserved

        type_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_bytes, Unset):
            type_bytes = self.type_bytes.to_dict()

        type_ = self.type_

        number = self.number

        full_name = self.full_name

        repeated = self.repeated

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
        if full_name_bytes is not UNSET:
            field_dict["fullNameBytes"] = full_name_bytes
        if reserved is not UNSET:
            field_dict["reserved"] = reserved
        if type_bytes is not UNSET:
            field_dict["typeBytes"] = type_bytes
        if type_ is not UNSET:
            field_dict["type"] = type_
        if number is not UNSET:
            field_dict["number"] = number
        if full_name is not UNSET:
            field_dict["fullName"] = full_name
        if repeated is not UNSET:
            field_dict["repeated"] = repeated
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
        from ..models.declaration_or_builder_all_fields import DeclarationOrBuilderAllFields
        from ..models.descriptor import Descriptor
        from ..models.message import Message
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _full_name_bytes = d.pop("fullNameBytes", UNSET)
        full_name_bytes: ByteString | Unset
        if isinstance(_full_name_bytes, Unset):
            full_name_bytes = UNSET
        else:
            full_name_bytes = ByteString.from_dict(_full_name_bytes)

        reserved = d.pop("reserved", UNSET)

        _type_bytes = d.pop("typeBytes", UNSET)
        type_bytes: ByteString | Unset
        if isinstance(_type_bytes, Unset):
            type_bytes = UNSET
        else:
            type_bytes = ByteString.from_dict(_type_bytes)

        type_ = d.pop("type", UNSET)

        number = d.pop("number", UNSET)

        full_name = d.pop("fullName", UNSET)

        repeated = d.pop("repeated", UNSET)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: DeclarationOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = DeclarationOrBuilderAllFields.from_dict(_all_fields)

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

        declaration_or_builder = cls(
            full_name_bytes=full_name_bytes,
            reserved=reserved,
            type_bytes=type_bytes,
            type_=type_,
            number=number,
            full_name=full_name,
            repeated=repeated,
            initialization_error_string=initialization_error_string,
            all_fields=all_fields,
            unknown_fields=unknown_fields,
            descriptor_for_type=descriptor_for_type,
            default_instance_for_type=default_instance_for_type,
            initialized=initialized,
        )

        declaration_or_builder.additional_properties = d
        return declaration_or_builder

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
