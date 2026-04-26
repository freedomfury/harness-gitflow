from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.parser_triggered_by import ParserTriggeredBy
    from ..models.triggered_by_all_fields import TriggeredByAllFields
    from ..models.triggered_by_extra_info import TriggeredByExtraInfo
    from ..models.triggered_by_extra_info_map import TriggeredByExtraInfoMap
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="TriggeredBy")


@_attrs_define
class TriggeredBy:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        initialized (bool | Unset):
        identifier (str | Unset):
        default_instance_for_type (TriggeredBy | Unset):
        parser_for_type (ParserTriggeredBy | Unset):
        serialized_size (int | Unset):
        uuid_bytes (ByteString | Unset):
        uuid (str | Unset):
        identifier_bytes (ByteString | Unset):
        extra_info_count (int | Unset):
        extra_info (TriggeredByExtraInfo | Unset):
        extra_info_map (TriggeredByExtraInfoMap | Unset):
        trigger_identifier (str | Unset):
        trigger_identifier_bytes (ByteString | Unset):
        trigger_name (str | Unset):
        trigger_name_bytes (ByteString | Unset):
        impersonate_username (str | Unset):
        impersonate_username_bytes (ByteString | Unset):
        impersonate_email (str | Unset):
        impersonate_email_bytes (ByteString | Unset):
        all_fields (TriggeredByAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialized: bool | Unset = UNSET
    identifier: str | Unset = UNSET
    default_instance_for_type: TriggeredBy | Unset = UNSET
    parser_for_type: ParserTriggeredBy | Unset = UNSET
    serialized_size: int | Unset = UNSET
    uuid_bytes: ByteString | Unset = UNSET
    uuid: str | Unset = UNSET
    identifier_bytes: ByteString | Unset = UNSET
    extra_info_count: int | Unset = UNSET
    extra_info: TriggeredByExtraInfo | Unset = UNSET
    extra_info_map: TriggeredByExtraInfoMap | Unset = UNSET
    trigger_identifier: str | Unset = UNSET
    trigger_identifier_bytes: ByteString | Unset = UNSET
    trigger_name: str | Unset = UNSET
    trigger_name_bytes: ByteString | Unset = UNSET
    impersonate_username: str | Unset = UNSET
    impersonate_username_bytes: ByteString | Unset = UNSET
    impersonate_email: str | Unset = UNSET
    impersonate_email_bytes: ByteString | Unset = UNSET
    all_fields: TriggeredByAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        initialized = self.initialized

        identifier = self.identifier

        default_instance_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.default_instance_for_type, Unset):
            default_instance_for_type = self.default_instance_for_type.to_dict()

        parser_for_type: dict[str, Any] | Unset = UNSET
        if not isinstance(self.parser_for_type, Unset):
            parser_for_type = self.parser_for_type.to_dict()

        serialized_size = self.serialized_size

        uuid_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.uuid_bytes, Unset):
            uuid_bytes = self.uuid_bytes.to_dict()

        uuid = self.uuid

        identifier_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.identifier_bytes, Unset):
            identifier_bytes = self.identifier_bytes.to_dict()

        extra_info_count = self.extra_info_count

        extra_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extra_info, Unset):
            extra_info = self.extra_info.to_dict()

        extra_info_map: dict[str, Any] | Unset = UNSET
        if not isinstance(self.extra_info_map, Unset):
            extra_info_map = self.extra_info_map.to_dict()

        trigger_identifier = self.trigger_identifier

        trigger_identifier_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trigger_identifier_bytes, Unset):
            trigger_identifier_bytes = self.trigger_identifier_bytes.to_dict()

        trigger_name = self.trigger_name

        trigger_name_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.trigger_name_bytes, Unset):
            trigger_name_bytes = self.trigger_name_bytes.to_dict()

        impersonate_username = self.impersonate_username

        impersonate_username_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.impersonate_username_bytes, Unset):
            impersonate_username_bytes = self.impersonate_username_bytes.to_dict()

        impersonate_email = self.impersonate_email

        impersonate_email_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.impersonate_email_bytes, Unset):
            impersonate_email_bytes = self.impersonate_email_bytes.to_dict()

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
        if uuid_bytes is not UNSET:
            field_dict["uuidBytes"] = uuid_bytes
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if identifier_bytes is not UNSET:
            field_dict["identifierBytes"] = identifier_bytes
        if extra_info_count is not UNSET:
            field_dict["extraInfoCount"] = extra_info_count
        if extra_info is not UNSET:
            field_dict["extraInfo"] = extra_info
        if extra_info_map is not UNSET:
            field_dict["extraInfoMap"] = extra_info_map
        if trigger_identifier is not UNSET:
            field_dict["triggerIdentifier"] = trigger_identifier
        if trigger_identifier_bytes is not UNSET:
            field_dict["triggerIdentifierBytes"] = trigger_identifier_bytes
        if trigger_name is not UNSET:
            field_dict["triggerName"] = trigger_name
        if trigger_name_bytes is not UNSET:
            field_dict["triggerNameBytes"] = trigger_name_bytes
        if impersonate_username is not UNSET:
            field_dict["impersonateUsername"] = impersonate_username
        if impersonate_username_bytes is not UNSET:
            field_dict["impersonateUsernameBytes"] = impersonate_username_bytes
        if impersonate_email is not UNSET:
            field_dict["impersonateEmail"] = impersonate_email
        if impersonate_email_bytes is not UNSET:
            field_dict["impersonateEmailBytes"] = impersonate_email_bytes
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
        from ..models.parser_triggered_by import ParserTriggeredBy
        from ..models.triggered_by_all_fields import TriggeredByAllFields
        from ..models.triggered_by_extra_info import TriggeredByExtraInfo
        from ..models.triggered_by_extra_info_map import TriggeredByExtraInfoMap
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        initialized = d.pop("initialized", UNSET)

        identifier = d.pop("identifier", UNSET)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: TriggeredBy | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = TriggeredBy.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserTriggeredBy | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserTriggeredBy.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _uuid_bytes = d.pop("uuidBytes", UNSET)
        uuid_bytes: ByteString | Unset
        if isinstance(_uuid_bytes, Unset):
            uuid_bytes = UNSET
        else:
            uuid_bytes = ByteString.from_dict(_uuid_bytes)

        uuid = d.pop("uuid", UNSET)

        _identifier_bytes = d.pop("identifierBytes", UNSET)
        identifier_bytes: ByteString | Unset
        if isinstance(_identifier_bytes, Unset):
            identifier_bytes = UNSET
        else:
            identifier_bytes = ByteString.from_dict(_identifier_bytes)

        extra_info_count = d.pop("extraInfoCount", UNSET)

        _extra_info = d.pop("extraInfo", UNSET)
        extra_info: TriggeredByExtraInfo | Unset
        if isinstance(_extra_info, Unset):
            extra_info = UNSET
        else:
            extra_info = TriggeredByExtraInfo.from_dict(_extra_info)

        _extra_info_map = d.pop("extraInfoMap", UNSET)
        extra_info_map: TriggeredByExtraInfoMap | Unset
        if isinstance(_extra_info_map, Unset):
            extra_info_map = UNSET
        else:
            extra_info_map = TriggeredByExtraInfoMap.from_dict(_extra_info_map)

        trigger_identifier = d.pop("triggerIdentifier", UNSET)

        _trigger_identifier_bytes = d.pop("triggerIdentifierBytes", UNSET)
        trigger_identifier_bytes: ByteString | Unset
        if isinstance(_trigger_identifier_bytes, Unset):
            trigger_identifier_bytes = UNSET
        else:
            trigger_identifier_bytes = ByteString.from_dict(_trigger_identifier_bytes)

        trigger_name = d.pop("triggerName", UNSET)

        _trigger_name_bytes = d.pop("triggerNameBytes", UNSET)
        trigger_name_bytes: ByteString | Unset
        if isinstance(_trigger_name_bytes, Unset):
            trigger_name_bytes = UNSET
        else:
            trigger_name_bytes = ByteString.from_dict(_trigger_name_bytes)

        impersonate_username = d.pop("impersonateUsername", UNSET)

        _impersonate_username_bytes = d.pop("impersonateUsernameBytes", UNSET)
        impersonate_username_bytes: ByteString | Unset
        if isinstance(_impersonate_username_bytes, Unset):
            impersonate_username_bytes = UNSET
        else:
            impersonate_username_bytes = ByteString.from_dict(_impersonate_username_bytes)

        impersonate_email = d.pop("impersonateEmail", UNSET)

        _impersonate_email_bytes = d.pop("impersonateEmailBytes", UNSET)
        impersonate_email_bytes: ByteString | Unset
        if isinstance(_impersonate_email_bytes, Unset):
            impersonate_email_bytes = UNSET
        else:
            impersonate_email_bytes = ByteString.from_dict(_impersonate_email_bytes)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: TriggeredByAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = TriggeredByAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        triggered_by = cls(
            unknown_fields=unknown_fields,
            initialized=initialized,
            identifier=identifier,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            uuid_bytes=uuid_bytes,
            uuid=uuid,
            identifier_bytes=identifier_bytes,
            extra_info_count=extra_info_count,
            extra_info=extra_info,
            extra_info_map=extra_info_map,
            trigger_identifier=trigger_identifier,
            trigger_identifier_bytes=trigger_identifier_bytes,
            trigger_name=trigger_name,
            trigger_name_bytes=trigger_name_bytes,
            impersonate_username=impersonate_username,
            impersonate_username_bytes=impersonate_username_bytes,
            impersonate_email=impersonate_email,
            impersonate_email_bytes=impersonate_email_bytes,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        triggered_by.additional_properties = d
        return triggered_by

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
