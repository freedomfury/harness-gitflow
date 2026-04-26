from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.failure_data_failure_types_list_item import (
    FailureDataFailureTypesListItem,
    check_failure_data_failure_types_list_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.failure_data_all_fields import FailureDataAllFields
    from ..models.failure_type_info import FailureTypeInfo
    from ..models.failure_type_info_or_builder import FailureTypeInfoOrBuilder
    from ..models.parser_failure_data import ParserFailureData
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="FailureData")


@_attrs_define
class FailureData:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        failure_type_infos_count (int | Unset):
        failure_type_infos_or_builder_list (list[FailureTypeInfoOrBuilder] | Unset):
        code_bytes (ByteString | Unset):
        level_bytes (ByteString | Unset):
        step_identifier_bytes (ByteString | Unset):
        stage_identifier_bytes (ByteString | Unset):
        failure_type_infos_list (list[FailureTypeInfo] | Unset):
        message (str | Unset):
        level (str | Unset):
        initialized (bool | Unset):
        code (str | Unset):
        default_instance_for_type (FailureData | Unset):
        parser_for_type (ParserFailureData | Unset):
        serialized_size (int | Unset):
        failure_types_list (list[FailureDataFailureTypesListItem] | Unset):
        failure_types_count (int | Unset):
        failure_types_value_list (list[int] | Unset):
        message_bytes (ByteString | Unset):
        stage_identifier (str | Unset):
        step_identifier (str | Unset):
        all_fields (FailureDataAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    failure_type_infos_count: int | Unset = UNSET
    failure_type_infos_or_builder_list: list[FailureTypeInfoOrBuilder] | Unset = UNSET
    code_bytes: ByteString | Unset = UNSET
    level_bytes: ByteString | Unset = UNSET
    step_identifier_bytes: ByteString | Unset = UNSET
    stage_identifier_bytes: ByteString | Unset = UNSET
    failure_type_infos_list: list[FailureTypeInfo] | Unset = UNSET
    message: str | Unset = UNSET
    level: str | Unset = UNSET
    initialized: bool | Unset = UNSET
    code: str | Unset = UNSET
    default_instance_for_type: FailureData | Unset = UNSET
    parser_for_type: ParserFailureData | Unset = UNSET
    serialized_size: int | Unset = UNSET
    failure_types_list: list[FailureDataFailureTypesListItem] | Unset = UNSET
    failure_types_count: int | Unset = UNSET
    failure_types_value_list: list[int] | Unset = UNSET
    message_bytes: ByteString | Unset = UNSET
    stage_identifier: str | Unset = UNSET
    step_identifier: str | Unset = UNSET
    all_fields: FailureDataAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        failure_type_infos_count = self.failure_type_infos_count

        failure_type_infos_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failure_type_infos_or_builder_list, Unset):
            failure_type_infos_or_builder_list = []
            for failure_type_infos_or_builder_list_item_data in self.failure_type_infos_or_builder_list:
                failure_type_infos_or_builder_list_item = failure_type_infos_or_builder_list_item_data.to_dict()
                failure_type_infos_or_builder_list.append(failure_type_infos_or_builder_list_item)

        code_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.code_bytes, Unset):
            code_bytes = self.code_bytes.to_dict()

        level_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.level_bytes, Unset):
            level_bytes = self.level_bytes.to_dict()

        step_identifier_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.step_identifier_bytes, Unset):
            step_identifier_bytes = self.step_identifier_bytes.to_dict()

        stage_identifier_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stage_identifier_bytes, Unset):
            stage_identifier_bytes = self.stage_identifier_bytes.to_dict()

        failure_type_infos_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.failure_type_infos_list, Unset):
            failure_type_infos_list = []
            for failure_type_infos_list_item_data in self.failure_type_infos_list:
                failure_type_infos_list_item = failure_type_infos_list_item_data.to_dict()
                failure_type_infos_list.append(failure_type_infos_list_item)

        message = self.message

        level = self.level

        initialized = self.initialized

        code = self.code

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

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

        message_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.message_bytes, Unset):
            message_bytes = self.message_bytes.to_dict()

        stage_identifier = self.stage_identifier

        step_identifier = self.step_identifier

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
        if failure_type_infos_count is not UNSET:
            field_dict["failureTypeInfosCount"] = failure_type_infos_count
        if failure_type_infos_or_builder_list is not UNSET:
            field_dict["failureTypeInfosOrBuilderList"] = failure_type_infos_or_builder_list
        if code_bytes is not UNSET:
            field_dict["codeBytes"] = code_bytes
        if level_bytes is not UNSET:
            field_dict["levelBytes"] = level_bytes
        if step_identifier_bytes is not UNSET:
            field_dict["stepIdentifierBytes"] = step_identifier_bytes
        if stage_identifier_bytes is not UNSET:
            field_dict["stageIdentifierBytes"] = stage_identifier_bytes
        if failure_type_infos_list is not UNSET:
            field_dict["failureTypeInfosList"] = failure_type_infos_list
        if message is not UNSET:
            field_dict["message"] = message
        if level is not UNSET:
            field_dict["level"] = level
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if code is not UNSET:
            field_dict["code"] = code
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if failure_types_list is not UNSET:
            field_dict["failureTypesList"] = failure_types_list
        if failure_types_count is not UNSET:
            field_dict["failureTypesCount"] = failure_types_count
        if failure_types_value_list is not UNSET:
            field_dict["failureTypesValueList"] = failure_types_value_list
        if message_bytes is not UNSET:
            field_dict["messageBytes"] = message_bytes
        if stage_identifier is not UNSET:
            field_dict["stageIdentifier"] = stage_identifier
        if step_identifier is not UNSET:
            field_dict["stepIdentifier"] = step_identifier
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
        from ..models.failure_data_all_fields import FailureDataAllFields
        from ..models.failure_type_info import FailureTypeInfo
        from ..models.failure_type_info_or_builder import FailureTypeInfoOrBuilder
        from ..models.parser_failure_data import ParserFailureData
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        failure_type_infos_count = d.pop("failureTypeInfosCount", UNSET)

        _failure_type_infos_or_builder_list = d.pop("failureTypeInfosOrBuilderList", UNSET)
        failure_type_infos_or_builder_list: list[FailureTypeInfoOrBuilder] | Unset = UNSET
        if _failure_type_infos_or_builder_list is not UNSET:
            failure_type_infos_or_builder_list = []
            for failure_type_infos_or_builder_list_item_data in _failure_type_infos_or_builder_list:
                failure_type_infos_or_builder_list_item = FailureTypeInfoOrBuilder.from_dict(
                    failure_type_infos_or_builder_list_item_data
                )

                failure_type_infos_or_builder_list.append(failure_type_infos_or_builder_list_item)

        _code_bytes = d.pop("codeBytes", UNSET)
        code_bytes: ByteString | Unset
        if isinstance(_code_bytes, Unset):
            code_bytes = UNSET
        else:
            code_bytes = ByteString.from_dict(_code_bytes)

        _level_bytes = d.pop("levelBytes", UNSET)
        level_bytes: ByteString | Unset
        if isinstance(_level_bytes, Unset):
            level_bytes = UNSET
        else:
            level_bytes = ByteString.from_dict(_level_bytes)

        _step_identifier_bytes = d.pop("stepIdentifierBytes", UNSET)
        step_identifier_bytes: ByteString | Unset
        if isinstance(_step_identifier_bytes, Unset):
            step_identifier_bytes = UNSET
        else:
            step_identifier_bytes = ByteString.from_dict(_step_identifier_bytes)

        _stage_identifier_bytes = d.pop("stageIdentifierBytes", UNSET)
        stage_identifier_bytes: ByteString | Unset
        if isinstance(_stage_identifier_bytes, Unset):
            stage_identifier_bytes = UNSET
        else:
            stage_identifier_bytes = ByteString.from_dict(_stage_identifier_bytes)

        _failure_type_infos_list = d.pop("failureTypeInfosList", UNSET)
        failure_type_infos_list: list[FailureTypeInfo] | Unset = UNSET
        if _failure_type_infos_list is not UNSET:
            failure_type_infos_list = []
            for failure_type_infos_list_item_data in _failure_type_infos_list:
                failure_type_infos_list_item = FailureTypeInfo.from_dict(failure_type_infos_list_item_data)

                failure_type_infos_list.append(failure_type_infos_list_item)

        message = d.pop("message", UNSET)

        level = d.pop("level", UNSET)

        initialized = d.pop("initialized", UNSET)

        code = d.pop("code", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: FailureData | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = FailureData.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserFailureData | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserFailureData.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _failure_types_list = d.pop("failureTypesList", UNSET)
        failure_types_list: list[FailureDataFailureTypesListItem] | Unset = UNSET
        if _failure_types_list is not UNSET:
            failure_types_list = []
            for failure_types_list_item_data in _failure_types_list:
                failure_types_list_item = check_failure_data_failure_types_list_item(failure_types_list_item_data)

                failure_types_list.append(failure_types_list_item)

        failure_types_count = d.pop("failureTypesCount", UNSET)

        failure_types_value_list = cast(list[int], d.pop("failureTypesValueList", UNSET))

        _message_bytes = d.pop("messageBytes", UNSET)
        message_bytes: ByteString | Unset
        if isinstance(_message_bytes, Unset):
            message_bytes = UNSET
        else:
            message_bytes = ByteString.from_dict(_message_bytes)

        stage_identifier = d.pop("stageIdentifier", UNSET)

        step_identifier = d.pop("stepIdentifier", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: FailureDataAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = FailureDataAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        failure_data = cls(
            unknown_fields=unknown_fields,
            failure_type_infos_count=failure_type_infos_count,
            failure_type_infos_or_builder_list=failure_type_infos_or_builder_list,
            code_bytes=code_bytes,
            level_bytes=level_bytes,
            step_identifier_bytes=step_identifier_bytes,
            stage_identifier_bytes=stage_identifier_bytes,
            failure_type_infos_list=failure_type_infos_list,
            message=message,
            level=level,
            initialized=initialized,
            code=code,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            failure_types_list=failure_types_list,
            failure_types_count=failure_types_count,
            failure_types_value_list=failure_types_value_list,
            message_bytes=message_bytes,
            stage_identifier=stage_identifier,
            step_identifier=step_identifier,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        failure_data.additional_properties = d
        return failure_data

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
