from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.parser_policy_metadata import ParserPolicyMetadata
    from ..models.policy_metadata_all_fields import PolicyMetadataAllFields
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="PolicyMetadata")


@_attrs_define
class PolicyMetadata:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        severity (str | Unset):
        initialized (bool | Unset):
        identifier (str | Unset):
        status (str | Unset):
        error (str | Unset):
        default_instance_for_type (PolicyMetadata | Unset):
        parser_for_type (ParserPolicyMetadata | Unset):
        serialized_size (int | Unset):
        identifier_bytes (ByteString | Unset):
        policy_id (str | Unset):
        policy_id_bytes (ByteString | Unset):
        policy_name (str | Unset):
        policy_name_bytes (ByteString | Unset):
        severity_bytes (ByteString | Unset):
        deny_messages_list (list[str] | Unset):
        deny_messages_count (int | Unset):
        status_bytes (ByteString | Unset):
        account_id (str | Unset):
        account_id_bytes (ByteString | Unset):
        org_id (str | Unset):
        org_id_bytes (ByteString | Unset):
        project_id (str | Unset):
        project_id_bytes (ByteString | Unset):
        created (int | Unset):
        updated (int | Unset):
        error_bytes (ByteString | Unset):
        all_fields (PolicyMetadataAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    severity: str | Unset = UNSET
    initialized: bool | Unset = UNSET
    identifier: str | Unset = UNSET
    status: str | Unset = UNSET
    error: str | Unset = UNSET
    default_instance_for_type: PolicyMetadata | Unset = UNSET
    parser_for_type: ParserPolicyMetadata | Unset = UNSET
    serialized_size: int | Unset = UNSET
    identifier_bytes: ByteString | Unset = UNSET
    policy_id: str | Unset = UNSET
    policy_id_bytes: ByteString | Unset = UNSET
    policy_name: str | Unset = UNSET
    policy_name_bytes: ByteString | Unset = UNSET
    severity_bytes: ByteString | Unset = UNSET
    deny_messages_list: list[str] | Unset = UNSET
    deny_messages_count: int | Unset = UNSET
    status_bytes: ByteString | Unset = UNSET
    account_id: str | Unset = UNSET
    account_id_bytes: ByteString | Unset = UNSET
    org_id: str | Unset = UNSET
    org_id_bytes: ByteString | Unset = UNSET
    project_id: str | Unset = UNSET
    project_id_bytes: ByteString | Unset = UNSET
    created: int | Unset = UNSET
    updated: int | Unset = UNSET
    error_bytes: ByteString | Unset = UNSET
    all_fields: PolicyMetadataAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        severity = self.severity

        initialized = self.initialized

        identifier = self.identifier

        status = self.status

        error = self.error

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

        policy_id = self.policy_id

        policy_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy_id_bytes, Unset):
            policy_id_bytes = self.policy_id_bytes.to_dict()

        policy_name = self.policy_name

        policy_name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.policy_name_bytes, Unset):
            policy_name_bytes = self.policy_name_bytes.to_dict()

        severity_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.severity_bytes, Unset):
            severity_bytes = self.severity_bytes.to_dict()

        deny_messages_list: list[str] | Unset = UNSET
        if not isinstance(self.deny_messages_list, Unset):
            deny_messages_list = self.deny_messages_list

        deny_messages_count = self.deny_messages_count

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

        updated = self.updated

        error_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.error_bytes, Unset):
            error_bytes = self.error_bytes.to_dict()

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
        if severity is not UNSET:
            field_dict["severity"] = severity
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if status is not UNSET:
            field_dict["status"] = status
        if error is not UNSET:
            field_dict["error"] = error
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if identifier_bytes is not UNSET:
            field_dict["identifierBytes"] = identifier_bytes
        if policy_id is not UNSET:
            field_dict["policyId"] = policy_id
        if policy_id_bytes is not UNSET:
            field_dict["policyIdBytes"] = policy_id_bytes
        if policy_name is not UNSET:
            field_dict["policyName"] = policy_name
        if policy_name_bytes is not UNSET:
            field_dict["policyNameBytes"] = policy_name_bytes
        if severity_bytes is not UNSET:
            field_dict["severityBytes"] = severity_bytes
        if deny_messages_list is not UNSET:
            field_dict["denyMessagesList"] = deny_messages_list
        if deny_messages_count is not UNSET:
            field_dict["denyMessagesCount"] = deny_messages_count
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
        if updated is not UNSET:
            field_dict["updated"] = updated
        if error_bytes is not UNSET:
            field_dict["errorBytes"] = error_bytes
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
        from ..models.parser_policy_metadata import ParserPolicyMetadata
        from ..models.policy_metadata_all_fields import PolicyMetadataAllFields
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        severity = d.pop("severity", UNSET)

        initialized = d.pop("initialized", UNSET)

        identifier = d.pop("identifier", UNSET)

        status = d.pop("status", UNSET)

        error = d.pop("error", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: PolicyMetadata | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = PolicyMetadata.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserPolicyMetadata | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserPolicyMetadata.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _identifier_bytes = d.pop("identifierBytes", UNSET)
        identifier_bytes: ByteString | Unset
        if isinstance(_identifier_bytes, Unset):
            identifier_bytes = UNSET
        else:
            identifier_bytes = ByteString.from_dict(_identifier_bytes)

        policy_id = d.pop("policyId", UNSET)

        _policy_id_bytes = d.pop("policyIdBytes", UNSET)
        policy_id_bytes: ByteString | Unset
        if isinstance(_policy_id_bytes, Unset):
            policy_id_bytes = UNSET
        else:
            policy_id_bytes = ByteString.from_dict(_policy_id_bytes)

        policy_name = d.pop("policyName", UNSET)

        _policy_name_bytes = d.pop("policyNameBytes", UNSET)
        policy_name_bytes: ByteString | Unset
        if isinstance(_policy_name_bytes, Unset):
            policy_name_bytes = UNSET
        else:
            policy_name_bytes = ByteString.from_dict(_policy_name_bytes)

        _severity_bytes = d.pop("severityBytes", UNSET)
        severity_bytes: ByteString | Unset
        if isinstance(_severity_bytes, Unset):
            severity_bytes = UNSET
        else:
            severity_bytes = ByteString.from_dict(_severity_bytes)

        deny_messages_list = cast(list[str], d.pop("denyMessagesList", UNSET))

        deny_messages_count = d.pop("denyMessagesCount", UNSET)

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

        updated = d.pop("updated", UNSET)

        _error_bytes = d.pop("errorBytes", UNSET)
        error_bytes: ByteString | Unset
        if isinstance(_error_bytes, Unset):
            error_bytes = UNSET
        else:
            error_bytes = ByteString.from_dict(_error_bytes)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: PolicyMetadataAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = PolicyMetadataAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        policy_metadata = cls(
            unknown_fields=unknown_fields,
            severity=severity,
            initialized=initialized,
            identifier=identifier,
            status=status,
            error=error,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            identifier_bytes=identifier_bytes,
            policy_id=policy_id,
            policy_id_bytes=policy_id_bytes,
            policy_name=policy_name,
            policy_name_bytes=policy_name_bytes,
            severity_bytes=severity_bytes,
            deny_messages_list=deny_messages_list,
            deny_messages_count=deny_messages_count,
            status_bytes=status_bytes,
            account_id=account_id,
            account_id_bytes=account_id_bytes,
            org_id=org_id,
            org_id_bytes=org_id_bytes,
            project_id=project_id,
            project_id_bytes=project_id_bytes,
            created=created,
            updated=updated,
            error_bytes=error_bytes,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        policy_metadata.additional_properties = d
        return policy_metadata

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
