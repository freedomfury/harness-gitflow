from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.parser_pipeline_stage_info import ParserPipelineStageInfo
    from ..models.pipeline_stage_info_all_fields import PipelineStageInfoAllFields
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="PipelineStageInfo")


@_attrs_define
class PipelineStageInfo:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        execution_id_bytes (ByteString | Unset):
        pipeline_name_bytes (ByteString | Unset):
        stage_node_id_bytes (ByteString | Unset):
        initialized (bool | Unset):
        identifier (str | Unset):
        default_instance_for_type (PipelineStageInfo | Unset):
        parser_for_type (ParserPipelineStageInfo | Unset):
        serialized_size (int | Unset):
        identifier_bytes (ByteString | Unset):
        run_sequence (int | Unset):
        org_id (str | Unset):
        org_id_bytes (ByteString | Unset):
        project_id (str | Unset):
        project_id_bytes (ByteString | Unset):
        pipeline_name (str | Unset):
        has_parent_pipeline (bool | Unset):
        stage_node_id (str | Unset):
        execution_id (str | Unset):
        all_fields (PipelineStageInfoAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    execution_id_bytes: ByteString | Unset = UNSET
    pipeline_name_bytes: ByteString | Unset = UNSET
    stage_node_id_bytes: ByteString | Unset = UNSET
    initialized: bool | Unset = UNSET
    identifier: str | Unset = UNSET
    default_instance_for_type: PipelineStageInfo | Unset = UNSET
    parser_for_type: ParserPipelineStageInfo | Unset = UNSET
    serialized_size: int | Unset = UNSET
    identifier_bytes: ByteString | Unset = UNSET
    run_sequence: int | Unset = UNSET
    org_id: str | Unset = UNSET
    org_id_bytes: ByteString | Unset = UNSET
    project_id: str | Unset = UNSET
    project_id_bytes: ByteString | Unset = UNSET
    pipeline_name: str | Unset = UNSET
    has_parent_pipeline: bool | Unset = UNSET
    stage_node_id: str | Unset = UNSET
    execution_id: str | Unset = UNSET
    all_fields: PipelineStageInfoAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        execution_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution_id_bytes, Unset):
            execution_id_bytes = self.execution_id_bytes.to_dict()

        pipeline_name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pipeline_name_bytes, Unset):
            pipeline_name_bytes = self.pipeline_name_bytes.to_dict()

        stage_node_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stage_node_id_bytes, Unset):
            stage_node_id_bytes = self.stage_node_id_bytes.to_dict()

        initialized = self.initialized

        identifier = self.identifier

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        identifier_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier_bytes, Unset):
            identifier_bytes = self.identifier_bytes.to_dict()

        run_sequence = self.run_sequence

        org_id = self.org_id

        org_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.org_id_bytes, Unset):
            org_id_bytes = self.org_id_bytes.to_dict()

        project_id = self.project_id

        project_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_id_bytes, Unset):
            project_id_bytes = self.project_id_bytes.to_dict()

        pipeline_name = self.pipeline_name

        has_parent_pipeline = self.has_parent_pipeline

        stage_node_id = self.stage_node_id

        execution_id = self.execution_id

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
        if execution_id_bytes is not UNSET:
            field_dict["executionIdBytes"] = execution_id_bytes
        if pipeline_name_bytes is not UNSET:
            field_dict["pipelineNameBytes"] = pipeline_name_bytes
        if stage_node_id_bytes is not UNSET:
            field_dict["stageNodeIdBytes"] = stage_node_id_bytes
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if identifier_bytes is not UNSET:
            field_dict["identifierBytes"] = identifier_bytes
        if run_sequence is not UNSET:
            field_dict["runSequence"] = run_sequence
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if org_id_bytes is not UNSET:
            field_dict["orgIdBytes"] = org_id_bytes
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if project_id_bytes is not UNSET:
            field_dict["projectIdBytes"] = project_id_bytes
        if pipeline_name is not UNSET:
            field_dict["pipelineName"] = pipeline_name
        if has_parent_pipeline is not UNSET:
            field_dict["hasParentPipeline"] = has_parent_pipeline
        if stage_node_id is not UNSET:
            field_dict["stageNodeId"] = stage_node_id
        if execution_id is not UNSET:
            field_dict["executionId"] = execution_id
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
        from ..models.parser_pipeline_stage_info import ParserPipelineStageInfo
        from ..models.pipeline_stage_info_all_fields import PipelineStageInfoAllFields
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        _execution_id_bytes = d.pop("executionIdBytes", UNSET)
        execution_id_bytes: ByteString | Unset
        if isinstance(_execution_id_bytes, Unset):
            execution_id_bytes = UNSET
        else:
            execution_id_bytes = ByteString.from_dict(_execution_id_bytes)

        _pipeline_name_bytes = d.pop("pipelineNameBytes", UNSET)
        pipeline_name_bytes: ByteString | Unset
        if isinstance(_pipeline_name_bytes, Unset):
            pipeline_name_bytes = UNSET
        else:
            pipeline_name_bytes = ByteString.from_dict(_pipeline_name_bytes)

        _stage_node_id_bytes = d.pop("stageNodeIdBytes", UNSET)
        stage_node_id_bytes: ByteString | Unset
        if isinstance(_stage_node_id_bytes, Unset):
            stage_node_id_bytes = UNSET
        else:
            stage_node_id_bytes = ByteString.from_dict(_stage_node_id_bytes)

        initialized = d.pop("initialized", UNSET)

        identifier = d.pop("identifier", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: PipelineStageInfo | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = PipelineStageInfo.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserPipelineStageInfo | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserPipelineStageInfo.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _identifier_bytes = d.pop("identifierBytes", UNSET)
        identifier_bytes: ByteString | Unset
        if isinstance(_identifier_bytes, Unset):
            identifier_bytes = UNSET
        else:
            identifier_bytes = ByteString.from_dict(_identifier_bytes)

        run_sequence = d.pop("runSequence", UNSET)

        org_id = d.pop("orgId", UNSET)

        _org_id_bytes = d.pop("orgIdBytes", UNSET)
        org_id_bytes: ByteString | Unset
        if isinstance(_org_id_bytes, Unset):
            org_id_bytes = UNSET
        else:
            org_id_bytes = ByteString.from_dict(_org_id_bytes)

        project_id = d.pop("projectId", UNSET)

        _project_id_bytes = d.pop("projectIdBytes", UNSET)
        project_id_bytes: ByteString | Unset
        if isinstance(_project_id_bytes, Unset):
            project_id_bytes = UNSET
        else:
            project_id_bytes = ByteString.from_dict(_project_id_bytes)

        pipeline_name = d.pop("pipelineName", UNSET)

        has_parent_pipeline = d.pop("hasParentPipeline", UNSET)

        stage_node_id = d.pop("stageNodeId", UNSET)

        execution_id = d.pop("executionId", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: PipelineStageInfoAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = PipelineStageInfoAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        pipeline_stage_info = cls(
            unknown_fields=unknown_fields,
            execution_id_bytes=execution_id_bytes,
            pipeline_name_bytes=pipeline_name_bytes,
            stage_node_id_bytes=stage_node_id_bytes,
            initialized=initialized,
            identifier=identifier,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            identifier_bytes=identifier_bytes,
            run_sequence=run_sequence,
            org_id=org_id,
            org_id_bytes=org_id_bytes,
            project_id=project_id,
            project_id_bytes=project_id_bytes,
            pipeline_name=pipeline_name,
            has_parent_pipeline=has_parent_pipeline,
            stage_node_id=stage_node_id,
            execution_id=execution_id,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        pipeline_stage_info.additional_properties = d
        return pipeline_stage_info

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
