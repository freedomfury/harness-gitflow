from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.ambiance_all_fields import AmbianceAllFields
    from ..models.ambiance_setup_abstractions import AmbianceSetupAbstractions
    from ..models.ambiance_setup_abstractions_map import AmbianceSetupAbstractionsMap
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.execution_metadata import ExecutionMetadata
    from ..models.execution_metadata_or_builder import ExecutionMetadataOrBuilder
    from ..models.level import Level
    from ..models.level_or_builder import LevelOrBuilder
    from ..models.parser_ambiance import ParserAmbiance
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="Ambiance")


@_attrs_define
class Ambiance:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        levels_count (int | Unset):
        original_stage_execution_id_for_rollback_mode (str | Unset):
        plan_execution_id_bytes (ByteString | Unset):
        setup_abstractions_count (int | Unset):
        levels_or_builder_list (list[LevelOrBuilder] | Unset):
        metadata_or_builder (ExecutionMetadataOrBuilder | Unset):
        plan_id_bytes (ByteString | Unset):
        stage_execution_id_bytes (ByteString | Unset):
        original_stage_execution_id_for_rollback_mode_bytes (ByteString | Unset):
        metadata (ExecutionMetadata | Unset):
        initialized (bool | Unset):
        plan_execution_id (str | Unset):
        default_instance_for_type (Ambiance | Unset):
        parser_for_type (ParserAmbiance | Unset):
        serialized_size (int | Unset):
        start_ts (int | Unset):
        setup_abstractions (AmbianceSetupAbstractions | Unset):
        setup_abstractions_map (AmbianceSetupAbstractionsMap | Unset):
        plan_id (str | Unset):
        levels_list (list[Level] | Unset):
        stage_execution_id (str | Unset):
        expression_functor_token (int | Unset):
        all_fields (AmbianceAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    levels_count: int | Unset = UNSET
    original_stage_execution_id_for_rollback_mode: str | Unset = UNSET
    plan_execution_id_bytes: ByteString | Unset = UNSET
    setup_abstractions_count: int | Unset = UNSET
    levels_or_builder_list: list[LevelOrBuilder] | Unset = UNSET
    metadata_or_builder: ExecutionMetadataOrBuilder | Unset = UNSET
    plan_id_bytes: ByteString | Unset = UNSET
    stage_execution_id_bytes: ByteString | Unset = UNSET
    original_stage_execution_id_for_rollback_mode_bytes: ByteString | Unset = UNSET
    metadata: ExecutionMetadata | Unset = UNSET
    initialized: bool | Unset = UNSET
    plan_execution_id: str | Unset = UNSET
    default_instance_for_type: Ambiance | Unset = UNSET
    parser_for_type: ParserAmbiance | Unset = UNSET
    serialized_size: int | Unset = UNSET
    start_ts: int | Unset = UNSET
    setup_abstractions: AmbianceSetupAbstractions | Unset = UNSET
    setup_abstractions_map: AmbianceSetupAbstractionsMap | Unset = UNSET
    plan_id: str | Unset = UNSET
    levels_list: list[Level] | Unset = UNSET
    stage_execution_id: str | Unset = UNSET
    expression_functor_token: int | Unset = UNSET
    all_fields: AmbianceAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        levels_count = self.levels_count

        original_stage_execution_id_for_rollback_mode = self.original_stage_execution_id_for_rollback_mode

        plan_execution_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plan_execution_id_bytes, Unset):
            plan_execution_id_bytes = self.plan_execution_id_bytes.to_dict()

        setup_abstractions_count = self.setup_abstractions_count

        levels_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.levels_or_builder_list, Unset):
            levels_or_builder_list = []
            for levels_or_builder_list_item_data in self.levels_or_builder_list:
                levels_or_builder_list_item = levels_or_builder_list_item_data.to_dict()
                levels_or_builder_list.append(levels_or_builder_list_item)

        metadata_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata_or_builder, Unset):
            metadata_or_builder = self.metadata_or_builder.to_dict()

        plan_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.plan_id_bytes, Unset):
            plan_id_bytes = self.plan_id_bytes.to_dict()

        stage_execution_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stage_execution_id_bytes, Unset):
            stage_execution_id_bytes = self.stage_execution_id_bytes.to_dict()

        original_stage_execution_id_for_rollback_mode_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.original_stage_execution_id_for_rollback_mode_bytes, Unset):
            original_stage_execution_id_for_rollback_mode_bytes = (
                self.original_stage_execution_id_for_rollback_mode_bytes.to_dict()
            )

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        initialized = self.initialized

        plan_execution_id = self.plan_execution_id

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        start_ts = self.start_ts

        setup_abstractions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.setup_abstractions, Unset):
            setup_abstractions = self.setup_abstractions.to_dict()

        setup_abstractions_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.setup_abstractions_map, Unset):
            setup_abstractions_map = self.setup_abstractions_map.to_dict()

        plan_id = self.plan_id

        levels_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.levels_list, Unset):
            levels_list = []
            for levels_list_item_data in self.levels_list:
                levels_list_item = levels_list_item_data.to_dict()
                levels_list.append(levels_list_item)

        stage_execution_id = self.stage_execution_id

        expression_functor_token = self.expression_functor_token

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
        if levels_count is not UNSET:
            field_dict["levelsCount"] = levels_count
        if original_stage_execution_id_for_rollback_mode is not UNSET:
            field_dict["originalStageExecutionIdForRollbackMode"] = original_stage_execution_id_for_rollback_mode
        if plan_execution_id_bytes is not UNSET:
            field_dict["planExecutionIdBytes"] = plan_execution_id_bytes
        if setup_abstractions_count is not UNSET:
            field_dict["setupAbstractionsCount"] = setup_abstractions_count
        if levels_or_builder_list is not UNSET:
            field_dict["levelsOrBuilderList"] = levels_or_builder_list
        if metadata_or_builder is not UNSET:
            field_dict["metadataOrBuilder"] = metadata_or_builder
        if plan_id_bytes is not UNSET:
            field_dict["planIdBytes"] = plan_id_bytes
        if stage_execution_id_bytes is not UNSET:
            field_dict["stageExecutionIdBytes"] = stage_execution_id_bytes
        if original_stage_execution_id_for_rollback_mode_bytes is not UNSET:
            field_dict["originalStageExecutionIdForRollbackModeBytes"] = (
                original_stage_execution_id_for_rollback_mode_bytes
            )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if plan_execution_id is not UNSET:
            field_dict["planExecutionId"] = plan_execution_id
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if start_ts is not UNSET:
            field_dict["startTs"] = start_ts
        if setup_abstractions is not UNSET:
            field_dict["setupAbstractions"] = setup_abstractions
        if setup_abstractions_map is not UNSET:
            field_dict["setupAbstractionsMap"] = setup_abstractions_map
        if plan_id is not UNSET:
            field_dict["planId"] = plan_id
        if levels_list is not UNSET:
            field_dict["levelsList"] = levels_list
        if stage_execution_id is not UNSET:
            field_dict["stageExecutionId"] = stage_execution_id
        if expression_functor_token is not UNSET:
            field_dict["expressionFunctorToken"] = expression_functor_token
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
        from ..models.ambiance_all_fields import AmbianceAllFields
        from ..models.ambiance_setup_abstractions import AmbianceSetupAbstractions
        from ..models.ambiance_setup_abstractions_map import AmbianceSetupAbstractionsMap
        from ..models.byte_string import ByteString
        from ..models.descriptor import Descriptor
        from ..models.execution_metadata import ExecutionMetadata
        from ..models.execution_metadata_or_builder import ExecutionMetadataOrBuilder
        from ..models.level import Level
        from ..models.level_or_builder import LevelOrBuilder
        from ..models.parser_ambiance import ParserAmbiance
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        levels_count = d.pop("levelsCount", UNSET)

        original_stage_execution_id_for_rollback_mode = d.pop("originalStageExecutionIdForRollbackMode", UNSET)

        _plan_execution_id_bytes = d.pop("planExecutionIdBytes", UNSET)
        plan_execution_id_bytes: ByteString | Unset
        if isinstance(_plan_execution_id_bytes, Unset):
            plan_execution_id_bytes = UNSET
        else:
            plan_execution_id_bytes = ByteString.from_dict(_plan_execution_id_bytes)

        setup_abstractions_count = d.pop("setupAbstractionsCount", UNSET)

        _levels_or_builder_list = d.pop("levelsOrBuilderList", UNSET)
        levels_or_builder_list: list[LevelOrBuilder] | Unset = UNSET
        if _levels_or_builder_list is not UNSET:
            levels_or_builder_list = []
            for levels_or_builder_list_item_data in _levels_or_builder_list:
                levels_or_builder_list_item = LevelOrBuilder.from_dict(levels_or_builder_list_item_data)

                levels_or_builder_list.append(levels_or_builder_list_item)

        _metadata_or_builder = d.pop("metadataOrBuilder", UNSET)
        metadata_or_builder: ExecutionMetadataOrBuilder | Unset
        if isinstance(_metadata_or_builder, Unset):
            metadata_or_builder = UNSET
        else:
            metadata_or_builder = ExecutionMetadataOrBuilder.from_dict(_metadata_or_builder)

        _plan_id_bytes = d.pop("planIdBytes", UNSET)
        plan_id_bytes: ByteString | Unset
        if isinstance(_plan_id_bytes, Unset):
            plan_id_bytes = UNSET
        else:
            plan_id_bytes = ByteString.from_dict(_plan_id_bytes)

        _stage_execution_id_bytes = d.pop("stageExecutionIdBytes", UNSET)
        stage_execution_id_bytes: ByteString | Unset
        if isinstance(_stage_execution_id_bytes, Unset):
            stage_execution_id_bytes = UNSET
        else:
            stage_execution_id_bytes = ByteString.from_dict(_stage_execution_id_bytes)

        _original_stage_execution_id_for_rollback_mode_bytes = d.pop(
            "originalStageExecutionIdForRollbackModeBytes", UNSET
        )
        original_stage_execution_id_for_rollback_mode_bytes: ByteString | Unset
        if isinstance(_original_stage_execution_id_for_rollback_mode_bytes, Unset):
            original_stage_execution_id_for_rollback_mode_bytes = UNSET
        else:
            original_stage_execution_id_for_rollback_mode_bytes = ByteString.from_dict(
                _original_stage_execution_id_for_rollback_mode_bytes
            )

        _metadata = d.pop("metadata", UNSET)
        metadata: ExecutionMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ExecutionMetadata.from_dict(_metadata)

        initialized = d.pop("initialized", UNSET)

        plan_execution_id = d.pop("planExecutionId", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: Ambiance | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = Ambiance.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserAmbiance | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserAmbiance.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        start_ts = d.pop("startTs", UNSET)

        _setup_abstractions = d.pop("setupAbstractions", UNSET)
        setup_abstractions: AmbianceSetupAbstractions | Unset
        if isinstance(_setup_abstractions, Unset):
            setup_abstractions = UNSET
        else:
            setup_abstractions = AmbianceSetupAbstractions.from_dict(_setup_abstractions)

        _setup_abstractions_map = d.pop("setupAbstractionsMap", UNSET)
        setup_abstractions_map: AmbianceSetupAbstractionsMap | Unset
        if isinstance(_setup_abstractions_map, Unset):
            setup_abstractions_map = UNSET
        else:
            setup_abstractions_map = AmbianceSetupAbstractionsMap.from_dict(_setup_abstractions_map)

        plan_id = d.pop("planId", UNSET)

        _levels_list = d.pop("levelsList", UNSET)
        levels_list: list[Level] | Unset = UNSET
        if _levels_list is not UNSET:
            levels_list = []
            for levels_list_item_data in _levels_list:
                levels_list_item = Level.from_dict(levels_list_item_data)

                levels_list.append(levels_list_item)

        stage_execution_id = d.pop("stageExecutionId", UNSET)

        expression_functor_token = d.pop("expressionFunctorToken", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: AmbianceAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = AmbianceAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        ambiance = cls(
            unknown_fields=unknown_fields,
            levels_count=levels_count,
            original_stage_execution_id_for_rollback_mode=original_stage_execution_id_for_rollback_mode,
            plan_execution_id_bytes=plan_execution_id_bytes,
            setup_abstractions_count=setup_abstractions_count,
            levels_or_builder_list=levels_or_builder_list,
            metadata_or_builder=metadata_or_builder,
            plan_id_bytes=plan_id_bytes,
            stage_execution_id_bytes=stage_execution_id_bytes,
            original_stage_execution_id_for_rollback_mode_bytes=original_stage_execution_id_for_rollback_mode_bytes,
            metadata=metadata,
            initialized=initialized,
            plan_execution_id=plan_execution_id,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            start_ts=start_ts,
            setup_abstractions=setup_abstractions,
            setup_abstractions_map=setup_abstractions_map,
            plan_id=plan_id,
            levels_list=levels_list,
            stage_execution_id=stage_execution_id,
            expression_functor_token=expression_functor_token,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        ambiance.additional_properties = d
        return ambiance

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
