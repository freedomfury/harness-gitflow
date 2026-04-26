from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.descriptor import Descriptor
    from ..models.parser_reserved_range import ParserReservedRange
    from ..models.reserved_range_all_fields import ReservedRangeAllFields
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="ReservedRange")


@_attrs_define
class ReservedRange:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        start (int | Unset):
        parser_for_type (ParserReservedRange | Unset):
        serialized_size (int | Unset):
        end (int | Unset):
        default_instance_for_type (ReservedRange | Unset):
        initialized (bool | Unset):
        initialization_error_string (str | Unset):
        all_fields (ReservedRangeAllFields | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    start: int | Unset = UNSET
    parser_for_type: ParserReservedRange | Unset = UNSET
    serialized_size: int | Unset = UNSET
    end: int | Unset = UNSET
    default_instance_for_type: ReservedRange | Unset = UNSET
    initialized: bool | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    all_fields: ReservedRangeAllFields | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        start = self.start

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        end = self.end

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
        if start is not UNSET:
            field_dict["start"] = start
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if end is not UNSET:
            field_dict["end"] = end
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
        from ..models.descriptor import Descriptor
        from ..models.parser_reserved_range import ParserReservedRange
        from ..models.reserved_range_all_fields import ReservedRangeAllFields
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        start = d.pop("start", UNSET)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserReservedRange | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserReservedRange.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        end = d.pop("end", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: ReservedRange | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = ReservedRange.from_dict(_default_instance_for_type)

        initialized = d.pop("initialized", UNSET)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: ReservedRangeAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = ReservedRangeAllFields.from_dict(_all_fields)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        reserved_range = cls(
            unknown_fields=unknown_fields,
            start=start,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            end=end,
            default_instance_for_type=default_instance_for_type,
            initialized=initialized,
            initialization_error_string=initialization_error_string,
            all_fields=all_fields,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        reserved_range.additional_properties = d
        return reserved_range

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
