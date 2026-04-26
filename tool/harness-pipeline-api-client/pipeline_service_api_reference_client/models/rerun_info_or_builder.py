from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rerun_info_or_builder_prev_trigger_type import (
    RerunInfoOrBuilderPrevTriggerType,
    check_rerun_info_or_builder_prev_trigger_type,
)
from ..models.rerun_info_or_builder_root_trigger_type import (
    RerunInfoOrBuilderRootTriggerType,
    check_rerun_info_or_builder_root_trigger_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.message import Message
    from ..models.rerun_info_or_builder_all_fields import RerunInfoOrBuilderAllFields
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="RerunInfoOrBuilder")


@_attrs_define
class RerunInfoOrBuilder:
    """
    Attributes:
        root_trigger_type (RerunInfoOrBuilderRootTriggerType | Unset):
        root_execution_id_bytes (ByteString | Unset):
        root_trigger_type_value (int | Unset):
        prev_execution_id_bytes (ByteString | Unset):
        prev_trigger_type_value (int | Unset):
        prev_trigger_type (RerunInfoOrBuilderPrevTriggerType | Unset):
        root_execution_id (str | Unset):
        prev_execution_id (str | Unset):
        all_fields (RerunInfoOrBuilderAllFields | Unset):
        default_instance_for_type (Message | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        initialized (bool | Unset):
    """

    root_trigger_type: RerunInfoOrBuilderRootTriggerType | Unset = UNSET
    root_execution_id_bytes: ByteString | Unset = UNSET
    root_trigger_type_value: int | Unset = UNSET
    prev_execution_id_bytes: ByteString | Unset = UNSET
    prev_trigger_type_value: int | Unset = UNSET
    prev_trigger_type: RerunInfoOrBuilderPrevTriggerType | Unset = UNSET
    root_execution_id: str | Unset = UNSET
    prev_execution_id: str | Unset = UNSET
    all_fields: RerunInfoOrBuilderAllFields | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        root_trigger_type: str | Unset = UNSET
        if not isinstance(self.root_trigger_type, Unset):
            root_trigger_type = self.root_trigger_type

        root_execution_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.root_execution_id_bytes, Unset):
            root_execution_id_bytes = self.root_execution_id_bytes.to_dict()

        root_trigger_type_value = self.root_trigger_type_value

        prev_execution_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.prev_execution_id_bytes, Unset):
            prev_execution_id_bytes = self.prev_execution_id_bytes.to_dict()

        prev_trigger_type_value = self.prev_trigger_type_value

        prev_trigger_type: str | Unset = UNSET
        if not isinstance(self.prev_trigger_type, Unset):
            prev_trigger_type = self.prev_trigger_type

        root_execution_id = self.root_execution_id

        prev_execution_id = self.prev_execution_id

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
        if root_trigger_type is not UNSET:
            field_dict["rootTriggerType"] = root_trigger_type
        if root_execution_id_bytes is not UNSET:
            field_dict["rootExecutionIdBytes"] = root_execution_id_bytes
        if root_trigger_type_value is not UNSET:
            field_dict["rootTriggerTypeValue"] = root_trigger_type_value
        if prev_execution_id_bytes is not UNSET:
            field_dict["prevExecutionIdBytes"] = prev_execution_id_bytes
        if prev_trigger_type_value is not UNSET:
            field_dict["prevTriggerTypeValue"] = prev_trigger_type_value
        if prev_trigger_type is not UNSET:
            field_dict["prevTriggerType"] = prev_trigger_type
        if root_execution_id is not UNSET:
            field_dict["rootExecutionId"] = root_execution_id
        if prev_execution_id is not UNSET:
            field_dict["prevExecutionId"] = prev_execution_id
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
        from ..models.rerun_info_or_builder_all_fields import RerunInfoOrBuilderAllFields
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _root_trigger_type = d.pop("rootTriggerType", UNSET)
        root_trigger_type: RerunInfoOrBuilderRootTriggerType | Unset
        if isinstance(_root_trigger_type, Unset):
            root_trigger_type = UNSET
        else:
            root_trigger_type = check_rerun_info_or_builder_root_trigger_type(_root_trigger_type)

        _root_execution_id_bytes = d.pop("rootExecutionIdBytes", UNSET)
        root_execution_id_bytes: ByteString | Unset
        if isinstance(_root_execution_id_bytes, Unset):
            root_execution_id_bytes = UNSET
        else:
            root_execution_id_bytes = ByteString.from_dict(_root_execution_id_bytes)

        root_trigger_type_value = d.pop("rootTriggerTypeValue", UNSET)

        _prev_execution_id_bytes = d.pop("prevExecutionIdBytes", UNSET)
        prev_execution_id_bytes: ByteString | Unset
        if isinstance(_prev_execution_id_bytes, Unset):
            prev_execution_id_bytes = UNSET
        else:
            prev_execution_id_bytes = ByteString.from_dict(_prev_execution_id_bytes)

        prev_trigger_type_value = d.pop("prevTriggerTypeValue", UNSET)

        _prev_trigger_type = d.pop("prevTriggerType", UNSET)
        prev_trigger_type: RerunInfoOrBuilderPrevTriggerType | Unset
        if isinstance(_prev_trigger_type, Unset):
            prev_trigger_type = UNSET
        else:
            prev_trigger_type = check_rerun_info_or_builder_prev_trigger_type(_prev_trigger_type)

        root_execution_id = d.pop("rootExecutionId", UNSET)

        prev_execution_id = d.pop("prevExecutionId", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: RerunInfoOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = RerunInfoOrBuilderAllFields.from_dict(_all_fields)

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

        rerun_info_or_builder = cls(
            root_trigger_type=root_trigger_type,
            root_execution_id_bytes=root_execution_id_bytes,
            root_trigger_type_value=root_trigger_type_value,
            prev_execution_id_bytes=prev_execution_id_bytes,
            prev_trigger_type_value=prev_trigger_type_value,
            prev_trigger_type=prev_trigger_type,
            root_execution_id=root_execution_id,
            prev_execution_id=prev_execution_id,
            all_fields=all_fields,
            default_instance_for_type=default_instance_for_type,
            unknown_fields=unknown_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            initialized=initialized,
        )

        rerun_info_or_builder.additional_properties = d
        return rerun_info_or_builder

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
