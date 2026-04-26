from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.enum_descriptor import EnumDescriptor
    from ..models.enum_value_descriptor_proto import EnumValueDescriptorProto
    from ..models.enum_value_options import EnumValueOptions
    from ..models.file_descriptor import FileDescriptor


T = TypeVar("T", bound="EnumValueDescriptor")


@_attrs_define
class EnumValueDescriptor:
    """
    Attributes:
        index (int | Unset):
        proto (EnumValueDescriptorProto | Unset):
        options (EnumValueOptions | Unset):
        full_name (str | Unset):
        type_ (EnumDescriptor | Unset):
        name (str | Unset):
        file (FileDescriptor | Unset):
        number (int | Unset):
    """

    index: int | Unset = UNSET
    proto: EnumValueDescriptorProto | Unset = UNSET
    options: EnumValueOptions | Unset = UNSET
    full_name: str | Unset = UNSET
    type_: EnumDescriptor | Unset = UNSET
    name: str | Unset = UNSET
    file: FileDescriptor | Unset = UNSET
    number: int | Unset = UNSET
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

        type_: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.to_dict()

        name = self.name

        file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()

        number = self.number

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
        if type_ is not UNSET:
            field_dict["type"] = type_
        if name is not UNSET:
            field_dict["name"] = name
        if file is not UNSET:
            field_dict["file"] = file
        if number is not UNSET:
            field_dict["number"] = number

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.enum_descriptor import EnumDescriptor
        from ..models.enum_value_descriptor_proto import EnumValueDescriptorProto
        from ..models.enum_value_options import EnumValueOptions
        from ..models.file_descriptor import FileDescriptor

        d = dict(src_dict)
        index = d.pop("index", UNSET)

        _proto = d.pop("proto", UNSET)
        proto: EnumValueDescriptorProto | Unset
        if isinstance(_proto, Unset):
            proto = UNSET
        else:
            proto = EnumValueDescriptorProto.from_dict(_proto)

        _options = d.pop("options", UNSET)
        options: EnumValueOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = EnumValueOptions.from_dict(_options)

        full_name = d.pop("fullName", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: EnumDescriptor | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EnumDescriptor.from_dict(_type_)

        name = d.pop("name", UNSET)

        _file = d.pop("file", UNSET)
        file: FileDescriptor | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = FileDescriptor.from_dict(_file)

        number = d.pop("number", UNSET)

        enum_value_descriptor = cls(
            index=index,
            proto=proto,
            options=options,
            full_name=full_name,
            type_=type_,
            name=name,
            file=file,
            number=number,
        )

        enum_value_descriptor.additional_properties = d
        return enum_value_descriptor

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
