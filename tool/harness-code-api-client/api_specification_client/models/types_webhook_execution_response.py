from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypesWebhookExecutionResponse")


@_attrs_define
class TypesWebhookExecutionResponse:
    """
    Attributes:
        body (str | Unset):
        headers (str | Unset):
        status (str | Unset):
        status_code (int | Unset):
    """

    body: str | Unset = UNSET
    headers: str | Unset = UNSET
    status: str | Unset = UNSET
    status_code: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        body = self.body

        headers = self.headers

        status = self.status

        status_code = self.status_code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if body is not UNSET:
            field_dict["body"] = body
        if headers is not UNSET:
            field_dict["headers"] = headers
        if status is not UNSET:
            field_dict["status"] = status
        if status_code is not UNSET:
            field_dict["status_code"] = status_code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        body = d.pop("body", UNSET)

        headers = d.pop("headers", UNSET)

        status = d.pop("status", UNSET)

        status_code = d.pop("status_code", UNSET)

        types_webhook_execution_response = cls(
            body=body,
            headers=headers,
            status=status,
            status_code=status_code,
        )

        types_webhook_execution_response.additional_properties = d
        return types_webhook_execution_response

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
