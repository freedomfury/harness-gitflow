from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_chain_executable_response_task_category import (
    TaskChainExecutableResponseTaskCategory,
    check_task_chain_executable_response_task_category,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.parser_task_chain_executable_response import ParserTaskChainExecutableResponse
    from ..models.task_chain_executable_response_all_fields import TaskChainExecutableResponseAllFields
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="TaskChainExecutableResponse")


@_attrs_define
class TaskChainExecutableResponse:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        chain_end (bool | Unset):
        pass_through_data (ByteString | Unset):
        task_category (TaskChainExecutableResponseTaskCategory | Unset):
        task_category_value (int | Unset):
        task_id_bytes (ByteString | Unset):
        units_list (list[str] | Unset):
        units_count (int | Unset):
        task_name_bytes (ByteString | Unset):
        log_keys_count (int | Unset):
        log_keys_list (list[str] | Unset):
        initialized (bool | Unset):
        default_instance_for_type (TaskChainExecutableResponse | Unset):
        parser_for_type (ParserTaskChainExecutableResponse | Unset):
        serialized_size (int | Unset):
        task_id (str | Unset):
        task_name (str | Unset):
        all_fields (TaskChainExecutableResponseAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    chain_end: bool | Unset = UNSET
    pass_through_data: ByteString | Unset = UNSET
    task_category: TaskChainExecutableResponseTaskCategory | Unset = UNSET
    task_category_value: int | Unset = UNSET
    task_id_bytes: ByteString | Unset = UNSET
    units_list: list[str] | Unset = UNSET
    units_count: int | Unset = UNSET
    task_name_bytes: ByteString | Unset = UNSET
    log_keys_count: int | Unset = UNSET
    log_keys_list: list[str] | Unset = UNSET
    initialized: bool | Unset = UNSET
    default_instance_for_type: TaskChainExecutableResponse | Unset = UNSET
    parser_for_type: ParserTaskChainExecutableResponse | Unset = UNSET
    serialized_size: int | Unset = UNSET
    task_id: str | Unset = UNSET
    task_name: str | Unset = UNSET
    all_fields: TaskChainExecutableResponseAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        chain_end = self.chain_end

        pass_through_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pass_through_data, Unset):
            pass_through_data = self.pass_through_data.to_dict()

        task_category: str | Unset = UNSET
        if not isinstance(self.task_category, Unset):
            task_category = self.task_category

        task_category_value = self.task_category_value

        task_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.task_id_bytes, Unset):
            task_id_bytes = self.task_id_bytes.to_dict()

        units_list: list[str] | Unset = UNSET
        if not isinstance(self.units_list, Unset):
            units_list = self.units_list

        units_count = self.units_count

        task_name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.task_name_bytes, Unset):
            task_name_bytes = self.task_name_bytes.to_dict()

        log_keys_count = self.log_keys_count

        log_keys_list: list[str] | Unset = UNSET
        if not isinstance(self.log_keys_list, Unset):
            log_keys_list = self.log_keys_list

        initialized = self.initialized

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        task_id = self.task_id

        task_name = self.task_name

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
        if chain_end is not UNSET:
            field_dict["chainEnd"] = chain_end
        if pass_through_data is not UNSET:
            field_dict["passThroughData"] = pass_through_data
        if task_category is not UNSET:
            field_dict["taskCategory"] = task_category
        if task_category_value is not UNSET:
            field_dict["taskCategoryValue"] = task_category_value
        if task_id_bytes is not UNSET:
            field_dict["taskIdBytes"] = task_id_bytes
        if units_list is not UNSET:
            field_dict["unitsList"] = units_list
        if units_count is not UNSET:
            field_dict["unitsCount"] = units_count
        if task_name_bytes is not UNSET:
            field_dict["taskNameBytes"] = task_name_bytes
        if log_keys_count is not UNSET:
            field_dict["logKeysCount"] = log_keys_count
        if log_keys_list is not UNSET:
            field_dict["logKeysList"] = log_keys_list
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if task_name is not UNSET:
            field_dict["taskName"] = task_name
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
        from ..models.parser_task_chain_executable_response import ParserTaskChainExecutableResponse
        from ..models.task_chain_executable_response_all_fields import TaskChainExecutableResponseAllFields
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        chain_end = d.pop("chainEnd", UNSET)

        _pass_through_data = d.pop("passThroughData", UNSET)
        pass_through_data: ByteString | Unset
        if isinstance(_pass_through_data, Unset):
            pass_through_data = UNSET
        else:
            pass_through_data = ByteString.from_dict(_pass_through_data)

        _task_category = d.pop("taskCategory", UNSET)
        task_category: TaskChainExecutableResponseTaskCategory | Unset
        if isinstance(_task_category, Unset):
            task_category = UNSET
        else:
            task_category = check_task_chain_executable_response_task_category(_task_category)

        task_category_value = d.pop("taskCategoryValue", UNSET)

        _task_id_bytes = d.pop("taskIdBytes", UNSET)
        task_id_bytes: ByteString | Unset
        if isinstance(_task_id_bytes, Unset):
            task_id_bytes = UNSET
        else:
            task_id_bytes = ByteString.from_dict(_task_id_bytes)

        units_list = cast(list[str], d.pop("unitsList", UNSET))

        units_count = d.pop("unitsCount", UNSET)

        _task_name_bytes = d.pop("taskNameBytes", UNSET)
        task_name_bytes: ByteString | Unset
        if isinstance(_task_name_bytes, Unset):
            task_name_bytes = UNSET
        else:
            task_name_bytes = ByteString.from_dict(_task_name_bytes)

        log_keys_count = d.pop("logKeysCount", UNSET)

        log_keys_list = cast(list[str], d.pop("logKeysList", UNSET))

        initialized = d.pop("initialized", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: TaskChainExecutableResponse | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = TaskChainExecutableResponse.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserTaskChainExecutableResponse | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserTaskChainExecutableResponse.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        task_id = d.pop("taskId", UNSET)

        task_name = d.pop("taskName", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: TaskChainExecutableResponseAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = TaskChainExecutableResponseAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        task_chain_executable_response = cls(
            unknown_fields=unknown_fields,
            chain_end=chain_end,
            pass_through_data=pass_through_data,
            task_category=task_category,
            task_category_value=task_category_value,
            task_id_bytes=task_id_bytes,
            units_list=units_list,
            units_count=units_count,
            task_name_bytes=task_name_bytes,
            log_keys_count=log_keys_count,
            log_keys_list=log_keys_list,
            initialized=initialized,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            task_id=task_id,
            task_name=task_name,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        task_chain_executable_response.additional_properties = d
        return task_chain_executable_response

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
