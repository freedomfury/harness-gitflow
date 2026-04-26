from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.message import Message
    from ..models.retry_execution_info_or_builder_all_fields import RetryExecutionInfoOrBuilderAllFields
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="RetryExecutionInfoOrBuilder")


@_attrs_define
class RetryExecutionInfoOrBuilder:
    """
    Attributes:
        parent_retry_id_bytes (ByteString | Unset):
        root_execution_id_bytes (ByteString | Unset):
        root_execution_id (str | Unset):
        is_retry (bool | Unset):
        parent_retry_id (str | Unset):
        all_fields (RetryExecutionInfoOrBuilderAllFields | Unset):
        default_instance_for_type (Message | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        initialized (bool | Unset):
    """

    parent_retry_id_bytes: ByteString | Unset = UNSET
    root_execution_id_bytes: ByteString | Unset = UNSET
    root_execution_id: str | Unset = UNSET
    is_retry: bool | Unset = UNSET
    parent_retry_id: str | Unset = UNSET
    all_fields: RetryExecutionInfoOrBuilderAllFields | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        parent_retry_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parent_retry_id_bytes, Unset):
            parent_retry_id_bytes = self.parent_retry_id_bytes.to_dict()

        root_execution_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.root_execution_id_bytes, Unset):
            root_execution_id_bytes = self.root_execution_id_bytes.to_dict()

        root_execution_id = self.root_execution_id

        is_retry = self.is_retry

        parent_retry_id = self.parent_retry_id

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
        if parent_retry_id_bytes is not UNSET:
            field_dict["parentRetryIdBytes"] = parent_retry_id_bytes
        if root_execution_id_bytes is not UNSET:
            field_dict["rootExecutionIdBytes"] = root_execution_id_bytes
        if root_execution_id is not UNSET:
            field_dict["rootExecutionId"] = root_execution_id
        if is_retry is not UNSET:
            field_dict["isRetry"] = is_retry
        if parent_retry_id is not UNSET:
            field_dict["parentRetryId"] = parent_retry_id
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
        from ..models.retry_execution_info_or_builder_all_fields import RetryExecutionInfoOrBuilderAllFields
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _parent_retry_id_bytes = d.pop("parentRetryIdBytes", UNSET)
        parent_retry_id_bytes: ByteString | Unset
        if isinstance(_parent_retry_id_bytes, Unset):
            parent_retry_id_bytes = UNSET
        else:
            parent_retry_id_bytes = ByteString.from_dict(_parent_retry_id_bytes)

        _root_execution_id_bytes = d.pop("rootExecutionIdBytes", UNSET)
        root_execution_id_bytes: ByteString | Unset
        if isinstance(_root_execution_id_bytes, Unset):
            root_execution_id_bytes = UNSET
        else:
            root_execution_id_bytes = ByteString.from_dict(_root_execution_id_bytes)

        root_execution_id = d.pop("rootExecutionId", UNSET)

        is_retry = d.pop("isRetry", UNSET)

        parent_retry_id = d.pop("parentRetryId", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: RetryExecutionInfoOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = RetryExecutionInfoOrBuilderAllFields.from_dict(_all_fields)

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

        retry_execution_info_or_builder = cls(
            parent_retry_id_bytes=parent_retry_id_bytes,
            root_execution_id_bytes=root_execution_id_bytes,
            root_execution_id=root_execution_id,
            is_retry=is_retry,
            parent_retry_id=parent_retry_id,
            all_fields=all_fields,
            default_instance_for_type=default_instance_for_type,
            unknown_fields=unknown_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            initialized=initialized,
        )

        retry_execution_info_or_builder.additional_properties = d
        return retry_execution_info_or_builder

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
