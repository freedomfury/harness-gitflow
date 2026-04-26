from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.build_info_all_fields import BuildInfoAllFields
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.parser_build_info import ParserBuildInfo
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="BuildInfo")


@_attrs_define
class BuildInfo:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        image_path_bytes (ByteString | Unset):
        build_bytes (ByteString | Unset):
        image_path (str | Unset):
        initialized (bool | Unset):
        default_instance_for_type (BuildInfo | Unset):
        parser_for_type (ParserBuildInfo | Unset):
        serialized_size (int | Unset):
        build (str | Unset):
        all_fields (BuildInfoAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    image_path_bytes: ByteString | Unset = UNSET
    build_bytes: ByteString | Unset = UNSET
    image_path: str | Unset = UNSET
    initialized: bool | Unset = UNSET
    default_instance_for_type: BuildInfo | Unset = UNSET
    parser_for_type: ParserBuildInfo | Unset = UNSET
    serialized_size: int | Unset = UNSET
    build: str | Unset = UNSET
    all_fields: BuildInfoAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        image_path_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.image_path_bytes, Unset):
            image_path_bytes = self.image_path_bytes.to_dict()

        build_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.build_bytes, Unset):
            build_bytes = self.build_bytes.to_dict()

        image_path = self.image_path

        initialized = self.initialized

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        build = self.build

        all_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields, Unset):
            all_fields = self.all_fields.to_dict()

        initialization_error_string = self.initialization_error_string

        descriptor_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.descriptor_for_type, Unset):
            descriptor_for_type = self.descriptor_for_type.to_dict()

        memoized_serialized_size = self.memoized_serialized_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unknown_fields is not UNSET:
            field_dict["unknownFields"] = unknown_fields
        if image_path_bytes is not UNSET:
            field_dict["imagePathBytes"] = image_path_bytes
        if build_bytes is not UNSET:
            field_dict["buildBytes"] = build_bytes
        if image_path is not UNSET:
            field_dict["imagePath"] = image_path
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if build is not UNSET:
            field_dict["build"] = build
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if initialization_error_string is not UNSET:
            field_dict["initializationErrorString"] = initialization_error_string
        if descriptor_for_type is not UNSET:
            field_dict["descriptorForType"] = descriptor_for_type
        if memoized_serialized_size is not UNSET:
            field_dict["memoizedSerializedSize"] = memoized_serialized_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.build_info_all_fields import BuildInfoAllFields
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.parser_build_info import ParserBuildInfo
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

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

        initialized = d.pop("initialized", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: BuildInfo | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = BuildInfo.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserBuildInfo | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserBuildInfo.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        build = d.pop("build", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: BuildInfoAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = BuildInfoAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        build_info = cls(
            unknown_fields=unknown_fields,
            image_path_bytes=image_path_bytes,
            build_bytes=build_bytes,
            image_path=image_path,
            initialized=initialized,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            build=build,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        build_info.additional_properties = d
        return build_info

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
