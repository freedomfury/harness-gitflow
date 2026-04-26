from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.child import Child
    from ..models.child_or_builder import ChildOrBuilder
    from ..models.children_executable_response_all_fields import ChildrenExecutableResponseAllFields
    from ..models.descriptor import Descriptor
    from ..models.parser_children_executable_response import ParserChildrenExecutableResponse
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="ChildrenExecutableResponse")


@_attrs_define
class ChildrenExecutableResponse:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        children_count (int | Unset):
        units_list (list[str] | Unset):
        units_count (int | Unset):
        log_keys_count (int | Unset):
        log_keys_list (list[str] | Unset):
        children_or_builder_list (list[ChildOrBuilder] | Unset):
        children_list (list[Child] | Unset):
        initialized (bool | Unset):
        default_instance_for_type (ChildrenExecutableResponse | Unset):
        parser_for_type (ParserChildrenExecutableResponse | Unset):
        serialized_size (int | Unset):
        should_proceed_if_failed (bool | Unset):
        max_concurrency (int | Unset):
        all_fields (ChildrenExecutableResponseAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    children_count: int | Unset = UNSET
    units_list: list[str] | Unset = UNSET
    units_count: int | Unset = UNSET
    log_keys_count: int | Unset = UNSET
    log_keys_list: list[str] | Unset = UNSET
    children_or_builder_list: list[ChildOrBuilder] | Unset = UNSET
    children_list: list[Child] | Unset = UNSET
    initialized: bool | Unset = UNSET
    default_instance_for_type: ChildrenExecutableResponse | Unset = UNSET
    parser_for_type: ParserChildrenExecutableResponse | Unset = UNSET
    serialized_size: int | Unset = UNSET
    should_proceed_if_failed: bool | Unset = UNSET
    max_concurrency: int | Unset = UNSET
    all_fields: ChildrenExecutableResponseAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        children_count = self.children_count

        units_list: list[str] | Unset = UNSET
        if not isinstance(self.units_list, Unset):
            units_list = self.units_list

        units_count = self.units_count

        log_keys_count = self.log_keys_count

        log_keys_list: list[str] | Unset = UNSET
        if not isinstance(self.log_keys_list, Unset):
            log_keys_list = self.log_keys_list

        children_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children_or_builder_list, Unset):
            children_or_builder_list = []
            for children_or_builder_list_item_data in self.children_or_builder_list:
                children_or_builder_list_item = children_or_builder_list_item_data.to_dict()
                children_or_builder_list.append(children_or_builder_list_item)

        children_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children_list, Unset):
            children_list = []
            for children_list_item_data in self.children_list:
                children_list_item = children_list_item_data.to_dict()
                children_list.append(children_list_item)

        initialized = self.initialized

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        should_proceed_if_failed = self.should_proceed_if_failed

        max_concurrency = self.max_concurrency

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
        if children_count is not UNSET:
            field_dict["childrenCount"] = children_count
        if units_list is not UNSET:
            field_dict["unitsList"] = units_list
        if units_count is not UNSET:
            field_dict["unitsCount"] = units_count
        if log_keys_count is not UNSET:
            field_dict["logKeysCount"] = log_keys_count
        if log_keys_list is not UNSET:
            field_dict["logKeysList"] = log_keys_list
        if children_or_builder_list is not UNSET:
            field_dict["childrenOrBuilderList"] = children_or_builder_list
        if children_list is not UNSET:
            field_dict["childrenList"] = children_list
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if should_proceed_if_failed is not UNSET:
            field_dict["shouldProceedIfFailed"] = should_proceed_if_failed
        if max_concurrency is not UNSET:
            field_dict["maxConcurrency"] = max_concurrency
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
        from ..models.child import Child
        from ..models.child_or_builder import ChildOrBuilder
        from ..models.children_executable_response_all_fields import ChildrenExecutableResponseAllFields
        from ..models.descriptor import Descriptor
        from ..models.parser_children_executable_response import ParserChildrenExecutableResponse
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        children_count = d.pop("childrenCount", UNSET)

        units_list = cast(list[str], d.pop("unitsList", UNSET))

        units_count = d.pop("unitsCount", UNSET)

        log_keys_count = d.pop("logKeysCount", UNSET)

        log_keys_list = cast(list[str], d.pop("logKeysList", UNSET))

        _children_or_builder_list = d.pop("childrenOrBuilderList", UNSET)
        children_or_builder_list: list[ChildOrBuilder] | Unset = UNSET
        if _children_or_builder_list is not UNSET:
            children_or_builder_list = []
            for children_or_builder_list_item_data in _children_or_builder_list:
                children_or_builder_list_item = ChildOrBuilder.from_dict(children_or_builder_list_item_data)

                children_or_builder_list.append(children_or_builder_list_item)

        _children_list = d.pop("childrenList", UNSET)
        children_list: list[Child] | Unset = UNSET
        if _children_list is not UNSET:
            children_list = []
            for children_list_item_data in _children_list:
                children_list_item = Child.from_dict(children_list_item_data)

                children_list.append(children_list_item)

        initialized = d.pop("initialized", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: ChildrenExecutableResponse | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = ChildrenExecutableResponse.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserChildrenExecutableResponse | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserChildrenExecutableResponse.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        should_proceed_if_failed = d.pop("shouldProceedIfFailed", UNSET)

        max_concurrency = d.pop("maxConcurrency", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: ChildrenExecutableResponseAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = ChildrenExecutableResponseAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        children_executable_response = cls(
            unknown_fields=unknown_fields,
            children_count=children_count,
            units_list=units_list,
            units_count=units_count,
            log_keys_count=log_keys_count,
            log_keys_list=log_keys_list,
            children_or_builder_list=children_or_builder_list,
            children_list=children_list,
            initialized=initialized,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            should_proceed_if_failed=should_proceed_if_failed,
            max_concurrency=max_concurrency,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        children_executable_response.additional_properties = d
        return children_executable_response

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
