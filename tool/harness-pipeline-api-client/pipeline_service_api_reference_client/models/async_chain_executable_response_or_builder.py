from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.async_chain_executable_response_or_builder_status import (
    AsyncChainExecutableResponseOrBuilderStatus,
    check_async_chain_executable_response_or_builder_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.async_chain_executable_response_or_builder_all_fields import (
        AsyncChainExecutableResponseOrBuilderAllFields,
    )
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.message import Message
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="AsyncChainExecutableResponseOrBuilder")


@_attrs_define
class AsyncChainExecutableResponseOrBuilder:
    """
    Attributes:
        callback_ids_count (int | Unset):
        chain_end (bool | Unset):
        pass_through_data (ByteString | Unset):
        units_list (list[str] | Unset):
        units_count (int | Unset):
        callback_id_bytes (ByteString | Unset):
        log_keys_count (int | Unset):
        log_keys_list (list[str] | Unset):
        status (AsyncChainExecutableResponseOrBuilderStatus | Unset):
        timeout (int | Unset):
        status_value (int | Unset):
        callback_ids_list (list[str] | Unset):
        callback_id (str | Unset):
        all_fields (AsyncChainExecutableResponseOrBuilderAllFields | Unset):
        default_instance_for_type (Message | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        initialized (bool | Unset):
    """

    callback_ids_count: int | Unset = UNSET
    chain_end: bool | Unset = UNSET
    pass_through_data: ByteString | Unset = UNSET
    units_list: list[str] | Unset = UNSET
    units_count: int | Unset = UNSET
    callback_id_bytes: ByteString | Unset = UNSET
    log_keys_count: int | Unset = UNSET
    log_keys_list: list[str] | Unset = UNSET
    status: AsyncChainExecutableResponseOrBuilderStatus | Unset = UNSET
    timeout: int | Unset = UNSET
    status_value: int | Unset = UNSET
    callback_ids_list: list[str] | Unset = UNSET
    callback_id: str | Unset = UNSET
    all_fields: AsyncChainExecutableResponseOrBuilderAllFields | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        callback_ids_count = self.callback_ids_count

        chain_end = self.chain_end

        pass_through_data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pass_through_data, Unset):
            pass_through_data = self.pass_through_data.to_dict()

        units_list: list[str] | Unset = UNSET
        if not isinstance(self.units_list, Unset):
            units_list = self.units_list

        units_count = self.units_count

        callback_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.callback_id_bytes, Unset):
            callback_id_bytes = self.callback_id_bytes.to_dict()

        log_keys_count = self.log_keys_count

        log_keys_list: list[str] | Unset = UNSET
        if not isinstance(self.log_keys_list, Unset):
            log_keys_list = self.log_keys_list

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        timeout = self.timeout

        status_value = self.status_value

        callback_ids_list: list[str] | Unset = UNSET
        if not isinstance(self.callback_ids_list, Unset):
            callback_ids_list = self.callback_ids_list

        callback_id = self.callback_id

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
        if chain_end is not UNSET:
            field_dict["chainEnd"] = chain_end
        if pass_through_data is not UNSET:
            field_dict["passThroughData"] = pass_through_data
        if units_list is not UNSET:
            field_dict["unitsList"] = units_list
        if units_count is not UNSET:
            field_dict["unitsCount"] = units_count
        if callback_id_bytes is not UNSET:
            field_dict["callbackIdBytes"] = callback_id_bytes
        if log_keys_count is not UNSET:
            field_dict["logKeysCount"] = log_keys_count
        if log_keys_list is not UNSET:
            field_dict["logKeysList"] = log_keys_list
        if status is not UNSET:
            field_dict["status"] = status
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if status_value is not UNSET:
            field_dict["statusValue"] = status_value
        if callback_ids_list is not UNSET:
            field_dict["callbackIdsList"] = callback_ids_list
        if callback_id is not UNSET:
            field_dict["callbackId"] = callback_id
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
        from ..models.async_chain_executable_response_or_builder_all_fields import (
            AsyncChainExecutableResponseOrBuilderAllFields,
        )
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.message import Message
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        callback_ids_count = d.pop("callbackIdsCount", UNSET)

        chain_end = d.pop("chainEnd", UNSET)

        _pass_through_data = d.pop("passThroughData", UNSET)
        pass_through_data: ByteString | Unset
        if isinstance(_pass_through_data, Unset):
            pass_through_data = UNSET
        else:
            pass_through_data = ByteString.from_dict(_pass_through_data)

        units_list = cast(list[str], d.pop("unitsList", UNSET))

        units_count = d.pop("unitsCount", UNSET)

        _callback_id_bytes = d.pop("callbackIdBytes", UNSET)
        callback_id_bytes: ByteString | Unset
        if isinstance(_callback_id_bytes, Unset):
            callback_id_bytes = UNSET
        else:
            callback_id_bytes = ByteString.from_dict(_callback_id_bytes)

        log_keys_count = d.pop("logKeysCount", UNSET)

        log_keys_list = cast(list[str], d.pop("logKeysList", UNSET))

        _status = d.pop("status", UNSET)
        status: AsyncChainExecutableResponseOrBuilderStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_async_chain_executable_response_or_builder_status(_status)

        timeout = d.pop("timeout", UNSET)

        status_value = d.pop("statusValue", UNSET)

        callback_ids_list = cast(list[str], d.pop("callbackIdsList", UNSET))

        callback_id = d.pop("callbackId", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: AsyncChainExecutableResponseOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = AsyncChainExecutableResponseOrBuilderAllFields.from_dict(_all_fields)

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

        async_chain_executable_response_or_builder = cls(
            callback_ids_count=callback_ids_count,
            chain_end=chain_end,
            pass_through_data=pass_through_data,
            units_list=units_list,
            units_count=units_count,
            callback_id_bytes=callback_id_bytes,
            log_keys_count=log_keys_count,
            log_keys_list=log_keys_list,
            status=status,
            timeout=timeout,
            status_value=status_value,
            callback_ids_list=callback_ids_list,
            callback_id=callback_id,
            all_fields=all_fields,
            default_instance_for_type=default_instance_for_type,
            unknown_fields=unknown_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            initialized=initialized,
        )

        async_chain_executable_response_or_builder.additional_properties = d
        return async_chain_executable_response_or_builder

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
