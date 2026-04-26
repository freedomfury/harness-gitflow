from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.freeze_summary_response import FreezeSummaryResponse


T = TypeVar("T", bound="FrozenExecutionDetail")


@_attrs_define
class FrozenExecutionDetail:
    """
    Attributes:
        freeze (FreezeSummaryResponse | Unset): This contains summary of the Freeze Response
        url (str | Unset):
    """

    freeze: FreezeSummaryResponse | Unset = UNSET
    url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        freeze: dict[str, Any] | Unset = UNSET
        if not isinstance(self.freeze, Unset):
            freeze = self.freeze.to_dict()

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if freeze is not UNSET:
            field_dict["freeze"] = freeze
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.freeze_summary_response import FreezeSummaryResponse

        d = dict(src_dict)
        _freeze = d.pop("freeze", UNSET)
        freeze: FreezeSummaryResponse | Unset
        if isinstance(_freeze, Unset):
            freeze = UNSET
        else:
            freeze = FreezeSummaryResponse.from_dict(_freeze)

        url = d.pop("url", UNSET)

        frozen_execution_detail = cls(
            freeze=freeze,
            url=url,
        )

        frozen_execution_detail.additional_properties = d
        return frozen_execution_detail

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
