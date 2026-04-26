from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.governance_metadata_all_fields import GovernanceMetadataAllFields
    from ..models.parser_governance_metadata import ParserGovernanceMetadata
    from ..models.policy_set_metadata import PolicySetMetadata
    from ..models.policy_set_metadata_or_builder import PolicySetMetadataOrBuilder
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="GovernanceMetadata")


@_attrs_define
class GovernanceMetadata:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        message (str | Unset):
        id (str | Unset):
        type_ (str | Unset):
        timestamp (int | Unset):
        initialized (bool | Unset):
        status (str | Unset):
        action (str | Unset):
        entity (str | Unset):
        default_instance_for_type (GovernanceMetadata | Unset):
        parser_for_type (ParserGovernanceMetadata | Unset):
        serialized_size (int | Unset):
        type_bytes (ByteString | Unset):
        message_bytes (ByteString | Unset):
        status_bytes (ByteString | Unset):
        account_id (str | Unset):
        account_id_bytes (ByteString | Unset):
        org_id (str | Unset):
        org_id_bytes (ByteString | Unset):
        project_id (str | Unset):
        project_id_bytes (ByteString | Unset):
        created (int | Unset):
        deny (bool | Unset):
        details_list (list[PolicySetMetadata] | Unset):
        id_bytes (ByteString | Unset):
        details_count (int | Unset):
        details_or_builder_list (list[PolicySetMetadataOrBuilder] | Unset):
        entity_bytes (ByteString | Unset):
        action_bytes (ByteString | Unset):
        all_fields (GovernanceMetadataAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    message: str | Unset = UNSET
    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    timestamp: int | Unset = UNSET
    initialized: bool | Unset = UNSET
    status: str | Unset = UNSET
    action: str | Unset = UNSET
    entity: str | Unset = UNSET
    default_instance_for_type: GovernanceMetadata | Unset = UNSET
    parser_for_type: ParserGovernanceMetadata | Unset = UNSET
    serialized_size: int | Unset = UNSET
    type_bytes: ByteString | Unset = UNSET
    message_bytes: ByteString | Unset = UNSET
    status_bytes: ByteString | Unset = UNSET
    account_id: str | Unset = UNSET
    account_id_bytes: ByteString | Unset = UNSET
    org_id: str | Unset = UNSET
    org_id_bytes: ByteString | Unset = UNSET
    project_id: str | Unset = UNSET
    project_id_bytes: ByteString | Unset = UNSET
    created: int | Unset = UNSET
    deny: bool | Unset = UNSET
    details_list: list[PolicySetMetadata] | Unset = UNSET
    id_bytes: ByteString | Unset = UNSET
    details_count: int | Unset = UNSET
    details_or_builder_list: list[PolicySetMetadataOrBuilder] | Unset = UNSET
    entity_bytes: ByteString | Unset = UNSET
    action_bytes: ByteString | Unset = UNSET
    all_fields: GovernanceMetadataAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        message = self.message

        id = self.id

        type_ = self.type_

        timestamp = self.timestamp

        initialized = self.initialized

        status = self.status

        action = self.action

        entity = self.entity

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        type_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.type_bytes, Unset):
            type_bytes = self.type_bytes.to_dict()

        message_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.message_bytes, Unset):
            message_bytes = self.message_bytes.to_dict()

        status_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.status_bytes, Unset):
            status_bytes = self.status_bytes.to_dict()

        account_id = self.account_id

        account_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.account_id_bytes, Unset):
            account_id_bytes = self.account_id_bytes.to_dict()

        org_id = self.org_id

        org_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.org_id_bytes, Unset):
            org_id_bytes = self.org_id_bytes.to_dict()

        project_id = self.project_id

        project_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.project_id_bytes, Unset):
            project_id_bytes = self.project_id_bytes.to_dict()

        created = self.created

        deny = self.deny

        details_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.details_list, Unset):
            details_list = []
            for details_list_item_data in self.details_list:
                details_list_item = details_list_item_data.to_dict()
                details_list.append(details_list_item)

        id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.id_bytes, Unset):
            id_bytes = self.id_bytes.to_dict()

        details_count = self.details_count

        details_or_builder_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.details_or_builder_list, Unset):
            details_or_builder_list = []
            for details_or_builder_list_item_data in self.details_or_builder_list:
                details_or_builder_list_item = details_or_builder_list_item_data.to_dict()
                details_or_builder_list.append(details_or_builder_list_item)

        entity_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.entity_bytes, Unset):
            entity_bytes = self.entity_bytes.to_dict()

        action_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.action_bytes, Unset):
            action_bytes = self.action_bytes.to_dict()

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
        if message is not UNSET:
            field_dict["message"] = message
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if status is not UNSET:
            field_dict["status"] = status
        if action is not UNSET:
            field_dict["action"] = action
        if entity is not UNSET:
            field_dict["entity"] = entity
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if type_bytes is not UNSET:
            field_dict["typeBytes"] = type_bytes
        if message_bytes is not UNSET:
            field_dict["messageBytes"] = message_bytes
        if status_bytes is not UNSET:
            field_dict["statusBytes"] = status_bytes
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if account_id_bytes is not UNSET:
            field_dict["accountIdBytes"] = account_id_bytes
        if org_id is not UNSET:
            field_dict["orgId"] = org_id
        if org_id_bytes is not UNSET:
            field_dict["orgIdBytes"] = org_id_bytes
        if project_id is not UNSET:
            field_dict["projectId"] = project_id
        if project_id_bytes is not UNSET:
            field_dict["projectIdBytes"] = project_id_bytes
        if created is not UNSET:
            field_dict["created"] = created
        if deny is not UNSET:
            field_dict["deny"] = deny
        if details_list is not UNSET:
            field_dict["detailsList"] = details_list
        if id_bytes is not UNSET:
            field_dict["idBytes"] = id_bytes
        if details_count is not UNSET:
            field_dict["detailsCount"] = details_count
        if details_or_builder_list is not UNSET:
            field_dict["detailsOrBuilderList"] = details_or_builder_list
        if entity_bytes is not UNSET:
            field_dict["entityBytes"] = entity_bytes
        if action_bytes is not UNSET:
            field_dict["actionBytes"] = action_bytes
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
        from ..models.governance_metadata_all_fields import GovernanceMetadataAllFields
        from ..models.parser_governance_metadata import ParserGovernanceMetadata
        from ..models.policy_set_metadata import PolicySetMetadata
        from ..models.policy_set_metadata_or_builder import PolicySetMetadataOrBuilder
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        message = d.pop("message", UNSET)

        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        timestamp = d.pop("timestamp", UNSET)

        initialized = d.pop("initialized", UNSET)

        status = d.pop("status", UNSET)

        action = d.pop("action", UNSET)

        entity = d.pop("entity", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: GovernanceMetadata | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = GovernanceMetadata.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserGovernanceMetadata | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserGovernanceMetadata.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _type_bytes = d.pop("typeBytes", UNSET)
        type_bytes: ByteString | Unset
        if isinstance(_type_bytes, Unset):
            type_bytes = UNSET
        else:
            type_bytes = ByteString.from_dict(_type_bytes)

        _message_bytes = d.pop("messageBytes", UNSET)
        message_bytes: ByteString | Unset
        if isinstance(_message_bytes, Unset):
            message_bytes = UNSET
        else:
            message_bytes = ByteString.from_dict(_message_bytes)

        _status_bytes = d.pop("statusBytes", UNSET)
        status_bytes: ByteString | Unset
        if isinstance(_status_bytes, Unset):
            status_bytes = UNSET
        else:
            status_bytes = ByteString.from_dict(_status_bytes)

        account_id = d.pop("accountId", UNSET)

        _account_id_bytes = d.pop("accountIdBytes", UNSET)
        account_id_bytes: ByteString | Unset
        if isinstance(_account_id_bytes, Unset):
            account_id_bytes = UNSET
        else:
            account_id_bytes = ByteString.from_dict(_account_id_bytes)

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

        created = d.pop("created", UNSET)

        deny = d.pop("deny", UNSET)

        _details_list = d.pop("detailsList", UNSET)
        details_list: list[PolicySetMetadata] | Unset = UNSET
        if _details_list is not UNSET:
            details_list = []
            for details_list_item_data in _details_list:
                details_list_item = PolicySetMetadata.from_dict(details_list_item_data)

                details_list.append(details_list_item)

        _id_bytes = d.pop("idBytes", UNSET)
        id_bytes: ByteString | Unset
        if isinstance(_id_bytes, Unset):
            id_bytes = UNSET
        else:
            id_bytes = ByteString.from_dict(_id_bytes)

        details_count = d.pop("detailsCount", UNSET)

        _details_or_builder_list = d.pop("detailsOrBuilderList", UNSET)
        details_or_builder_list: list[PolicySetMetadataOrBuilder] | Unset = UNSET
        if _details_or_builder_list is not UNSET:
            details_or_builder_list = []
            for details_or_builder_list_item_data in _details_or_builder_list:
                details_or_builder_list_item = PolicySetMetadataOrBuilder.from_dict(details_or_builder_list_item_data)

                details_or_builder_list.append(details_or_builder_list_item)

        _entity_bytes = d.pop("entityBytes", UNSET)
        entity_bytes: ByteString | Unset
        if isinstance(_entity_bytes, Unset):
            entity_bytes = UNSET
        else:
            entity_bytes = ByteString.from_dict(_entity_bytes)

        _action_bytes = d.pop("actionBytes", UNSET)
        action_bytes: ByteString | Unset
        if isinstance(_action_bytes, Unset):
            action_bytes = UNSET
        else:
            action_bytes = ByteString.from_dict(_action_bytes)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: GovernanceMetadataAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = GovernanceMetadataAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        governance_metadata = cls(
            unknown_fields=unknown_fields,
            message=message,
            id=id,
            type_=type_,
            timestamp=timestamp,
            initialized=initialized,
            status=status,
            action=action,
            entity=entity,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            type_bytes=type_bytes,
            message_bytes=message_bytes,
            status_bytes=status_bytes,
            account_id=account_id,
            account_id_bytes=account_id_bytes,
            org_id=org_id,
            org_id_bytes=org_id_bytes,
            project_id=project_id,
            project_id_bytes=project_id_bytes,
            created=created,
            deny=deny,
            details_list=details_list,
            id_bytes=id_bytes,
            details_count=details_count,
            details_or_builder_list=details_or_builder_list,
            entity_bytes=entity_bytes,
            action_bytes=action_bytes,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        governance_metadata.additional_properties = d
        return governance_metadata

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
