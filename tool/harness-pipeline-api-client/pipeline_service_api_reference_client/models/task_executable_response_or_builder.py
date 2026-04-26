from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.task_executable_response_or_builder_task_category import (
    TaskExecutableResponseOrBuilderTaskCategory,
    check_task_executable_response_or_builder_task_category,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.message import Message
    from ..models.task_executable_response_or_builder_all_fields import TaskExecutableResponseOrBuilderAllFields
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="TaskExecutableResponseOrBuilder")


@_attrs_define
class TaskExecutableResponseOrBuilder:
    """
    Attributes:
        task_category (TaskExecutableResponseOrBuilderTaskCategory | Unset):
        task_category_value (int | Unset):
        task_id_bytes (ByteString | Unset):
        units_list (list[str] | Unset):
        units_count (int | Unset):
        task_name_bytes (ByteString | Unset):
        log_keys_count (int | Unset):
        log_keys_list (list[str] | Unset):
        task_id (str | Unset):
        task_name (str | Unset):
        all_fields (TaskExecutableResponseOrBuilderAllFields | Unset):
        default_instance_for_type (Message | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        initialized (bool | Unset):
    """

    task_category: TaskExecutableResponseOrBuilderTaskCategory | Unset = UNSET
    task_category_value: int | Unset = UNSET
    task_id_bytes: ByteString | Unset = UNSET
    units_list: list[str] | Unset = UNSET
    units_count: int | Unset = UNSET
    task_name_bytes: ByteString | Unset = UNSET
    log_keys_count: int | Unset = UNSET
    log_keys_list: list[str] | Unset = UNSET
    task_id: str | Unset = UNSET
    task_name: str | Unset = UNSET
    all_fields: TaskExecutableResponseOrBuilderAllFields | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
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

        task_id = self.task_id

        task_name = self.task_name

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
        if task_id is not UNSET:
            field_dict["taskId"] = task_id
        if task_name is not UNSET:
            field_dict["taskName"] = task_name
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
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.message import Message
        from ..models.task_executable_response_or_builder_all_fields import TaskExecutableResponseOrBuilderAllFields
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _task_category = d.pop("taskCategory", UNSET)
        task_category: TaskExecutableResponseOrBuilderTaskCategory | Unset
        if isinstance(_task_category, Unset):
            task_category = UNSET
        else:
            task_category = check_task_executable_response_or_builder_task_category(_task_category)

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

        task_id = d.pop("taskId", UNSET)

        task_name = d.pop("taskName", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: TaskExecutableResponseOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = TaskExecutableResponseOrBuilderAllFields.from_dict(_all_fields)

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

        task_executable_response_or_builder = cls(
            task_category=task_category,
            task_category_value=task_category_value,
            task_id_bytes=task_id_bytes,
            units_list=units_list,
            units_count=units_count,
            task_name_bytes=task_name_bytes,
            log_keys_count=log_keys_count,
            log_keys_list=log_keys_list,
            task_id=task_id,
            task_name=task_name,
            all_fields=all_fields,
            default_instance_for_type=default_instance_for_type,
            unknown_fields=unknown_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            initialized=initialized,
        )

        task_executable_response_or_builder.additional_properties = d
        return task_executable_response_or_builder

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
