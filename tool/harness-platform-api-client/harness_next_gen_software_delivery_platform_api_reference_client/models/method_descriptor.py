from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.descriptor import Descriptor
    from ..models.file_descriptor import FileDescriptor
    from ..models.method_descriptor_proto import MethodDescriptorProto
    from ..models.method_options import MethodOptions
    from ..models.service_descriptor import ServiceDescriptor


T = TypeVar("T", bound="MethodDescriptor")


@_attrs_define
class MethodDescriptor:
    """
    Attributes:
        index (int | Unset):
        proto (MethodDescriptorProto | Unset):
        options (MethodOptions | Unset):
        full_name (str | Unset):
        file (FileDescriptor | Unset):
        service (ServiceDescriptor | Unset):
        input_type (Descriptor | Unset):
        output_type (Descriptor | Unset):
        server_streaming (bool | Unset):
        client_streaming (bool | Unset):
        name (str | Unset):
    """

    index: int | Unset = UNSET
    proto: MethodDescriptorProto | Unset = UNSET
    options: MethodOptions | Unset = UNSET
    full_name: str | Unset = UNSET
    file: FileDescriptor | Unset = UNSET
    service: ServiceDescriptor | Unset = UNSET
    input_type: Descriptor | Unset = UNSET
    output_type: Descriptor | Unset = UNSET
    server_streaming: bool | Unset = UNSET
    client_streaming: bool | Unset = UNSET
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

        service: dict[str, Any] | Unset = UNSET
        if not isinstance(self.service, Unset):
            service = self.service.to_dict()

        input_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.input_type, Unset):
            input_type = self.input_type.to_dict()

        output_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.output_type, Unset):
            output_type = self.output_type.to_dict()

        server_streaming = self.server_streaming

        client_streaming = self.client_streaming

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
        if service is not UNSET:
            field_dict["service"] = service
        if input_type is not UNSET:
            field_dict["inputType"] = input_type
        if output_type is not UNSET:
            field_dict["outputType"] = output_type
        if server_streaming is not UNSET:
            field_dict["serverStreaming"] = server_streaming
        if client_streaming is not UNSET:
            field_dict["clientStreaming"] = client_streaming
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.descriptor import Descriptor
        from ..models.file_descriptor import FileDescriptor
        from ..models.method_descriptor_proto import MethodDescriptorProto
        from ..models.method_options import MethodOptions
        from ..models.service_descriptor import ServiceDescriptor

        d = dict(src_dict)
        index = d.pop("index", UNSET)

        _proto = d.pop("proto", UNSET)
        proto: MethodDescriptorProto | Unset
        if isinstance(_proto, Unset):
            proto = UNSET
        else:
            proto = MethodDescriptorProto.from_dict(_proto)

        _options = d.pop("options", UNSET)
        options: MethodOptions | Unset
        if isinstance(_options, Unset):
            options = UNSET
        else:
            options = MethodOptions.from_dict(_options)

        full_name = d.pop("fullName", UNSET)

        _file = d.pop("file", UNSET)
        file: FileDescriptor | Unset
        if isinstance(_file, Unset):
            file = UNSET
        else:
            file = FileDescriptor.from_dict(_file)

        _service = d.pop("service", UNSET)
        service: ServiceDescriptor | Unset
        if isinstance(_service, Unset):
            service = UNSET
        else:
            service = ServiceDescriptor.from_dict(_service)

        _input_type = d.pop("inputType", UNSET)
        input_type: Descriptor | Unset
        if isinstance(_input_type, Unset):
            input_type = UNSET
        else:
            input_type = Descriptor.from_dict(_input_type)

        _output_type = d.pop("outputType", UNSET)
        output_type: Descriptor | Unset
        if isinstance(_output_type, Unset):
            output_type = UNSET
        else:
            output_type = Descriptor.from_dict(_output_type)

        server_streaming = d.pop("serverStreaming", UNSET)

        client_streaming = d.pop("clientStreaming", UNSET)

        name = d.pop("name", UNSET)

        method_descriptor = cls(
            index=index,
            proto=proto,
            options=options,
            full_name=full_name,
            file=file,
            service=service,
            input_type=input_type,
            output_type=output_type,
            server_streaming=server_streaming,
            client_streaming=client_streaming,
            name=name,
        )

        method_descriptor.additional_properties = d
        return method_descriptor

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
