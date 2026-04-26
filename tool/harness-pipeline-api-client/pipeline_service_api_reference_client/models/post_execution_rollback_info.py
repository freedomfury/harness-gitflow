from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.parser_post_execution_rollback_info import ParserPostExecutionRollbackInfo
    from ..models.post_execution_rollback_info_all_fields import PostExecutionRollbackInfoAllFields
    from ..models.strategy_metadata import StrategyMetadata
    from ..models.strategy_metadata_or_builder import StrategyMetadataOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="PostExecutionRollbackInfo")


@_attrs_define
class PostExecutionRollbackInfo:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        post_execution_rollback_stage_id (str | Unset):
        rollback_stage_strategy_metadata (StrategyMetadata | Unset):
        post_execution_rollback_stage_id_bytes (ByteString | Unset):
        rollback_stage_strategy_metadata_or_builder (StrategyMetadataOrBuilder | Unset):
        original_stage_execution_id_bytes (ByteString | Unset):
        initialized (bool | Unset):
        default_instance_for_type (PostExecutionRollbackInfo | Unset):
        parser_for_type (ParserPostExecutionRollbackInfo | Unset):
        serialized_size (int | Unset):
        original_stage_execution_id (str | Unset):
        all_fields (PostExecutionRollbackInfoAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    post_execution_rollback_stage_id: str | Unset = UNSET
    rollback_stage_strategy_metadata: StrategyMetadata | Unset = UNSET
    post_execution_rollback_stage_id_bytes: ByteString | Unset = UNSET
    rollback_stage_strategy_metadata_or_builder: StrategyMetadataOrBuilder | Unset = UNSET
    original_stage_execution_id_bytes: ByteString | Unset = UNSET
    initialized: bool | Unset = UNSET
    default_instance_for_type: PostExecutionRollbackInfo | Unset = UNSET
    parser_for_type: ParserPostExecutionRollbackInfo | Unset = UNSET
    serialized_size: int | Unset = UNSET
    original_stage_execution_id: str | Unset = UNSET
    all_fields: PostExecutionRollbackInfoAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        post_execution_rollback_stage_id = self.post_execution_rollback_stage_id

        rollback_stage_strategy_metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rollback_stage_strategy_metadata, Unset):
            rollback_stage_strategy_metadata = self.rollback_stage_strategy_metadata.to_dict()

        post_execution_rollback_stage_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.post_execution_rollback_stage_id_bytes, Unset):
            post_execution_rollback_stage_id_bytes = self.post_execution_rollback_stage_id_bytes.to_dict()

        rollback_stage_strategy_metadata_or_builder: dict[str, Any] | Unset = UNSET
        if not isinstance(self.rollback_stage_strategy_metadata_or_builder, Unset):
            rollback_stage_strategy_metadata_or_builder = self.rollback_stage_strategy_metadata_or_builder.to_dict()

        original_stage_execution_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.original_stage_execution_id_bytes, Unset):
            original_stage_execution_id_bytes = self.original_stage_execution_id_bytes.to_dict()

        initialized = self.initialized

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        original_stage_execution_id = self.original_stage_execution_id

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
        if post_execution_rollback_stage_id is not UNSET:
            field_dict["postExecutionRollbackStageId"] = post_execution_rollback_stage_id
        if rollback_stage_strategy_metadata is not UNSET:
            field_dict["rollbackStageStrategyMetadata"] = rollback_stage_strategy_metadata
        if post_execution_rollback_stage_id_bytes is not UNSET:
            field_dict["postExecutionRollbackStageIdBytes"] = post_execution_rollback_stage_id_bytes
        if rollback_stage_strategy_metadata_or_builder is not UNSET:
            field_dict["rollbackStageStrategyMetadataOrBuilder"] = rollback_stage_strategy_metadata_or_builder
        if original_stage_execution_id_bytes is not UNSET:
            field_dict["originalStageExecutionIdBytes"] = original_stage_execution_id_bytes
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if original_stage_execution_id is not UNSET:
            field_dict["originalStageExecutionId"] = original_stage_execution_id
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
        from ..models.parser_post_execution_rollback_info import ParserPostExecutionRollbackInfo
        from ..models.post_execution_rollback_info_all_fields import PostExecutionRollbackInfoAllFields
        from ..models.strategy_metadata import StrategyMetadata
        from ..models.strategy_metadata_or_builder import StrategyMetadataOrBuilder
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        post_execution_rollback_stage_id = d.pop("postExecutionRollbackStageId", UNSET)

        _rollback_stage_strategy_metadata = d.pop("rollbackStageStrategyMetadata", UNSET)
        rollback_stage_strategy_metadata: StrategyMetadata | Unset
        if isinstance(_rollback_stage_strategy_metadata, Unset):
            rollback_stage_strategy_metadata = UNSET
        else:
            rollback_stage_strategy_metadata = StrategyMetadata.from_dict(_rollback_stage_strategy_metadata)

        _post_execution_rollback_stage_id_bytes = d.pop("postExecutionRollbackStageIdBytes", UNSET)
        post_execution_rollback_stage_id_bytes: ByteString | Unset
        if isinstance(_post_execution_rollback_stage_id_bytes, Unset):
            post_execution_rollback_stage_id_bytes = UNSET
        else:
            post_execution_rollback_stage_id_bytes = ByteString.from_dict(_post_execution_rollback_stage_id_bytes)

        _rollback_stage_strategy_metadata_or_builder = d.pop("rollbackStageStrategyMetadataOrBuilder", UNSET)
        rollback_stage_strategy_metadata_or_builder: StrategyMetadataOrBuilder | Unset
        if isinstance(_rollback_stage_strategy_metadata_or_builder, Unset):
            rollback_stage_strategy_metadata_or_builder = UNSET
        else:
            rollback_stage_strategy_metadata_or_builder = StrategyMetadataOrBuilder.from_dict(
                _rollback_stage_strategy_metadata_or_builder
            )

        _original_stage_execution_id_bytes = d.pop("originalStageExecutionIdBytes", UNSET)
        original_stage_execution_id_bytes: ByteString | Unset
        if isinstance(_original_stage_execution_id_bytes, Unset):
            original_stage_execution_id_bytes = UNSET
        else:
            original_stage_execution_id_bytes = ByteString.from_dict(_original_stage_execution_id_bytes)

        initialized = d.pop("initialized", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: PostExecutionRollbackInfo | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = PostExecutionRollbackInfo.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserPostExecutionRollbackInfo | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserPostExecutionRollbackInfo.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        original_stage_execution_id = d.pop("originalStageExecutionId", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: PostExecutionRollbackInfoAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = PostExecutionRollbackInfoAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        post_execution_rollback_info = cls(
            unknown_fields=unknown_fields,
            post_execution_rollback_stage_id=post_execution_rollback_stage_id,
            rollback_stage_strategy_metadata=rollback_stage_strategy_metadata,
            post_execution_rollback_stage_id_bytes=post_execution_rollback_stage_id_bytes,
            rollback_stage_strategy_metadata_or_builder=rollback_stage_strategy_metadata_or_builder,
            original_stage_execution_id_bytes=original_stage_execution_id_bytes,
            initialized=initialized,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            original_stage_execution_id=original_stage_execution_id,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        post_execution_rollback_info.additional_properties = d
        return post_execution_rollback_info

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
