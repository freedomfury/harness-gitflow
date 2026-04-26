from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PullreqSuggestionReference")


@_attrs_define
class PullreqSuggestionReference:
    """
    Attributes:
        check_sum (str | Unset):
        comment_id (int | Unset):
    """

    check_sum: str | Unset = UNSET
    comment_id: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        check_sum = self.check_sum

        comment_id = self.comment_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check_sum is not UNSET:
            field_dict["check_sum"] = check_sum
        if comment_id is not UNSET:
            field_dict["comment_id"] = comment_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        check_sum = d.pop("check_sum", UNSET)

        comment_id = d.pop("comment_id", UNSET)

        pullreq_suggestion_reference = cls(
            check_sum=check_sum,
            comment_id=comment_id,
        )

        pullreq_suggestion_reference.additional_properties = d
        return pullreq_suggestion_reference

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
