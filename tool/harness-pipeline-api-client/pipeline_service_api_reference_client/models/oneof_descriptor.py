from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.descriptor import Descriptor
    from ..models.field_descriptor import FieldDescriptor
    from ..models.file_descriptor import FileDescriptor
    from ..models.oneof_descriptor_proto import OneofDescriptorProto
    from ..models.oneof_options import OneofOptions


T = TypeVar("T", bound="OneofDescriptor")


@_attrs_define
class OneofDescriptor:
    """
    Attributes:
        index (int | Unset):
        proto (OneofDescriptorProto | Unset):
        options (OneofOptions | Unset):
        full_name (str | Unset):
        file (FileDescriptor | Unset):
        containing_type (Descriptor | Unset):
        field_count (int | Unset):
        fields (list[FieldDescriptor] | Unset):
        name (str | Unset):
    """

    index: int | Unset = UNSET
    proto: OneofDescriptorProto | Unset = UNSET
    options: OneofOptions | Unset = UNSET
    full_name: str | Unset = UNSET
    file: FileDescriptor | Unset = UNSET
    containing_type: Descriptor | Unset = UNSET
    field_count: int | Unset = UNSET
    fields: list[FieldDescriptor] | Unset = UNSET
    name: str | Unset = UNSET
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

        field_count = self.field_count

        fields: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()
                fields.append(fields_item)

        name = self.name

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
        if field_count is not UNSET:
            field_dict["fieldCount"] = field_count
        if fields is not UNSET:
            field_dict["fields"] = fields
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.descriptor import Descriptor
        from ..models.field_descriptor import FieldDescriptor
        from ..models.file_descriptor import FileDescriptor
        from ..models.oneof_descriptor_proto import OneofDescriptorProto
        from ..models.oneof_options import OneofOptions

        d = dict(src_dict)
        index = d.pop("index", UNSET)

        _proto = d.pop("proto", UNSET)
        proto: OneofDescriptorProto | Unset
        if isinstance(_proto, Unset):
            proto = UNSET
        else:
            proto = OneofDescriptorProto.from_dict(_proto)

        _options = d.pop("options", UNSET)
        options: OneofOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = OneofOptions.from_dict(_options)

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

        field_count = d.pop("fieldCount", UNSET)

        _fields = d.pop("fields", UNSET)
        fields: list[FieldDescriptor] | Unset = UNSET
        if _fields is not UNSET:
            fields = []
            for fields_item_data in _fields:
                fields_item = FieldDescriptor.from_dict(fields_item_data)

                fields.append(fields_item)

        name = d.pop("name", UNSET)

        oneof_descriptor = cls(
            index=index,
            proto=proto,
            options=options,
            full_name=full_name,
            file=file,
            containing_type=containing_type,
            field_count=field_count,
            fields=fields,
            name=name,
        )

        oneof_descriptor.additional_properties = d
        return oneof_descriptor

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
