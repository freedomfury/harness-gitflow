from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RetryStagesMetadata")


@_attrs_define
class RetryStagesMetadata:
    """This has lists of retried and skipped stage identifiers

    Attributes:
        retry_stages_identifier (list[str] | Unset):
        skip_stages_identifier (list[str] | Unset):
    """

    retry_stages_identifier: list[str] | Unset = UNSET
    skip_stages_identifier: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        retry_stages_identifier: list[str] | Unset = UNSET
        if not isinstance(self.retry_stages_identifier, Unset):
            retry_stages_identifier = self.retry_stages_identifier

        skip_stages_identifier: list[str] | Unset = UNSET
        if not isinstance(self.skip_stages_identifier, Unset):
            skip_stages_identifier = self.skip_stages_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if retry_stages_identifier is not UNSET:
            field_dict["retryStagesIdentifier"] = retry_stages_identifier
        if skip_stages_identifier is not UNSET:
            field_dict["skipStagesIdentifier"] = skip_stages_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        retry_stages_identifier = cast(list[str], d.pop("retryStagesIdentifier", UNSET))

        skip_stages_identifier = cast(list[str], d.pop("skipStagesIdentifier", UNSET))

        retry_stages_metadata = cls(
            retry_stages_identifier=retry_stages_identifier,
            skip_stages_identifier=skip_stages_identifier,
        )

        retry_stages_metadata.additional_properties = d
        return retry_stages_metadata

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
