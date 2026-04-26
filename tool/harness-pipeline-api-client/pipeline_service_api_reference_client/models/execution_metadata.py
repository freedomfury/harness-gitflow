from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.execution_metadata_execution_mode import (
    ExecutionMetadataExecutionMode,
    check_execution_metadata_execution_mode,
)
from ..models.execution_metadata_pipeline_store_type import (
    ExecutionMetadataPipelineStoreType,
    check_execution_metadata_pipeline_store_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.execution_metadata_all_fields import ExecutionMetadataAllFields
    from ..models.execution_metadata_feature_flag_to_value_map import ExecutionMetadataFeatureFlagToValueMap
    from ..models.execution_metadata_feature_flag_to_value_map_map import ExecutionMetadataFeatureFlagToValueMapMap
    from ..models.execution_metadata_setting_to_value_map import ExecutionMetadataSettingToValueMap
    from ..models.execution_metadata_setting_to_value_map_map import ExecutionMetadataSettingToValueMapMap
    from ..models.execution_principal_info import ExecutionPrincipalInfo
    from ..models.execution_principal_info_or_builder import ExecutionPrincipalInfoOrBuilder
    from ..models.execution_trigger_info import ExecutionTriggerInfo
    from ..models.execution_trigger_info_or_builder import ExecutionTriggerInfoOrBuilder
    from ..models.parser_execution_metadata import ParserExecutionMetadata
    from ..models.pipeline_stage_info import PipelineStageInfo
    from ..models.pipeline_stage_info_or_builder import PipelineStageInfoOrBuilder
    from ..models.retry_execution_info import RetryExecutionInfo
    from ..models.retry_execution_info_or_builder import RetryExecutionInfoOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="ExecutionMetadata")


@_attrs_define
class ExecutionMetadata:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        principal_info (ExecutionPrincipalInfo | Unset):
        initialized (bool | Unset):
        default_instance_for_type (ExecutionMetadata | Unset):
        parser_for_type (ParserExecutionMetadata | Unset):
        serialized_size (int | Unset):
        trigger_info (ExecutionTriggerInfo | Unset):
        trigger_info_or_builder (ExecutionTriggerInfoOrBuilder | Unset):
        pipeline_identifier (str | Unset):
        pipeline_identifier_bytes (ByteString | Unset):
        execution_uuid (str | Unset):
        execution_uuid_bytes (ByteString | Unset):
        principal_info_or_builder (ExecutionPrincipalInfoOrBuilder | Unset):
        git_sync_branch_context (ByteString | Unset):
        module_type (str | Unset):
        module_type_bytes (ByteString | Unset):
        retry_info (RetryExecutionInfo | Unset):
        retry_info_or_builder (RetryExecutionInfoOrBuilder | Unset):
        is_notification_configured (bool | Unset):
        pipeline_store_type_value (int | Unset):
        pipeline_store_type (ExecutionMetadataPipelineStoreType | Unset):
        pipeline_connector_ref (str | Unset):
        pipeline_connector_ref_bytes (ByteString | Unset):
        pipeline_stage_info (PipelineStageInfo | Unset):
        pipeline_stage_info_or_builder (PipelineStageInfoOrBuilder | Unset):
        harness_version (str | Unset):
        harness_version_bytes (ByteString | Unset):
        is_debug (bool | Unset):
        execution_mode_value (int | Unset):
        execution_mode (ExecutionMetadataExecutionMode | Unset):
        original_plan_execution_id_for_rollback_mode (str | Unset):
        original_plan_execution_id_for_rollback_mode_bytes (ByteString | Unset):
        setting_to_value_map_count (int | Unset):
        setting_to_value_map (ExecutionMetadataSettingToValueMap | Unset):
        setting_to_value_map_map (ExecutionMetadataSettingToValueMapMap | Unset):
        feature_flag_to_value_map_count (int | Unset):
        feature_flag_to_value_map (ExecutionMetadataFeatureFlagToValueMap | Unset):
        feature_flag_to_value_map_map (ExecutionMetadataFeatureFlagToValueMapMap | Unset):
        processed_yaml_version (str | Unset):
        processed_yaml_version_bytes (ByteString | Unset):
        is_stages_expressions_provided (bool | Unset):
        branch_seq_id (int | Unset):
        codebase_branch (str | Unset):
        codebase_branch_bytes (ByteString | Unset):
        normalized_repo_url (str | Unset):
        normalized_repo_url_bytes (ByteString | Unset):
        enable_dag (bool | Unset):
        run_sequence (int | Unset):
        all_fields (ExecutionMetadataAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    principal_info: ExecutionPrincipalInfo | Unset = UNSET
    initialized: bool | Unset = UNSET
    default_instance_for_type: ExecutionMetadata | Unset = UNSET
    parser_for_type: ParserExecutionMetadata | Unset = UNSET
    serialized_size: int | Unset = UNSET
    trigger_info: ExecutionTriggerInfo | Unset = UNSET
    trigger_info_or_builder: ExecutionTriggerInfoOrBuilder | Unset = UNSET
    pipeline_identifier: str | Unset = UNSET
    pipeline_identifier_bytes: ByteString | Unset = UNSET
    execution_uuid: str | Unset = UNSET
    execution_uuid_bytes: ByteString | Unset = UNSET
    principal_info_or_builder: ExecutionPrincipalInfoOrBuilder | Unset = UNSET
    git_sync_branch_context: ByteString | Unset = UNSET
    module_type: str | Unset = UNSET
    module_type_bytes: ByteString | Unset = UNSET
    retry_info: RetryExecutionInfo | Unset = UNSET
    retry_info_or_builder: RetryExecutionInfoOrBuilder | Unset = UNSET
    is_notification_configured: bool | Unset = UNSET
    pipeline_store_type_value: int | Unset = UNSET
    pipeline_store_type: ExecutionMetadataPipelineStoreType | Unset = UNSET
    pipeline_connector_ref: str | Unset = UNSET
    pipeline_connector_ref_bytes: ByteString | Unset = UNSET
    pipeline_stage_info: PipelineStageInfo | Unset = UNSET
    pipeline_stage_info_or_builder: PipelineStageInfoOrBuilder | Unset = UNSET
    harness_version: str | Unset = UNSET
    harness_version_bytes: ByteString | Unset = UNSET
    is_debug: bool | Unset = UNSET
    execution_mode_value: int | Unset = UNSET
    execution_mode: ExecutionMetadataExecutionMode | Unset = UNSET
    original_plan_execution_id_for_rollback_mode: str | Unset = UNSET
    original_plan_execution_id_for_rollback_mode_bytes: ByteString | Unset = UNSET
    setting_to_value_map_count: int | Unset = UNSET
    setting_to_value_map: ExecutionMetadataSettingToValueMap | Unset = UNSET
    setting_to_value_map_map: ExecutionMetadataSettingToValueMapMap | Unset = UNSET
    feature_flag_to_value_map_count: int | Unset = UNSET
    feature_flag_to_value_map: ExecutionMetadataFeatureFlagToValueMap | Unset = UNSET
    feature_flag_to_value_map_map: ExecutionMetadataFeatureFlagToValueMapMap | Unset = UNSET
    processed_yaml_version: str | Unset = UNSET
    processed_yaml_version_bytes: ByteString | Unset = UNSET
    is_stages_expressions_provided: bool | Unset = UNSET
    branch_seq_id: int | Unset = UNSET
    codebase_branch: str | Unset = UNSET
    codebase_branch_bytes: ByteString | Unset = UNSET
    normalized_repo_url: str | Unset = UNSET
    normalized_repo_url_bytes: ByteString | Unset = UNSET
    enable_dag: bool | Unset = UNSET
    run_sequence: int | Unset = UNSET
    all_fields: ExecutionMetadataAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        principal_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.principal_info, Unset):
            principal_info = self.principal_info.to_dict()

        initialized = self.initialized

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        trigger_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trigger_info, Unset):
            trigger_info = self.trigger_info.to_dict()

        trigger_info_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trigger_info_or_builder, Unset):
            trigger_info_or_builder = self.trigger_info_or_builder.to_dict()

        pipeline_identifier = self.pipeline_identifier

        pipeline_identifier_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pipeline_identifier_bytes, Unset):
            pipeline_identifier_bytes = self.pipeline_identifier_bytes.to_dict()

        execution_uuid = self.execution_uuid

        execution_uuid_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.execution_uuid_bytes, Unset):
            execution_uuid_bytes = self.execution_uuid_bytes.to_dict()

        principal_info_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.principal_info_or_builder, Unset):
            principal_info_or_builder = self.principal_info_or_builder.to_dict()

        git_sync_branch_context: dict[str, Any] | Unset = UNSET
        if not isinstance(self.git_sync_branch_context, Unset):
            git_sync_branch_context = self.git_sync_branch_context.to_dict()

        module_type = self.module_type

        module_type_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.module_type_bytes, Unset):
            module_type_bytes = self.module_type_bytes.to_dict()

        retry_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retry_info, Unset):
            retry_info = self.retry_info.to_dict()

        retry_info_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.retry_info_or_builder, Unset):
            retry_info_or_builder = self.retry_info_or_builder.to_dict()

        is_notification_configured = self.is_notification_configured

        pipeline_store_type_value = self.pipeline_store_type_value

        pipeline_store_type: str | Unset = UNSET
        if not isinstance(self.pipeline_store_type, Unset):
            pipeline_store_type = self.pipeline_store_type

        pipeline_connector_ref = self.pipeline_connector_ref

        pipeline_connector_ref_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pipeline_connector_ref_bytes, Unset):
            pipeline_connector_ref_bytes = self.pipeline_connector_ref_bytes.to_dict()

        pipeline_stage_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pipeline_stage_info, Unset):
            pipeline_stage_info = self.pipeline_stage_info.to_dict()

        pipeline_stage_info_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.pipeline_stage_info_or_builder, Unset):
            pipeline_stage_info_or_builder = self.pipeline_stage_info_or_builder.to_dict()

        harness_version = self.harness_version

        harness_version_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.harness_version_bytes, Unset):
            harness_version_bytes = self.harness_version_bytes.to_dict()

        is_debug = self.is_debug

        execution_mode_value = self.execution_mode_value

        execution_mode: str | Unset = UNSET
        if not isinstance(self.execution_mode, Unset):
            execution_mode = self.execution_mode

        original_plan_execution_id_for_rollback_mode = self.original_plan_execution_id_for_rollback_mode

        original_plan_execution_id_for_rollback_mode_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.original_plan_execution_id_for_rollback_mode_bytes, Unset):
            original_plan_execution_id_for_rollback_mode_bytes = (
                self.original_plan_execution_id_for_rollback_mode_bytes.to_dict()
            )

        setting_to_value_map_count = self.setting_to_value_map_count

        setting_to_value_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.setting_to_value_map, Unset):
            setting_to_value_map = self.setting_to_value_map.to_dict()

        setting_to_value_map_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.setting_to_value_map_map, Unset):
            setting_to_value_map_map = self.setting_to_value_map_map.to_dict()

        feature_flag_to_value_map_count = self.feature_flag_to_value_map_count

        feature_flag_to_value_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature_flag_to_value_map, Unset):
            feature_flag_to_value_map = self.feature_flag_to_value_map.to_dict()

        feature_flag_to_value_map_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.feature_flag_to_value_map_map, Unset):
            feature_flag_to_value_map_map = self.feature_flag_to_value_map_map.to_dict()

        processed_yaml_version = self.processed_yaml_version

        processed_yaml_version_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.processed_yaml_version_bytes, Unset):
            processed_yaml_version_bytes = self.processed_yaml_version_bytes.to_dict()

        is_stages_expressions_provided = self.is_stages_expressions_provided

        branch_seq_id = self.branch_seq_id

        codebase_branch = self.codebase_branch

        codebase_branch_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.codebase_branch_bytes, Unset):
            codebase_branch_bytes = self.codebase_branch_bytes.to_dict()

        normalized_repo_url = self.normalized_repo_url

        normalized_repo_url_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.normalized_repo_url_bytes, Unset):
            normalized_repo_url_bytes = self.normalized_repo_url_bytes.to_dict()

        enable_dag = self.enable_dag

        run_sequence = self.run_sequence

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
        if principal_info is not UNSET:
            field_dict["principalInfo"] = principal_info
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if trigger_info is not UNSET:
            field_dict["triggerInfo"] = trigger_info
        if trigger_info_or_builder is not UNSET:
            field_dict["triggerInfoOrBuilder"] = trigger_info_or_builder
        if pipeline_identifier is not UNSET:
            field_dict["pipelineIdentifier"] = pipeline_identifier
        if pipeline_identifier_bytes is not UNSET:
            field_dict["pipelineIdentifierBytes"] = pipeline_identifier_bytes
        if execution_uuid is not UNSET:
            field_dict["executionUuid"] = execution_uuid
        if execution_uuid_bytes is not UNSET:
            field_dict["executionUuidBytes"] = execution_uuid_bytes
        if principal_info_or_builder is not UNSET:
            field_dict["principalInfoOrBuilder"] = principal_info_or_builder
        if git_sync_branch_context is not UNSET:
            field_dict["gitSyncBranchContext"] = git_sync_branch_context
        if module_type is not UNSET:
            field_dict["moduleType"] = module_type
        if module_type_bytes is not UNSET:
            field_dict["moduleTypeBytes"] = module_type_bytes
        if retry_info is not UNSET:
            field_dict["retryInfo"] = retry_info
        if retry_info_or_builder is not UNSET:
            field_dict["retryInfoOrBuilder"] = retry_info_or_builder
        if is_notification_configured is not UNSET:
            field_dict["isNotificationConfigured"] = is_notification_configured
        if pipeline_store_type_value is not UNSET:
            field_dict["pipelineStoreTypeValue"] = pipeline_store_type_value
        if pipeline_store_type is not UNSET:
            field_dict["pipelineStoreType"] = pipeline_store_type
        if pipeline_connector_ref is not UNSET:
            field_dict["pipelineConnectorRef"] = pipeline_connector_ref
        if pipeline_connector_ref_bytes is not UNSET:
            field_dict["pipelineConnectorRefBytes"] = pipeline_connector_ref_bytes
        if pipeline_stage_info is not UNSET:
            field_dict["pipelineStageInfo"] = pipeline_stage_info
        if pipeline_stage_info_or_builder is not UNSET:
            field_dict["pipelineStageInfoOrBuilder"] = pipeline_stage_info_or_builder
        if harness_version is not UNSET:
            field_dict["harnessVersion"] = harness_version
        if harness_version_bytes is not UNSET:
            field_dict["harnessVersionBytes"] = harness_version_bytes
        if is_debug is not UNSET:
            field_dict["isDebug"] = is_debug
        if execution_mode_value is not UNSET:
            field_dict["executionModeValue"] = execution_mode_value
        if execution_mode is not UNSET:
            field_dict["executionMode"] = execution_mode
        if original_plan_execution_id_for_rollback_mode is not UNSET:
            field_dict["originalPlanExecutionIdForRollbackMode"] = original_plan_execution_id_for_rollback_mode
        if original_plan_execution_id_for_rollback_mode_bytes is not UNSET:
            field_dict["originalPlanExecutionIdForRollbackModeBytes"] = (
                original_plan_execution_id_for_rollback_mode_bytes
            )
        if setting_to_value_map_count is not UNSET:
            field_dict["settingToValueMapCount"] = setting_to_value_map_count
        if setting_to_value_map is not UNSET:
            field_dict["settingToValueMap"] = setting_to_value_map
        if setting_to_value_map_map is not UNSET:
            field_dict["settingToValueMapMap"] = setting_to_value_map_map
        if feature_flag_to_value_map_count is not UNSET:
            field_dict["featureFlagToValueMapCount"] = feature_flag_to_value_map_count
        if feature_flag_to_value_map is not UNSET:
            field_dict["featureFlagToValueMap"] = feature_flag_to_value_map
        if feature_flag_to_value_map_map is not UNSET:
            field_dict["featureFlagToValueMapMap"] = feature_flag_to_value_map_map
        if processed_yaml_version is not UNSET:
            field_dict["processedYamlVersion"] = processed_yaml_version
        if processed_yaml_version_bytes is not UNSET:
            field_dict["processedYamlVersionBytes"] = processed_yaml_version_bytes
        if is_stages_expressions_provided is not UNSET:
            field_dict["isStagesExpressionsProvided"] = is_stages_expressions_provided
        if branch_seq_id is not UNSET:
            field_dict["branchSeqId"] = branch_seq_id
        if codebase_branch is not UNSET:
            field_dict["codebaseBranch"] = codebase_branch
        if codebase_branch_bytes is not UNSET:
            field_dict["codebaseBranchBytes"] = codebase_branch_bytes
        if normalized_repo_url is not UNSET:
            field_dict["normalizedRepoUrl"] = normalized_repo_url
        if normalized_repo_url_bytes is not UNSET:
            field_dict["normalizedRepoUrlBytes"] = normalized_repo_url_bytes
        if enable_dag is not UNSET:
            field_dict["enableDAG"] = enable_dag
        if run_sequence is not UNSET:
            field_dict["runSequence"] = run_sequence
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
        from ..models.execution_metadata_all_fields import ExecutionMetadataAllFields
        from ..models.execution_metadata_feature_flag_to_value_map import ExecutionMetadataFeatureFlagToValueMap
        from ..models.execution_metadata_feature_flag_to_value_map_map import ExecutionMetadataFeatureFlagToValueMapMap
        from ..models.execution_metadata_setting_to_value_map import ExecutionMetadataSettingToValueMap
        from ..models.execution_metadata_setting_to_value_map_map import ExecutionMetadataSettingToValueMapMap
        from ..models.execution_principal_info import ExecutionPrincipalInfo
        from ..models.execution_principal_info_or_builder import ExecutionPrincipalInfoOrBuilder
        from ..models.execution_trigger_info import ExecutionTriggerInfo
        from ..models.execution_trigger_info_or_builder import ExecutionTriggerInfoOrBuilder
        from ..models.parser_execution_metadata import ParserExecutionMetadata
        from ..models.pipeline_stage_info import PipelineStageInfo
        from ..models.pipeline_stage_info_or_builder import PipelineStageInfoOrBuilder
        from ..models.retry_execution_info import RetryExecutionInfo
        from ..models.retry_execution_info_or_builder import RetryExecutionInfoOrBuilder
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        _principal_info = d.pop("principalInfo", UNSET)
        principal_info: ExecutionPrincipalInfo | Unset
        if isinstance(_principal_info, Unset):
            principal_info = UNSET
        else:
            principal_info = ExecutionPrincipalInfo.from_dict(_principal_info)

        initialized = d.pop("initialized", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: ExecutionMetadata | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = ExecutionMetadata.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserExecutionMetadata | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserExecutionMetadata.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _trigger_info = d.pop("triggerInfo", UNSET)
        trigger_info: ExecutionTriggerInfo | Unset
        if isinstance(_trigger_info, Unset):
            trigger_info = UNSET
        else:
            trigger_info = ExecutionTriggerInfo.from_dict(_trigger_info)

        _trigger_info_or_builder = d.pop("triggerInfoOrBuilder", UNSET)
        trigger_info_or_builder: ExecutionTriggerInfoOrBuilder | Unset
        if isinstance(_trigger_info_or_builder, Unset):
            trigger_info_or_builder = UNSET
        else:
            trigger_info_or_builder = ExecutionTriggerInfoOrBuilder.from_dict(_trigger_info_or_builder)

        pipeline_identifier = d.pop("pipelineIdentifier", UNSET)

        _pipeline_identifier_bytes = d.pop("pipelineIdentifierBytes", UNSET)
        pipeline_identifier_bytes: ByteString | Unset
        if isinstance(_pipeline_identifier_bytes, Unset):
            pipeline_identifier_bytes = UNSET
        else:
            pipeline_identifier_bytes = ByteString.from_dict(_pipeline_identifier_bytes)

        execution_uuid = d.pop("executionUuid", UNSET)

        _execution_uuid_bytes = d.pop("executionUuidBytes", UNSET)
        execution_uuid_bytes: ByteString | Unset
        if isinstance(_execution_uuid_bytes, Unset):
            execution_uuid_bytes = UNSET
        else:
            execution_uuid_bytes = ByteString.from_dict(_execution_uuid_bytes)

        _principal_info_or_builder = d.pop("principalInfoOrBuilder", UNSET)
        principal_info_or_builder: ExecutionPrincipalInfoOrBuilder | Unset
        if isinstance(_principal_info_or_builder, Unset):
            principal_info_or_builder = UNSET
        else:
            principal_info_or_builder = ExecutionPrincipalInfoOrBuilder.from_dict(_principal_info_or_builder)

        _git_sync_branch_context = d.pop("gitSyncBranchContext", UNSET)
        git_sync_branch_context: ByteString | Unset
        if isinstance(_git_sync_branch_context, Unset):
            git_sync_branch_context = UNSET
        else:
            git_sync_branch_context = ByteString.from_dict(_git_sync_branch_context)

        module_type = d.pop("moduleType", UNSET)

        _module_type_bytes = d.pop("moduleTypeBytes", UNSET)
        module_type_bytes: ByteString | Unset
        if isinstance(_module_type_bytes, Unset):
            module_type_bytes = UNSET
        else:
            module_type_bytes = ByteString.from_dict(_module_type_bytes)

        _retry_info = d.pop("retryInfo", UNSET)
        retry_info: RetryExecutionInfo | Unset
        if isinstance(_retry_info, Unset):
            retry_info = UNSET
        else:
            retry_info = RetryExecutionInfo.from_dict(_retry_info)

        _retry_info_or_builder = d.pop("retryInfoOrBuilder", UNSET)
        retry_info_or_builder: RetryExecutionInfoOrBuilder | Unset
        if isinstance(_retry_info_or_builder, Unset):
            retry_info_or_builder = UNSET
        else:
            retry_info_or_builder = RetryExecutionInfoOrBuilder.from_dict(_retry_info_or_builder)

        is_notification_configured = d.pop("isNotificationConfigured", UNSET)

        pipeline_store_type_value = d.pop("pipelineStoreTypeValue", UNSET)

        _pipeline_store_type = d.pop("pipelineStoreType", UNSET)
        pipeline_store_type: ExecutionMetadataPipelineStoreType | Unset
        if isinstance(_pipeline_store_type, Unset):
            pipeline_store_type = UNSET
        else:
            pipeline_store_type = check_execution_metadata_pipeline_store_type(_pipeline_store_type)

        pipeline_connector_ref = d.pop("pipelineConnectorRef", UNSET)

        _pipeline_connector_ref_bytes = d.pop("pipelineConnectorRefBytes", UNSET)
        pipeline_connector_ref_bytes: ByteString | Unset
        if isinstance(_pipeline_connector_ref_bytes, Unset):
            pipeline_connector_ref_bytes = UNSET
        else:
            pipeline_connector_ref_bytes = ByteString.from_dict(_pipeline_connector_ref_bytes)

        _pipeline_stage_info = d.pop("pipelineStageInfo", UNSET)
        pipeline_stage_info: PipelineStageInfo | Unset
        if isinstance(_pipeline_stage_info, Unset):
            pipeline_stage_info = UNSET
        else:
            pipeline_stage_info = PipelineStageInfo.from_dict(_pipeline_stage_info)

        _pipeline_stage_info_or_builder = d.pop("pipelineStageInfoOrBuilder", UNSET)
        pipeline_stage_info_or_builder: PipelineStageInfoOrBuilder | Unset
        if isinstance(_pipeline_stage_info_or_builder, Unset):
            pipeline_stage_info_or_builder = UNSET
        else:
            pipeline_stage_info_or_builder = PipelineStageInfoOrBuilder.from_dict(_pipeline_stage_info_or_builder)

        harness_version = d.pop("harnessVersion", UNSET)

        _harness_version_bytes = d.pop("harnessVersionBytes", UNSET)
        harness_version_bytes: ByteString | Unset
        if isinstance(_harness_version_bytes, Unset):
            harness_version_bytes = UNSET
        else:
            harness_version_bytes = ByteString.from_dict(_harness_version_bytes)

        is_debug = d.pop("isDebug", UNSET)

        execution_mode_value = d.pop("executionModeValue", UNSET)

        _execution_mode = d.pop("executionMode", UNSET)
        execution_mode: ExecutionMetadataExecutionMode | Unset
        if isinstance(_execution_mode, Unset):
            execution_mode = UNSET
        else:
            execution_mode = check_execution_metadata_execution_mode(_execution_mode)

        original_plan_execution_id_for_rollback_mode = d.pop("originalPlanExecutionIdForRollbackMode", UNSET)

        _original_plan_execution_id_for_rollback_mode_bytes = d.pop(
            "originalPlanExecutionIdForRollbackModeBytes", UNSET
        )
        original_plan_execution_id_for_rollback_mode_bytes: ByteString | Unset
        if isinstance(_original_plan_execution_id_for_rollback_mode_bytes, Unset):
            original_plan_execution_id_for_rollback_mode_bytes = UNSET
        else:
            original_plan_execution_id_for_rollback_mode_bytes = ByteString.from_dict(
                _original_plan_execution_id_for_rollback_mode_bytes
            )

        setting_to_value_map_count = d.pop("settingToValueMapCount", UNSET)

        _setting_to_value_map = d.pop("settingToValueMap", UNSET)
        setting_to_value_map: ExecutionMetadataSettingToValueMap | Unset
        if isinstance(_setting_to_value_map, Unset):
            setting_to_value_map = UNSET
        else:
            setting_to_value_map = ExecutionMetadataSettingToValueMap.from_dict(_setting_to_value_map)

        _setting_to_value_map_map = d.pop("settingToValueMapMap", UNSET)
        setting_to_value_map_map: ExecutionMetadataSettingToValueMapMap | Unset
        if isinstance(_setting_to_value_map_map, Unset):
            setting_to_value_map_map = UNSET
        else:
            setting_to_value_map_map = ExecutionMetadataSettingToValueMapMap.from_dict(_setting_to_value_map_map)

        feature_flag_to_value_map_count = d.pop("featureFlagToValueMapCount", UNSET)

        _feature_flag_to_value_map = d.pop("featureFlagToValueMap", UNSET)
        feature_flag_to_value_map: ExecutionMetadataFeatureFlagToValueMap | Unset
        if isinstance(_feature_flag_to_value_map, Unset):
            feature_flag_to_value_map = UNSET
        else:
            feature_flag_to_value_map = ExecutionMetadataFeatureFlagToValueMap.from_dict(_feature_flag_to_value_map)

        _feature_flag_to_value_map_map = d.pop("featureFlagToValueMapMap", UNSET)
        feature_flag_to_value_map_map: ExecutionMetadataFeatureFlagToValueMapMap | Unset
        if isinstance(_feature_flag_to_value_map_map, Unset):
            feature_flag_to_value_map_map = UNSET
        else:
            feature_flag_to_value_map_map = ExecutionMetadataFeatureFlagToValueMapMap.from_dict(
                _feature_flag_to_value_map_map
            )

        processed_yaml_version = d.pop("processedYamlVersion", UNSET)

        _processed_yaml_version_bytes = d.pop("processedYamlVersionBytes", UNSET)
        processed_yaml_version_bytes: ByteString | Unset
        if isinstance(_processed_yaml_version_bytes, Unset):
            processed_yaml_version_bytes = UNSET
        else:
            processed_yaml_version_bytes = ByteString.from_dict(_processed_yaml_version_bytes)

        is_stages_expressions_provided = d.pop("isStagesExpressionsProvided", UNSET)

        branch_seq_id = d.pop("branchSeqId", UNSET)

        codebase_branch = d.pop("codebaseBranch", UNSET)

        _codebase_branch_bytes = d.pop("codebaseBranchBytes", UNSET)
        codebase_branch_bytes: ByteString | Unset
        if isinstance(_codebase_branch_bytes, Unset):
            codebase_branch_bytes = UNSET
        else:
            codebase_branch_bytes = ByteString.from_dict(_codebase_branch_bytes)

        normalized_repo_url = d.pop("normalizedRepoUrl", UNSET)

        _normalized_repo_url_bytes = d.pop("normalizedRepoUrlBytes", UNSET)
        normalized_repo_url_bytes: ByteString | Unset
        if isinstance(_normalized_repo_url_bytes, Unset):
            normalized_repo_url_bytes = UNSET
        else:
            normalized_repo_url_bytes = ByteString.from_dict(_normalized_repo_url_bytes)

        enable_dag = d.pop("enableDAG", UNSET)

        run_sequence = d.pop("runSequence", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: ExecutionMetadataAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = ExecutionMetadataAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        execution_metadata = cls(
            unknown_fields=unknown_fields,
            principal_info=principal_info,
            initialized=initialized,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            trigger_info=trigger_info,
            trigger_info_or_builder=trigger_info_or_builder,
            pipeline_identifier=pipeline_identifier,
            pipeline_identifier_bytes=pipeline_identifier_bytes,
            execution_uuid=execution_uuid,
            execution_uuid_bytes=execution_uuid_bytes,
            principal_info_or_builder=principal_info_or_builder,
            git_sync_branch_context=git_sync_branch_context,
            module_type=module_type,
            module_type_bytes=module_type_bytes,
            retry_info=retry_info,
            retry_info_or_builder=retry_info_or_builder,
            is_notification_configured=is_notification_configured,
            pipeline_store_type_value=pipeline_store_type_value,
            pipeline_store_type=pipeline_store_type,
            pipeline_connector_ref=pipeline_connector_ref,
            pipeline_connector_ref_bytes=pipeline_connector_ref_bytes,
            pipeline_stage_info=pipeline_stage_info,
            pipeline_stage_info_or_builder=pipeline_stage_info_or_builder,
            harness_version=harness_version,
            harness_version_bytes=harness_version_bytes,
            is_debug=is_debug,
            execution_mode_value=execution_mode_value,
            execution_mode=execution_mode,
            original_plan_execution_id_for_rollback_mode=original_plan_execution_id_for_rollback_mode,
            original_plan_execution_id_for_rollback_mode_bytes=original_plan_execution_id_for_rollback_mode_bytes,
            setting_to_value_map_count=setting_to_value_map_count,
            setting_to_value_map=setting_to_value_map,
            setting_to_value_map_map=setting_to_value_map_map,
            feature_flag_to_value_map_count=feature_flag_to_value_map_count,
            feature_flag_to_value_map=feature_flag_to_value_map,
            feature_flag_to_value_map_map=feature_flag_to_value_map_map,
            processed_yaml_version=processed_yaml_version,
            processed_yaml_version_bytes=processed_yaml_version_bytes,
            is_stages_expressions_provided=is_stages_expressions_provided,
            branch_seq_id=branch_seq_id,
            codebase_branch=codebase_branch,
            codebase_branch_bytes=codebase_branch_bytes,
            normalized_repo_url=normalized_repo_url,
            normalized_repo_url_bytes=normalized_repo_url_bytes,
            enable_dag=enable_dag,
            run_sequence=run_sequence,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        execution_metadata.additional_properties = d
        return execution_metadata

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
