from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.facilitator_executable_response_status import (
    FacilitatorExecutableResponseStatus,
    check_facilitator_executable_response_status,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.byte_string import ByteString
    from ..models.descriptor import Descriptor
    from ..models.facilitator_executable_response_all_fields import FacilitatorExecutableResponseAllFields
    from ..models.parser_facilitator_executable_response import ParserFacilitatorExecutableResponse
    from ..models.unknown_field_set import UnknownFieldSet


T = TypeVar("T", bound="FacilitatorExecutableResponse")


@_attrs_define
class FacilitatorExecutableResponse:
    """
    Attributes:
        unknown_fields (UnknownFieldSet | Unset):
        callback_ids_count (int | Unset):
        type_ (str | Unset):
        initialized (bool | Unset):
        status (FacilitatorExecutableResponseStatus | Unset):
        default_instance_for_type (FacilitatorExecutableResponse | Unset):
        parser_for_type (ParserFacilitatorExecutableResponse | Unset):
        serialized_size (int | Unset):
        type_bytes (ByteString | Unset):
        status_value (int | Unset):
        start_ts (int | Unset):
        callback_ids_list (list[str] | Unset):
        timeout_in_seconds (int | Unset):
        all_fields (FacilitatorExecutableResponseAllFields | Unset):
        initialization_error_string (str | Unset):
        descriptor_for_type (Descriptor | Unset):
        memoized_serialized_size (int | Unset):
    """

    unknown_fields: UnknownFieldSet | Unset = UNSET
    callback_ids_count: int | Unset = UNSET
    type_: str | Unset = UNSET
    initialized: bool | Unset = UNSET
    status: FacilitatorExecutableResponseStatus | Unset = UNSET
    default_instance_for_type: FacilitatorExecutableResponse | Unset = UNSET
    parser_for_type: ParserFacilitatorExecutableResponse | Unset = UNSET
    serialized_size: int | Unset = UNSET
    type_bytes: ByteString | Unset = UNSET
    status_value: int | Unset = UNSET
    start_ts: int | Unset = UNSET
    callback_ids_list: list[str] | Unset = UNSET
    timeout_in_seconds: int | Unset = UNSET
    all_fields: FacilitatorExecutableResponseAllFields | Unset = UNSET
    initialization_error_string: str | Unset = UNSET
    descriptor_for_type: Descriptor | Unset = UNSET
    memoized_serialized_size: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        unknown_fields: dict[str, Any] | Unset = UNSET
        if not isinstance(self.unknown_fields, Unset):
            unknown_fields = self.unknown_fields.to_dict()

        callback_ids_count = self.callback_ids_count

        type_ = self.type_

        initialized = self.initialized

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

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

        status_value = self.status_value

        start_ts = self.start_ts

        callback_ids_list: list[str] | Unset = UNSET
        if not isinstance(self.callback_ids_list, Unset):
            callback_ids_list = self.callback_ids_list

        timeout_in_seconds = self.timeout_in_seconds

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
        if callback_ids_count is not UNSET:
            field_dict["callbackIdsCount"] = callback_ids_count
        if type_ is not UNSET:
            field_dict["type"] = type_
        if initialized is not UNSET:
            field_dict["initialized"] = initialized
        if status is not UNSET:
            field_dict["status"] = status
        if default_instance_for_type is not UNSET:
            field_dict["defaultInstanceForType"] = default_instance_for_type
        if parser_for_type is not UNSET:
            field_dict["parserForType"] = parser_for_type
        if serialized_size is not UNSET:
            field_dict["serializedSize"] = serialized_size
        if type_bytes is not UNSET:
            field_dict["typeBytes"] = type_bytes
        if status_value is not UNSET:
            field_dict["statusValue"] = status_value
        if start_ts is not UNSET:
            field_dict["startTs"] = start_ts
        if callback_ids_list is not UNSET:
            field_dict["callbackIdsList"] = callback_ids_list
        if timeout_in_seconds is not UNSET:
            field_dict["timeoutInSeconds"] = timeout_in_seconds
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
        from ..models.facilitator_executable_response_all_fields import FacilitatorExecutableResponseAllFields
        from ..models.parser_facilitator_executable_response import ParserFacilitatorExecutableResponse
        from ..models.unknown_field_set import UnknownFieldSet

        d = dict(src_dict)
        _unknown_fields = d.pop("unknownFields", UNSET)
        unknown_fields: UnknownFieldSet | Unset
        if isinstance(_unknown_fields, Unset):
            unknown_fields = UNSET
        else:
            unknown_fields = UnknownFieldSet.from_dict(_unknown_fields)

        callback_ids_count = d.pop("callbackIdsCount", UNSET)

        type_ = d.pop("type", UNSET)

        initialized = d.pop("initialized", UNSET)

        _status = d.pop("status", UNSET)
        status: FacilitatorExecutableResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_facilitator_executable_response_status(_status)

        _default_instance_for_type = d.pop("defaultInstanceForType", UNSET)
        default_instance_for_type: FacilitatorExecutableResponse | Unset
        if isinstance(_default_instance_for_type, Unset):
            default_instance_for_type = UNSET
        else:
            default_instance_for_type = FacilitatorExecutableResponse.from_dict(_default_instance_for_type)

        _parser_for_type = d.pop("parserForType", UNSET)
        parser_for_type: ParserFacilitatorExecutableResponse | Unset
        if isinstance(_parser_for_type, Unset):
            parser_for_type = UNSET
        else:
            parser_for_type = ParserFacilitatorExecutableResponse.from_dict(_parser_for_type)

        serialized_size = d.pop("serializedSize", UNSET)

        _type_bytes = d.pop("typeBytes", UNSET)
        type_bytes: ByteString | Unset
        if isinstance(_type_bytes, Unset):
            type_bytes = UNSET
        else:
            type_bytes = ByteString.from_dict(_type_bytes)

        status_value = d.pop("statusValue", UNSET)

        start_ts = d.pop("startTs", UNSET)

        callback_ids_list = cast(list[str], d.pop("callbackIdsList", UNSET))

        timeout_in_seconds = d.pop("timeoutInSeconds", UNSET)

        _all_fields = d.pop("allFields", UNSET)
        all_fields: FacilitatorExecutableResponseAllFields | Unset
        if isinstance(_all_fields, Unset):
            all_fields = UNSET
        else:
            all_fields = FacilitatorExecutableResponseAllFields.from_dict(_all_fields)

        initialization_error_string = d.pop("initializationErrorString", UNSET)

        _descriptor_for_type = d.pop("descriptorForType", UNSET)
        descriptor_for_type: Descriptor | Unset
        if isinstance(_descriptor_for_type, Unset):
            descriptor_for_type = UNSET
        else:
            descriptor_for_type = Descriptor.from_dict(_descriptor_for_type)

        memoized_serialized_size = d.pop("memoizedSerializedSize", UNSET)

        facilitator_executable_response = cls(
            unknown_fields=unknown_fields,
            callback_ids_count=callback_ids_count,
            type_=type_,
            initialized=initialized,
            status=status,
            default_instance_for_type=default_instance_for_type,
            parser_for_type=parser_for_type,
            serialized_size=serialized_size,
            type_bytes=type_bytes,
            status_value=status_value,
            start_ts=start_ts,
            callback_ids_list=callback_ids_list,
            timeout_in_seconds=timeout_in_seconds,
            all_fields=all_fields,
            initialization_error_string=initialization_error_string,
            descriptor_for_type=descriptor_for_type,
            memoized_serialized_size=memoized_serialized_size,
        )

        facilitator_executable_response.additional_properties = d
        return facilitator_executable_response

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
