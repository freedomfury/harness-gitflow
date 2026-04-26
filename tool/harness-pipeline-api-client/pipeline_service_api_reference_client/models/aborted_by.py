from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AbortedBy")


@_attrs_define
class AbortedBy:
    """This contains info of the user who aborted the pipeline

    Attributes:
        email (str | Unset): Email id of the user who aborted the pipeline
        user_name (str | Unset): User name of the user who aborted the pipeline
        created_at (int | Unset): Timestamp when user aborted the pipeline
    """

    email: str | Unset = UNSET
    user_name: str | Unset = UNSET
    created_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        user_name = self.user_name

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if email is not UNSET:
            field_dict["email"] = email
        if user_name is not UNSET:
            field_dict["userName"] = user_name
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        email = d.pop("email", UNSET)

        user_name = d.pop("userName", UNSET)

        created_at = d.pop("createdAt", UNSET)

        aborted_by = cls(
            email=email,
            user_name=user_name,
            created_at=created_at,
        )

        aborted_by.additional_properties = d
        return aborted_by

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
