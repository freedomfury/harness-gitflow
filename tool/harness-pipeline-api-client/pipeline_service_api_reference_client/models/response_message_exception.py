from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.response_message_exception_stack_trace_item import ResponseMessageExceptionStackTraceItem
    from ..models.response_message_exception_suppressed_item import ResponseMessageExceptionSuppressedItem


T = TypeVar("T", bound="ResponseMessageException")


@_attrs_define
class ResponseMessageException:
    """
    Attributes:
        stack_trace (list[ResponseMessageExceptionStackTraceItem] | Unset):
        message (str | Unset):
        suppressed (list[ResponseMessageExceptionSuppressedItem] | Unset):
        localized_message (str | Unset):
    """

    stack_trace: list[ResponseMessageExceptionStackTraceItem] | Unset = UNSET
    message: str | Unset = UNSET
    suppressed: list[ResponseMessageExceptionSuppressedItem] | Unset = UNSET
    localized_message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        stack_trace: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.stack_trace, Unset):
            stack_trace = []
            for stack_trace_item_data in self.stack_trace:
                stack_trace_item = stack_trace_item_data.to_dict()
                stack_trace.append(stack_trace_item)

        message = self.message

        suppressed: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.suppressed, Unset):
            suppressed = []
            for suppressed_item_data in self.suppressed:
                suppressed_item = suppressed_item_data.to_dict()
                suppressed.append(suppressed_item)

        localized_message = self.localized_message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if stack_trace is not UNSET:
            field_dict["stackTrace"] = stack_trace
        if message is not UNSET:
            field_dict["message"] = message
        if suppressed is not UNSET:
            field_dict["suppressed"] = suppressed
        if localized_message is not UNSET:
            field_dict["localizedMessage"] = localized_message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.response_message_exception_stack_trace_item import ResponseMessageExceptionStackTraceItem
        from ..models.response_message_exception_suppressed_item import ResponseMessageExceptionSuppressedItem

        d = dict(src_dict)
        _stack_trace = d.pop("stackTrace", UNSET)
        stack_trace: list[ResponseMessageExceptionStackTraceItem] | Unset = UNSET
        if _stack_trace is not UNSET:
            stack_trace = []
            for stack_trace_item_data in _stack_trace:
                stack_trace_item = ResponseMessageExceptionStackTraceItem.from_dict(stack_trace_item_data)

                stack_trace.append(stack_trace_item)

        message = d.pop("message", UNSET)

        _suppressed = d.pop("suppressed", UNSET)
        suppressed: list[ResponseMessageExceptionSuppressedItem] | Unset = UNSET
        if _suppressed is not UNSET:
            suppressed = []
            for suppressed_item_data in _suppressed:
                suppressed_item = ResponseMessageExceptionSuppressedItem.from_dict(suppressed_item_data)

                suppressed.append(suppressed_item)

        localized_message = d.pop("localizedMessage", UNSET)

        response_message_exception = cls(
            stack_trace=stack_trace,
            message=message,
            suppressed=suppressed,
            localized_message=localized_message,
        )

        response_message_exception.additional_properties = d
        return response_message_exception

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
