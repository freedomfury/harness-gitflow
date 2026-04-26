from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.parser import Parser


T = TypeVar("T", bound="UnknownFieldSet")


@_attrs_define
class UnknownFieldSet:
    """
    Attributes:
        empty (bool | Unset):
        initialized (bool | Unset):
        default_instance_for_type (UnknownFieldSet | Unset):
        parser_for_type (Parser | Unset):
        serialized_size (int | Unset):
        serialized_size_as_message_set (int | Unset):
    """

    empty: bool | Unset = UNSET
    initialized: bool | Unset = UNSET
    default_instance_for_type: UnknownFieldSet | Unset = UNSET
    parser_for_type: Parser | Unset = UNSET
    serialized_size: int | Unset = UNSET
    serialized_size_as_message_set: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        empty = self.empty

        initialized = self.initialized

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        serialized_size_as_message_set = self.serialized_size_as_message_set

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if empty is not UNSET:
            field_dict["empty"] = empty
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if serialized_size_as_message_set is not UNSET:
            field_dict["serializedSizeAsMessageSet"] = serialized_size_as_message_set

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.parser import Parser

        d = dict(src_dict)
        empty = d.pop("empty", UNSET)

        initialized = d.pop("initialized", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: UnknownFieldSet | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = UnknownFieldSet.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: Parser | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = Parser.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        serialized_size_as_message_set = d.pop("serializedSizeAsMessageSet", UNSET)

        unknown_field_set = cls(
            empty=empty,
            initialized=initialized,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            serialized_size_as_message_set=serialized_size_as_message_set,
        )

        unknown_field_set.additional_properties = d
        return unknown_field_set

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
