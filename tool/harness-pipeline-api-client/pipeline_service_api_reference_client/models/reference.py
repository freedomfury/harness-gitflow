from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.parser_reference import ParserReference
    from ..models.reference_all_fields import ReferenceAllFields
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="Reference")


@_attrs_define
class Reference:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        sha (str | Unset):
        path_bytes (ByteString | Unset):
        sha_bytes (ByteString | Unset):
        name (str | Unset):
        path (str | Unset):
        initialized (bool | Unset):
        default_instance_for_type (Reference | Unset):
        parser_for_type (ParserReference | Unset):
        serialized_size (int | Unset):
        name_bytes (ByteString | Unset):
        all_fields (ReferenceAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    sha: str | Unset = UNSET
    path_bytes: ByteString | Unset = UNSET
    sha_bytes: ByteString | Unset = UNSET
    name: str | Unset = UNSET
    path: str | Unset = UNSET
    initialized: bool | Unset = UNSET
    default_instance_for_type: Reference | Unset = UNSET
    parser_for_type: ParserReference | Unset = UNSET
    serialized_size: int | Unset = UNSET
    name_bytes: ByteString | Unset = UNSET
    all_fields: ReferenceAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        sha = self.sha

        path_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.path_bytes, Unset):
            path_bytes = self.path_bytes.to_dict()

        sha_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sha_bytes, Unset):
            sha_bytes = self.sha_bytes.to_dict()

        name = self.name

        path = self.path

        initialized = self.initialized

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.name_bytes, Unset):
            name_bytes = self.name_bytes.to_dict()

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
        if sha is not UNSET:
            field_dict["sha"] = sha
        if path_bytes is not UNSET:
            field_dict["pathBytes"] = path_bytes
        if sha_bytes is not UNSET:
            field_dict["shaBytes"] = sha_bytes
        if name is not UNSET:
            field_dict["name"] = name
        if path is not UNSET:
            field_dict["path"] = path
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if name_bytes is not UNSET:
            field_dict["nameBytes"] = name_bytes
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
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.parser_reference import ParserReference
        from ..models.reference_all_fields import ReferenceAllFields
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        sha = d.pop("sha", UNSET)

        _path_bytes = d.pop("pathBytes", UNSET)
        path_bytes: ByteString | Unset
        if isinstance(_path_bytes, Unset):
            path_bytes = UNSET
        else:
            path_bytes = ByteString.from_dict(_path_bytes)

        _sha_bytes = d.pop("shaBytes", UNSET)
        sha_bytes: ByteString | Unset
        if isinstance(_sha_bytes, Unset):
            sha_bytes = UNSET
        else:
            sha_bytes = ByteString.from_dict(_sha_bytes)

        name = d.pop("name", UNSET)

        path = d.pop("path", UNSET)

        initialized = d.pop("initialized", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: Reference | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = Reference.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserReference | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserReference.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _name_bytes = d.pop("nameBytes", UNSET)
        name_bytes: ByteString | Unset
        if isinstance(_name_bytes, Unset):
            name_bytes = UNSET
        else:
            name_bytes = ByteString.from_dict(_name_bytes)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: ReferenceAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = ReferenceAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        reference = cls(
            unknown_fields=unknown_fields,
            sha=sha,
            path_bytes=path_bytes,
            sha_bytes=sha_bytes,
            name=name,
            path=path,
            initialized=initialized,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            name_bytes=name_bytes,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        reference.additional_properties = d
        return reference

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
