from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.async_executable_response_or_builder_status import (
    AsyncExecutableResponseOrBuilderStatus,
    check_async_executable_response_or_builder_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.async_executable_response_or_builder_all_fields import AsyncExecutableResponseOrBuilderAllFields
    from ..models.descriptor import Descriptor
    from ..models.message import Message
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="AsyncExecutableResponseOrBuilder")


@_attrs_define
class AsyncExecutableResponseOrBuilder:
    """
    Attributes:
        callback_ids_count (int | Unset):
        units_list (list[str] | Unset):
        units_count (int | Unset):
        log_keys_count (int | Unset):
        log_keys_list (list[str] | Unset):
        should_remove_already_processed_notify_ids (bool | Unset):
        status (AsyncExecutableResponseOrBuilderStatus | Unset):
        timeout (int | Unset):
        status_value (int | Unset):
        callback_ids_list (list[str] | Unset):
        all_fields (AsyncExecutableResponseOrBuilderAllFields | Unset):
        default_instance_for_type (Message | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        initialized (bool | Unset):
    """

    callback_ids_count: int | Unset = UNSET
    units_list: list[str] | Unset = UNSET
    units_count: int | Unset = UNSET
    log_keys_count: int | Unset = UNSET
    log_keys_list: list[str] | Unset = UNSET
    should_remove_already_processed_notify_ids: bool | Unset = UNSET
    status: AsyncExecutableResponseOrBuilderStatus | Unset = UNSET
    timeout: int | Unset = UNSET
    status_value: int | Unset = UNSET
    callback_ids_list: list[str] | Unset = UNSET
    all_fields: AsyncExecutableResponseOrBuilderAllFields | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        callback_ids_count = self.callback_ids_count

        units_list: list[str] | Unset = UNSET
        if not isinstance(self.units_list, Unset):
            units_list = self.units_list

        units_count = self.units_count

        log_keys_count = self.log_keys_count

        log_keys_list: list[str] | Unset = UNSET
        if not isinstance(self.log_keys_list, Unset):
            log_keys_list = self.log_keys_list

        should_remove_already_processed_notify_ids = self.should_remove_already_processed_notify_ids

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        timeout = self.timeout

        status_value = self.status_value

        callback_ids_list: list[str] | Unset = UNSET
        if not isinstance(self.callback_ids_list, Unset):
            callback_ids_list = self.callback_ids_list

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
        if callback_ids_count is not UNSET:
            field_dict["callbackIdsCount"] = callback_ids_count
        if units_list is not UNSET:
            field_dict["unitsList"] = units_list
        if units_count is not UNSET:
            field_dict["unitsCount"] = units_count
        if log_keys_count is not UNSET:
            field_dict["logKeysCount"] = log_keys_count
        if log_keys_list is not UNSET:
            field_dict["logKeysList"] = log_keys_list
        if should_remove_already_processed_notify_ids is not UNSET:
            field_dict["shouldRemoveAlreadyProcessedNotifyIds"] = should_remove_already_processed_notify_ids
        if status is not UNSET:
            field_dict["status"] = status
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if status_value is not UNSET:
            field_dict["statusValue"] = status_value
        if callback_ids_list is not UNSET:
            field_dict["callbackIdsList"] = callback_ids_list
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
        from ..models.async_executable_response_or_builder_all_fields import AsyncExecutableResponseOrBuilderAllFields
        from ..models.descriptor import Descriptor
        from ..models.message import Message
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        callback_ids_count = d.pop("callbackIdsCount", UNSET)

        units_list = cast(list[str], d.pop("unitsList", UNSET))

        units_count = d.pop("unitsCount", UNSET)

        log_keys_count = d.pop("logKeysCount", UNSET)

        log_keys_list = cast(list[str], d.pop("logKeysList", UNSET))

        should_remove_already_processed_notify_ids = d.pop("shouldRemoveAlreadyProcessedNotifyIds", UNSET)

        _status = d.pop("status", UNSET)
        status: AsyncExecutableResponseOrBuilderStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_async_executable_response_or_builder_status(_status)

        timeout = d.pop("timeout", UNSET)

        status_value = d.pop("statusValue", UNSET)

        callback_ids_list = cast(list[str], d.pop("callbackIdsList", UNSET))

        _all_fields = d.pop("allFields", UNSET)
        all_fields: AsyncExecutableResponseOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = AsyncExecutableResponseOrBuilderAllFields.from_dict(_all_fields)

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

        async_executable_response_or_builder = cls(
            callback_ids_count=callback_ids_count,
            units_list=units_list,
            units_count=units_count,
            log_keys_count=log_keys_count,
            log_keys_list=log_keys_list,
            should_remove_already_processed_notify_ids=should_remove_already_processed_notify_ids,
            status=status,
            timeout=timeout,
            status_value=status_value,
            callback_ids_list=callback_ids_list,
            all_fields=all_fields,
            default_instance_for_type=default_instance_for_type,
            unknown_fields=unknown_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            initialized=initialized,
        )

        async_executable_response_or_builder.additional_properties = d
        return async_executable_response_or_builder

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
