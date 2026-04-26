from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.error_code import ErrorCode, check_error_code
from ..models.error_status import ErrorStatus, check_error_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.error_metadata import ErrorMetadata
    from ..models.response_message import ResponseMessage


T = TypeVar("T", bound="Error")


@_attrs_define
class Error:
    """This is Error entity as defined in Harness

    Attributes:
        status (ErrorStatus | Unset):
        code (ErrorCode | Unset):
        message (str | Unset):
        correlation_id (str | Unset):
        detailed_message (str | Unset):
        response_messages (list[ResponseMessage] | Unset):
        metadata (ErrorMetadata | Unset): This implements different error meta data objects
    """

    status: ErrorStatus | Unset = UNSET
    code: ErrorCode | Unset = UNSET
    message: str | Unset = UNSET
    correlation_id: str | Unset = UNSET
    detailed_message: str | Unset = UNSET
    response_messages: list[ResponseMessage] | Unset = UNSET
    metadata: ErrorMetadata | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        code: str | Unset = UNSET
        if not isinstance(self.code, Unset):
            code = self.code

        message = self.message

        correlation_id = self.correlation_id

        detailed_message = self.detailed_message

        response_messages: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.response_messages, Unset):
            response_messages = []
            for response_messages_item_data in self.response_messages:
                response_messages_item = response_messages_item_data.to_dict()
                response_messages.append(response_messages_item)

        metadata: dict[str, Any] | Unset = UNSET
        if not isinstance(self.metadata, Unset):
            metadata = self.metadata.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if status is not UNSET:
            field_dict["status"] = status
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if correlation_id is not UNSET:
            field_dict["correlationId"] = correlation_id
        if detailed_message is not UNSET:
            field_dict["detailedMessage"] = detailed_message
        if response_messages is not UNSET:
            field_dict["responseMessages"] = response_messages
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.error_metadata import ErrorMetadata
        from ..models.response_message import ResponseMessage

        d = dict(src_dict)
        _status = d.pop("status", UNSET)
        status: ErrorStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_error_status(_status)

        _code = d.pop("code", UNSET)
        code: ErrorCode | Unset
        if isinstance(_code, Unset):
            code = UNSET
        else:
            code = check_error_code(_code)

        message = d.pop("message", UNSET)

        correlation_id = d.pop("correlationId", UNSET)

        detailed_message = d.pop("detailedMessage", UNSET)

        _response_messages = d.pop("responseMessages", UNSET)
        response_messages: list[ResponseMessage] | Unset = UNSET
        if _response_messages is not UNSET:
            response_messages = []
            for response_messages_item_data in _response_messages:
                response_messages_item = ResponseMessage.from_dict(response_messages_item_data)

                response_messages.append(response_messages_item)

        _metadata = d.pop("metadata", UNSET)
        metadata: ErrorMetadata | Unset
        if isinstance(_metadata, Unset):
            metadata = UNSET
        else:
            metadata = ErrorMetadata.from_dict(_metadata)

        error = cls(
            status=status,
            code=code,
            message=message,
            correlation_id=correlation_id,
            detailed_message=detailed_message,
            response_messages=response_messages,
            metadata=metadata,
        )

        error.additional_properties = d
        return error

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
