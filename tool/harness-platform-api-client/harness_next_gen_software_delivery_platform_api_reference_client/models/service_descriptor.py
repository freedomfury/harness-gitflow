from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.file_descriptor import FileDescriptor
    from ..models.method_descriptor import MethodDescriptor
    from ..models.service_descriptor_proto import ServiceDescriptorProto
    from ..models.service_options import ServiceOptions


T = TypeVar("T", bound="ServiceDescriptor")


@_attrs_define
class ServiceDescriptor:
    """
    Attributes:
        index (int | Unset):
        proto (ServiceDescriptorProto | Unset):
        options (ServiceOptions | Unset):
        full_name (str | Unset):
        file (FileDescriptor | Unset):
        methods (list[MethodDescriptor] | Unset):
        name (str | Unset):
    """

    index: int | Unset = UNSET
    proto: ServiceDescriptorProto | Unset = UNSET
    options: ServiceOptions | Unset = UNSET
    full_name: str | Unset = UNSET
    file: FileDescriptor | Unset = UNSET
    methods: list[MethodDescriptor] | Unset = UNSET
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

        methods: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.methods, Unset):
            methods = []
            for methods_item_data in self.methods:
                methods_item = methods_item_data.to_dict()
                methods.append(methods_item)

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
        if methods is not UNSET:
            field_dict["methods"] = methods
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.file_descriptor import FileDescriptor
        from ..models.method_descriptor import MethodDescriptor
        from ..models.service_descriptor_proto import ServiceDescriptorProto
        from ..models.service_options import ServiceOptions

        d = dict(src_dict)
        index = d.pop("index", UNSET)

        _proto = d.pop("proto", UNSET)
        proto: ServiceDescriptorProto | Unset
        if isinstance(_proto, Unset):
            proto = UNSET
        else:
            proto = ServiceDescriptorProto.from_dict(_proto)

        _options = d.pop("options", UNSET)
        options: ServiceOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = ServiceOptions.from_dict(_options)

        full_name = d.pop("fullName", UNSET)

        _file = d.pop("file", UNSET)
        file: FileDescriptor | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = FileDescriptor.from_dict(_file)

        _methods = d.pop("methods", UNSET)
        methods: list[MethodDescriptor] | Unset = UNSET
        if _methods is not UNSET:
            methods = []
            for methods_item_data in _methods:
                methods_item = MethodDescriptor.from_dict(methods_item_data)

                methods.append(methods_item)

        name = d.pop("name", UNSET)

        service_descriptor = cls(
            index=index,
            proto=proto,
            options=options,
            full_name=full_name,
            file=file,
            methods=methods,
            name=name,
        )

        service_descriptor.additional_properties = d
        return service_descriptor

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
