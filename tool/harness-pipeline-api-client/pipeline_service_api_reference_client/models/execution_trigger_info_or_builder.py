from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_trigger_info_or_builder_trigger_type import (
    ExecutionTriggerInfoOrBuilderTriggerType,
    check_execution_trigger_info_or_builder_trigger_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.build_info import BuildInfo
    from ..models.build_info_or_builder import BuildInfoOrBuilder
    from ..models.descriptor import Descriptor
    from ..models.execution_trigger_info_or_builder_all_fields import ExecutionTriggerInfoOrBuilderAllFields
    from ..models.message import Message
    from ..models.rerun_info import RerunInfo
    from ..models.rerun_info_or_builder import RerunInfoOrBuilder
    from ..models.triggered_by import TriggeredBy
    from ..models.triggered_by_or_builder import TriggeredByOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="ExecutionTriggerInfoOrBuilder")


@_attrs_define
class ExecutionTriggerInfoOrBuilder:
    """
    Attributes:
        trigger_type (ExecutionTriggerInfoOrBuilderTriggerType | Unset):
        triggered_by (TriggeredBy | Unset):
        triggered_by_or_builder (TriggeredByOrBuilder | Unset):
        is_rerun (bool | Unset):
        rerun_info (RerunInfo | Unset):
        rerun_info_or_builder (RerunInfoOrBuilder | Unset):
        build_info (BuildInfo | Unset):
        build_info_or_builder (BuildInfoOrBuilder | Unset):
        trigger_type_value (int | Unset):
        all_fields (ExecutionTriggerInfoOrBuilderAllFields | Unset):
        default_instance_for_type (Message | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        initialized (bool | Unset):
    """

    trigger_type: ExecutionTriggerInfoOrBuilderTriggerType | Unset = UNSET
    triggered_by: TriggeredBy | Unset = UNSET
    triggered_by_or_builder: TriggeredByOrBuilder | Unset = UNSET
    is_rerun: bool | Unset = UNSET
    rerun_info: RerunInfo | Unset = UNSET
    rerun_info_or_builder: RerunInfoOrBuilder | Unset = UNSET
    build_info: BuildInfo | Unset = UNSET
    build_info_or_builder: BuildInfoOrBuilder | Unset = UNSET
    trigger_type_value: int | Unset = UNSET
    all_fields: ExecutionTriggerInfoOrBuilderAllFields | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trigger_type: str | Unset = UNSET
        if not isinstance(self.trigger_type, Unset):
            trigger_type = self.trigger_type

        triggered_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.triggered_by, Unset):
            triggered_by = self.triggered_by.to_dict()

        triggered_by_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.triggered_by_or_builder, Unset):
            triggered_by_or_builder = self.triggered_by_or_builder.to_dict()

        is_rerun = self.is_rerun

        rerun_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rerun_info, Unset):
            rerun_info = self.rerun_info.to_dict()

        rerun_info_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rerun_info_or_builder, Unset):
            rerun_info_or_builder = self.rerun_info_or_builder.to_dict()

        build_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.build_info, Unset):
            build_info = self.build_info.to_dict()

        build_info_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.build_info_or_builder, Unset):
            build_info_or_builder = self.build_info_or_builder.to_dict()

        trigger_type_value = self.trigger_type_value

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
        if trigger_type is not UNSET:
            field_dict["triggerType"] = trigger_type
        if triggered_by is not UNSET:
            field_dict["triggeredBy"] = triggered_by
        if triggered_by_or_builder is not UNSET:
            field_dict["triggeredByOrBuilder"] = triggered_by_or_builder
        if is_rerun is not UNSET:
            field_dict["isRerun"] = is_rerun
        if rerun_info is not UNSET:
            field_dict["rerunInfo"] = rerun_info
        if rerun_info_or_builder is not UNSET:
            field_dict["rerunInfoOrBuilder"] = rerun_info_or_builder
        if build_info is not UNSET:
            field_dict["buildInfo"] = build_info
        if build_info_or_builder is not UNSET:
            field_dict["buildInfoOrBuilder"] = build_info_or_builder
        if trigger_type_value is not UNSET:
            field_dict["triggerTypeValue"] = trigger_type_value
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
        from ..models.build_info import BuildInfo
        from ..models.build_info_or_builder import BuildInfoOrBuilder
        from ..models.descriptor import Descriptor
        from ..models.execution_trigger_info_or_builder_all_fields import ExecutionTriggerInfoOrBuilderAllFields
        from ..models.message import Message
        from ..models.rerun_info import RerunInfo
        from ..models.rerun_info_or_builder import RerunInfoOrBuilder
        from ..models.triggered_by import TriggeredBy
        from ..models.triggered_by_or_builder import TriggeredByOrBuilder
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _trigger_type = d.pop("triggerType", UNSET)
        trigger_type: ExecutionTriggerInfoOrBuilderTriggerType | Unset
        if isinstance(_trigger_type, Unset):
            trigger_type = UNSET
        else:
            trigger_type = check_execution_trigger_info_or_builder_trigger_type(_trigger_type)

        _triggered_by = d.pop("triggeredBy", UNSET)
        triggered_by: TriggeredBy | Unset
        if isinstance(_triggered_by, Unset):
            triggered_by = UNSET
        else:
            triggered_by = TriggeredBy.from_dict(_triggered_by)

        _triggered_by_or_builder = d.pop("triggeredByOrBuilder", UNSET)
        triggered_by_or_builder: TriggeredByOrBuilder | Unset
        if isinstance(_triggered_by_or_builder, Unset):
            triggered_by_or_builder = UNSET
        else:
            triggered_by_or_builder = TriggeredByOrBuilder.from_dict(_triggered_by_or_builder)

        is_rerun = d.pop("isRerun", UNSET)

        _rerun_info = d.pop("rerunInfo", UNSET)
        rerun_info: RerunInfo | Unset
        if isinstance(_rerun_info, Unset):
            rerun_info = UNSET
        else:
            rerun_info = RerunInfo.from_dict(_rerun_info)

        _rerun_info_or_builder = d.pop("rerunInfoOrBuilder", UNSET)
        rerun_info_or_builder: RerunInfoOrBuilder | Unset
        if isinstance(_rerun_info_or_builder, Unset):
            rerun_info_or_builder = UNSET
        else:
            rerun_info_or_builder = RerunInfoOrBuilder.from_dict(_rerun_info_or_builder)

        _build_info = d.pop("buildInfo", UNSET)
        build_info: BuildInfo | Unset
        if isinstance(_build_info, Unset):
            build_info = UNSET
        else:
            build_info = BuildInfo.from_dict(_build_info)

        _build_info_or_builder = d.pop("buildInfoOrBuilder", UNSET)
        build_info_or_builder: BuildInfoOrBuilder | Unset
        if isinstance(_build_info_or_builder, Unset):
            build_info_or_builder = UNSET
        else:
            build_info_or_builder = BuildInfoOrBuilder.from_dict(_build_info_or_builder)

        trigger_type_value = d.pop("triggerTypeValue", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: ExecutionTriggerInfoOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = ExecutionTriggerInfoOrBuilderAllFields.from_dict(_all_fields)

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

        execution_trigger_info_or_builder = cls(
            trigger_type=trigger_type,
            triggered_by=triggered_by,
            triggered_by_or_builder=triggered_by_or_builder,
            is_rerun=is_rerun,
            rerun_info=rerun_info,
            rerun_info_or_builder=rerun_info_or_builder,
            build_info=build_info,
            build_info_or_builder=build_info_or_builder,
            trigger_type_value=trigger_type_value,
            all_fields=all_fields,
            default_instance_for_type=default_instance_for_type,
            unknown_fields=unknown_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            initialized=initialized,
        )

        execution_trigger_info_or_builder.additional_properties = d
        return execution_trigger_info_or_builder

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
