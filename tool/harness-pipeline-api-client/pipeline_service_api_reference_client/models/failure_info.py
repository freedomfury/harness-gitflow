from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.failure_info_failure_types_list_item import (
    FailureInfoFailureTypesListItem,
    check_failure_info_failure_types_list_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.failure_data import FailureData
    from ..models.failure_data_or_builder import FailureDataOrBuilder
    from ..models.failure_info_all_fields import FailureInfoAllFields
    from ..models.parser_failure_info import ParserFailureInfo
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="FailureInfo")


@_attrs_define
class FailureInfo:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        error_message (str | Unset):
        initialized (bool | Unset):
        default_instance_for_type (FailureInfo | Unset):
        parser_for_type (ParserFailureInfo | Unset):
        serialized_size (int | Unset):
        error_message_bytes (ByteString | Unset):
        failure_types_list (list[FailureInfoFailureTypesListItem] | Unset):
        failure_types_count (int | Unset):
        failure_types_value_list (list[int] | Unset):
        failure_data_list (list[FailureData] | Unset):
        failure_data_count (int | Unset):
        failure_data_or_builder_list (list[FailureDataOrBuilder] | Unset):
        all_fields (FailureInfoAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    error_message: str | Unset = UNSET
    initialized: bool | Unset = UNSET
    default_instance_for_type: FailureInfo | Unset = UNSET
    parser_for_type: ParserFailureInfo | Unset = UNSET
    serialized_size: int | Unset = UNSET
    error_message_bytes: ByteString | Unset = UNSET
    failure_types_list: list[FailureInfoFailureTypesListItem] | Unset = UNSET
    failure_types_count: int | Unset = UNSET
    failure_types_value_list: list[int] | Unset = UNSET
    failure_data_list: list[FailureData] | Unset = UNSET
    failure_data_count: int | Unset = UNSET
    failure_data_or_builder_list: list[FailureDataOrBuilder] | Unset = UNSET
    all_fields: FailureInfoAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        error_message = self.error_message

        initialized = self.initialized

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        error_message_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error_message_bytes, Unset):
            error_message_bytes = self.error_message_bytes.to_dict()

        failure_types_list: list[str] | Unset = UNSET
        if not isinstance(self.failure_types_list, Unset):
            failure_types_list = []
            for failure_types_list_item_data in self.failure_types_list:
                failure_types_list_item: str = failure_types_list_item_data
                failure_types_list.append(failure_types_list_item)

        failure_types_count = self.failure_types_count

        failure_types_value_list: list[int] | Unset = UNSET
        if not isinstance(self.failure_types_value_list, Unset):
            failure_types_value_list = self.failure_types_value_list

        failure_data_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failure_data_list, Unset):
            failure_data_list = []
            for failure_data_list_item_data in self.failure_data_list:
                failure_data_list_item = failure_data_list_item_data.to_dict()
                failure_data_list.append(failure_data_list_item)

        failure_data_count = self.failure_data_count

        failure_data_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failure_data_or_builder_list, Unset):
            failure_data_or_builder_list = []
            for failure_data_or_builder_list_item_data in self.failure_data_or_builder_list:
                failure_data_or_builder_list_item = failure_data_or_builder_list_item_data.to_dict()
                failure_data_or_builder_list.append(failure_data_or_builder_list_item)

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
        if error_message is not UNSET:
            field_dict["errorMessage"] = error_message
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if error_message_bytes is not UNSET:
            field_dict["errorMessageBytes"] = error_message_bytes
        if failure_types_list is not UNSET:
            field_dict["failureTypesList"] = failure_types_list
        if failure_types_count is not UNSET:
            field_dict["failureTypesCount"] = failure_types_count
        if failure_types_value_list is not UNSET:
            field_dict["failureTypesValueList"] = failure_types_value_list
        if failure_data_list is not UNSET:
            field_dict["failureDataList"] = failure_data_list
        if failure_data_count is not UNSET:
            field_dict["failureDataCount"] = failure_data_count
        if failure_data_or_builder_list is not UNSET:
            field_dict["failureDataOrBuilderList"] = failure_data_or_builder_list
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
        from ..models.failure_data import FailureData
        from ..models.failure_data_or_builder import FailureDataOrBuilder
        from ..models.failure_info_all_fields import FailureInfoAllFields
        from ..models.parser_failure_info import ParserFailureInfo
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        error_message = d.pop("errorMessage", UNSET)

        initialized = d.pop("initialized", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: FailureInfo | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = FailureInfo.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserFailureInfo | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserFailureInfo.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _error_message_bytes = d.pop("errorMessageBytes", UNSET)
        error_message_bytes: ByteString | Unset
        if isinstance(_error_message_bytes, Unset):
            error_message_bytes = UNSET
        else:
            error_message_bytes = ByteString.from_dict(_error_message_bytes)

        _failure_types_list = d.pop("failureTypesList", UNSET)
        failure_types_list: list[FailureInfoFailureTypesListItem] | Unset = UNSET
        if _failure_types_list is not UNSET:
            failure_types_list = []
            for failure_types_list_item_data in _failure_types_list:
                failure_types_list_item = check_failure_info_failure_types_list_item(failure_types_list_item_data)

                failure_types_list.append(failure_types_list_item)

        failure_types_count = d.pop("failureTypesCount", UNSET)

        failure_types_value_list = cast(list[int], d.pop("failureTypesValueList", UNSET))

        _failure_data_list = d.pop("failureDataList", UNSET)
        failure_data_list: list[FailureData] | Unset = UNSET
        if _failure_data_list is not UNSET:
            failure_data_list = []
            for failure_data_list_item_data in _failure_data_list:
                failure_data_list_item = FailureData.from_dict(failure_data_list_item_data)

                failure_data_list.append(failure_data_list_item)

        failure_data_count = d.pop("failureDataCount", UNSET)

        _failure_data_or_builder_list = d.pop("failureDataOrBuilderList", UNSET)
        failure_data_or_builder_list: list[FailureDataOrBuilder] | Unset = UNSET
        if _failure_data_or_builder_list is not UNSET:
            failure_data_or_builder_list = []
            for failure_data_or_builder_list_item_data in _failure_data_or_builder_list:
                failure_data_or_builder_list_item = FailureDataOrBuilder.from_dict(
                    failure_data_or_builder_list_item_data
                )

                failure_data_or_builder_list.append(failure_data_or_builder_list_item)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: FailureInfoAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = FailureInfoAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        failure_info = cls(
            unknown_fields=unknown_fields,
            error_message=error_message,
            initialized=initialized,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            error_message_bytes=error_message_bytes,
            failure_types_list=failure_types_list,
            failure_types_count=failure_types_count,
            failure_types_value_list=failure_types_value_list,
            failure_data_list=failure_data_list,
            failure_data_count=failure_data_count,
            failure_data_or_builder_list=failure_data_or_builder_list,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        failure_info.additional_properties = d
        return failure_info

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
