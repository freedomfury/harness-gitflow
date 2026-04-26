from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CreateAnnotationsResponse")


@_attrs_define
class CreateAnnotationsResponse:
    """Response from creating/updating annotations

    Attributes:
        processed (int | Unset): Number of annotations successfully processed
        failed (int | Unset): Number of annotations that failed to process
        message (str | Unset): Error message if any
    """

    processed: int | Unset = UNSET
    failed: int | Unset = UNSET
    message: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        processed = self.processed

        failed = self.failed

        message = self.message

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if processed is not UNSET:
            field_dict["processed"] = processed
        if failed is not UNSET:
            field_dict["failed"] = failed
        if message is not UNSET:
            field_dict["message"] = message

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        processed = d.pop("processed", UNSET)

        failed = d.pop("failed", UNSET)

        message = d.pop("message", UNSET)

        create_annotations_response = cls(
            processed=processed,
            failed=failed,
            message=message,
        )

        create_annotations_response.additional_properties = d
        return create_annotations_response

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
