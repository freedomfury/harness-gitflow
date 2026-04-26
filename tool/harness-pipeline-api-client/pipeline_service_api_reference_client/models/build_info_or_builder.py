from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.build_info_or_builder_all_fields import BuildInfoOrBuilderAllFields
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.message import Message
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="BuildInfoOrBuilder")


@_attrs_define
class BuildInfoOrBuilder:
    """
    Attributes:
        image_path_bytes (ByteString | Unset):
        build_bytes (ByteString | Unset):
        image_path (str | Unset):
        build (str | Unset):
        all_fields (BuildInfoOrBuilderAllFields | Unset):
        default_instance_for_type (Message | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        initialized (bool | Unset):
    """

    image_path_bytes: ByteString | Unset = UNSET
    build_bytes: ByteString | Unset = UNSET
    image_path: str | Unset = UNSET
    build: str | Unset = UNSET
    all_fields: BuildInfoOrBuilderAllFields | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        image_path_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image_path_bytes, Unset):
            image_path_bytes = self.image_path_bytes.to_dict()

        build_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.build_bytes, Unset):
            build_bytes = self.build_bytes.to_dict()

        image_path = self.image_path

        build = self.build

        all_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields, Unset):
            all_fields = self.all_fields.to_dict()

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        initialization_error_string = self.initialization_error_string

        descriptor_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.descriptor_for_type, Unset):
            descriptor_for_type = self.descriptor_for_type.to_dict()

        initialized = self.initialized

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if image_path_bytes is not UNSET:
            field_dict["imagePathBytes"] = image_path_bytes
        if build_bytes is not UNSET:
            field_dict["buildBytes"] = build_bytes
        if image_path is not UNSET:
            field_dict["imagePath"] = image_path
        if build is not UNSET:
            field_dict["build"] = build
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if unknown_fields is not UNSET:
            field_dict["unknownFields"] = unknown_fields
        if initialization_error_string is not UNSET:
            field_dict["initializationErrorString"] = initialization_error_string
        if descriptor_for_type is not UNSET:
            field_dict["descriptorForType"] = descriptor_for_type
        if initialized is not UNSET:
            field_dict["initialized"] = initialized

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.build_info_or_builder_all_fields import BuildInfoOrBuilderAllFields
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.message import Message
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _image_path_bytes = d.pop("imagePathBytes", UNSET)
        image_path_bytes: ByteString | Unset
        if isinstance(_image_path_bytes, Unset):
            image_path_bytes = UNSET
        else:
            image_path_bytes = ByteString.from_dict(_image_path_bytes)

        _build_bytes = d.pop("buildBytes", UNSET)
        build_bytes: ByteString | Unset
        if isinstance(_build_bytes, Unset):
            build_bytes = UNSET
        else:
            build_bytes = ByteString.from_dict(_build_bytes)

        image_path = d.pop("imagePath", UNSET)

        build = d.pop("build", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: BuildInfoOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = BuildInfoOrBuilderAllFields.from_dict(_all_fields)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: Message | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = Message.from_dict(_default_instance_for_type)

        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        initialized = d.pop("initialized", UNSET)

        build_info_or_builder = cls(
            image_path_bytes=image_path_bytes,
            build_bytes=build_bytes,
            image_path=image_path,
            build=build,
            all_fields=all_fields,
            default_instance_for_type=default_instance_for_type,
            unknown_fields=unknown_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            initialized=initialized,
        )

        build_info_or_builder.additional_properties = d
        return build_info_or_builder

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
