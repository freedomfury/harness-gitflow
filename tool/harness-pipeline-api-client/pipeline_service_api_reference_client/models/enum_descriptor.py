from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.descriptor import Descriptor
    from ..models.enum_descriptor_proto import EnumDescriptorProto
    from ..models.enum_options import EnumOptions
    from ..models.enum_value_descriptor import EnumValueDescriptor
    from ..models.file_descriptor import FileDescriptor


T = TypeVar("T", bound="EnumDescriptor")


@_attrs_define
class EnumDescriptor:
    """
    Attributes:
        index (int | Unset):
        proto (EnumDescriptorProto | Unset):
        options (EnumOptions | Unset):
        full_name (str | Unset):
        file (FileDescriptor | Unset):
        containing_type (Descriptor | Unset):
        values (list[EnumValueDescriptor] | Unset):
        name (str | Unset):
        closed (bool | Unset):
    """

    index: int | Unset = UNSET
    proto: EnumDescriptorProto | Unset = UNSET
    options: EnumOptions | Unset = UNSET
    full_name: str | Unset = UNSET
    file: FileDescriptor | Unset = UNSET
    containing_type: Descriptor | Unset = UNSET
    values: list[EnumValueDescriptor] | Unset = UNSET
    name: str | Unset = UNSET
    closed: bool | Unset = UNSET
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

        values: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.values, Unset):
            values = []
            for values_item_data in self.values:
                values_item = values_item_data.to_dict()
                values.append(values_item)

        name = self.name

        closed = self.closed

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
        if values is not UNSET:
            field_dict["values"] = values
        if name is not UNSET:
            field_dict["name"] = name
        if closed is not UNSET:
            field_dict["closed"] = closed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.descriptor import Descriptor
        from ..models.enum_descriptor_proto import EnumDescriptorProto
        from ..models.enum_options import EnumOptions
        from ..models.enum_value_descriptor import EnumValueDescriptor
        from ..models.file_descriptor import FileDescriptor

        d = dict(src_dict)
        index = d.pop("index", UNSET)

        _proto = d.pop("proto", UNSET)
        proto: EnumDescriptorProto | Unset
        if isinstance(_proto, Unset):
            proto = UNSET
        else:
            proto = EnumDescriptorProto.from_dict(_proto)

        _options = d.pop("options", UNSET)
        options: EnumOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = EnumOptions.from_dict(_options)

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

        _values = d.pop("values", UNSET)
        values: list[EnumValueDescriptor] | Unset = UNSET
        if _values is not UNSET:
            values = []
            for values_item_data in _values:
                values_item = EnumValueDescriptor.from_dict(values_item_data)

                values.append(values_item)

        name = d.pop("name", UNSET)

        closed = d.pop("closed", UNSET)

        enum_descriptor = cls(
            index=index,
            proto=proto,
            options=options,
            full_name=full_name,
            file=file,
            containing_type=containing_type,
            values=values,
            name=name,
            closed=closed,
        )

        enum_descriptor.additional_properties = d
        return enum_descriptor

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
