from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.child_executable_response_or_builder_all_fields import ChildExecutableResponseOrBuilderAllFields
    from ..models.descriptor import Descriptor
    from ..models.message import Message
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="ChildExecutableResponseOrBuilder")


@_attrs_define
class ChildExecutableResponseOrBuilder:
    """
    Attributes:
        units_list (list[str] | Unset):
        units_count (int | Unset):
        log_keys_count (int | Unset):
        log_keys_list (list[str] | Unset):
        child_node_id_bytes (ByteString | Unset):
        child_node_id (str | Unset):
        skip (bool | Unset):
        all_fields (ChildExecutableResponseOrBuilderAllFields | Unset):
        default_instance_for_type (Message | Unset):
        unknown_fields (UnknownFieldSet | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        initialized (bool | Unset):
    """

    units_list: list[str] | Unset = UNSET
    units_count: int | Unset = UNSET
    log_keys_count: int | Unset = UNSET
    log_keys_list: list[str] | Unset = UNSET
    child_node_id_bytes: ByteString | Unset = UNSET
    child_node_id: str | Unset = UNSET
    skip: bool | Unset = UNSET
    all_fields: ChildExecutableResponseOrBuilderAllFields | Unset = UNSET
    default_instance_for_type: Message | Unset = UNSET
    unknown_fields: UnknownFieldSet | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    initialized: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        units_list: list[str] | Unset = UNSET
        if not isinstance(self.units_list, Unset):
            units_list = self.units_list

        units_count = self.units_count

        log_keys_count = self.log_keys_count

        log_keys_list: list[str] | Unset = UNSET
        if not isinstance(self.log_keys_list, Unset):
            log_keys_list = self.log_keys_list

        child_node_id_bytes: dict[str, Any] | Unset = UNSET
        if not isinstance(self.child_node_id_bytes, Unset):
            child_node_id_bytes = self.child_node_id_bytes.to_dict()

        child_node_id = self.child_node_id

        skip = self.skip

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
        if units_list is not UNSET:
            field_dict["unitsList"] = units_list
        if units_count is not UNSET:
            field_dict["unitsCount"] = units_count
        if log_keys_count is not UNSET:
            field_dict["logKeysCount"] = log_keys_count
        if log_keys_list is not UNSET:
            field_dict["logKeysList"] = log_keys_list
        if child_node_id_bytes is not UNSET:
            field_dict["childNodeIdBytes"] = child_node_id_bytes
        if child_node_id is not UNSET:
            field_dict["childNodeId"] = child_node_id
        if skip is not UNSET:
            field_dict["skip"] = skip
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
        from ..models.child_executable_response_or_builder_all_fields import ChildExecutableResponseOrBuilderAllFields
        from ..models.descriptor import Descriptor
        from ..models.message import Message
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        units_list = cast(list[str], d.pop("unitsList", UNSET))

        units_count = d.pop("unitsCount", UNSET)

        log_keys_count = d.pop("logKeysCount", UNSET)

        log_keys_list = cast(list[str], d.pop("logKeysList", UNSET))

        _child_node_id_bytes = d.pop("childNodeIdBytes", UNSET)
        child_node_id_bytes: ByteString | Unset
        if isinstance(_child_node_id_bytes, Unset):
            child_node_id_bytes = UNSET
        else:
            child_node_id_bytes = ByteString.from_dict(_child_node_id_bytes)

        child_node_id = d.pop("childNodeId", UNSET)

        skip = d.pop("skip", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: ChildExecutableResponseOrBuilderAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = ChildExecutableResponseOrBuilderAllFields.from_dict(_all_fields)

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

        child_executable_response_or_builder = cls(
            units_list=units_list,
            units_count=units_count,
            log_keys_count=log_keys_count,
            log_keys_list=log_keys_list,
            child_node_id_bytes=child_node_id_bytes,
            child_node_id=child_node_id,
            skip=skip,
            all_fields=all_fields,
            default_instance_for_type=default_instance_for_type,
            unknown_fields=unknown_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            initialized=initialized,
        )

        child_executable_response_or_builder.additional_properties = d
        return child_executable_response_or_builder

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
