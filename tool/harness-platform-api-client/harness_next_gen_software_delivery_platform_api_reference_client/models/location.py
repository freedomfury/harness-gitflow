from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.location_all_fields import LocationAllFields
    from ..models.parser_location import ParserLocation
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="Location")


@_attrs_define
class Location:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        path_count (int | Unset):
        span_list (list[int] | Unset):
        span_count (int | Unset):
        leading_comments (str | Unset):
        leading_comments_bytes (ByteString | Unset):
        trailing_comments (str | Unset):
        trailing_comments_bytes (ByteString | Unset):
        leading_detached_comments_list (list[str] | Unset):
        leading_detached_comments_count (int | Unset):
        path_list (list[int] | Unset):
        parser_for_type (ParserLocation | Unset):
        serialized_size (int | Unset):
        default_instance_for_type (Location | Unset):
        initialized (bool | Unset):
        initialization_error_string (str | Unset):
        all_fields (LocationAllFields | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    path_count: int | Unset = UNSET
    span_list: list[int] | Unset = UNSET
    span_count: int | Unset = UNSET
    leading_comments: str | Unset = UNSET
    leading_comments_bytes: ByteString | Unset = UNSET
    trailing_comments: str | Unset = UNSET
    trailing_comments_bytes: ByteString | Unset = UNSET
    leading_detached_comments_list: list[str] | Unset = UNSET
    leading_detached_comments_count: int | Unset = UNSET
    path_list: list[int] | Unset = UNSET
    parser_for_type: ParserLocation | Unset = UNSET
    serialized_size: int | Unset = UNSET
    default_instance_for_type: Location | Unset = UNSET
    initialized: bool | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    all_fields: LocationAllFields | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        path_count = self.path_count

        span_list: list[int] | Unset = UNSET
        if not isinstance(self.span_list, Unset):
            span_list = self.span_list

        span_count = self.span_count

        leading_comments = self.leading_comments

        leading_comments_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.leading_comments_bytes, Unset):
            leading_comments_bytes = self.leading_comments_bytes.to_dict()

        trailing_comments = self.trailing_comments

        trailing_comments_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trailing_comments_bytes, Unset):
            trailing_comments_bytes = self.trailing_comments_bytes.to_dict()

        leading_detached_comments_list: list[str] | Unset = UNSET
        if not isinstance(self.leading_detached_comments_list, Unset):
            leading_detached_comments_list = self.leading_detached_comments_list

        leading_detached_comments_count = self.leading_detached_comments_count

        path_list: list[int] | Unset = UNSET
        if not isinstance(self.path_list, Unset):
            path_list = self.path_list

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        initialized = self.initialized

        initialization_error_string = self.initialization_error_string

        all_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.all_fields, Unset):
            all_fields = self.all_fields.to_dict()

        descriptor_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.descriptor_for_type, Unset):
            descriptor_for_type = self.descriptor_for_type.to_dict()

        memoized_serialized_size = self.memoized_serialized_size

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if unknown_fields is not UNSET:
            field_dict["unknownFields"] = unknown_fields
        if path_count is not UNSET:
            field_dict["pathCount"] = path_count
        if span_list is not UNSET:
            field_dict["spanList"] = span_list
        if span_count is not UNSET:
            field_dict["spanCount"] = span_count
        if leading_comments is not UNSET:
            field_dict["leadingComments"] = leading_comments
        if leading_comments_bytes is not UNSET:
            field_dict["leadingCommentsBytes"] = leading_comments_bytes
        if trailing_comments is not UNSET:
            field_dict["trailingComments"] = trailing_comments
        if trailing_comments_bytes is not UNSET:
            field_dict["trailingCommentsBytes"] = trailing_comments_bytes
        if leading_detached_comments_list is not UNSET:
            field_dict["leadingDetachedCommentsList"] = leading_detached_comments_list
        if leading_detached_comments_count is not UNSET:
            field_dict["leadingDetachedCommentsCount"] = leading_detached_comments_count
        if path_list is not UNSET:
            field_dict["pathList"] = path_list
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if initialization_error_string is not UNSET:
            field_dict["initializationErrorString"] = initialization_error_string
        if all_fields is not UNSET:
            field_dict["allFields"] = all_fields
        if descriptor_for_type is not UNSET:
            field_dict["descriptorForType"] = descriptor_for_type
        if memoized_serialized_size is not UNSET:
            field_dict["memoizedSerializedSize"] = memoized_serialized_size

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.location_all_fields import LocationAllFields
        from ..models.parser_location import ParserLocation
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        path_count = d.pop("pathCount", UNSET)

        span_list = cast(list[int], d.pop("spanList", UNSET))

        span_count = d.pop("spanCount", UNSET)

        leading_comments = d.pop("leadingComments", UNSET)

        _leading_comments_bytes = d.pop("leadingCommentsBytes", UNSET)
        leading_comments_bytes: ByteString | Unset
        if isinstance(_leading_comments_bytes, Unset):
            leading_comments_bytes = UNSET
        else:
            leading_comments_bytes = ByteString.from_dict(_leading_comments_bytes)

        trailing_comments = d.pop("trailingComments", UNSET)

        _trailing_comments_bytes = d.pop("trailingCommentsBytes", UNSET)
        trailing_comments_bytes: ByteString | Unset
        if isinstance(_trailing_comments_bytes, Unset):
            trailing_comments_bytes = UNSET
        else:
            trailing_comments_bytes = ByteString.from_dict(_trailing_comments_bytes)

        leading_detached_comments_list = cast(list[str], d.pop("leadingDetachedCommentsList", UNSET))

        leading_detached_comments_count = d.pop("leadingDetachedCommentsCount", UNSET)

        path_list = cast(list[int], d.pop("pathList", UNSET))

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserLocation | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserLocation.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: Location | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = Location.from_dict(_default_instance_for_type)

        initialized = d.pop("initialized", UNSET)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: LocationAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = LocationAllFields.from_dict(_all_fields)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        location = cls(
            unknown_fields=unknown_fields,
            path_count=path_count,
            span_list=span_list,
            span_count=span_count,
            leading_comments=leading_comments,
            leading_comments_bytes=leading_comments_bytes,
            trailing_comments=trailing_comments,
            trailing_comments_bytes=trailing_comments_bytes,
            leading_detached_comments_list=leading_detached_comments_list,
            leading_detached_comments_count=leading_detached_comments_count,
            path_list=path_list,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            default_instance_for_type=default_instance_for_type,
            initialized=initialized,
            initialization_error_string=initialization_error_string,
            all_fields=all_fields,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        location.additional_properties = d
        return location

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
