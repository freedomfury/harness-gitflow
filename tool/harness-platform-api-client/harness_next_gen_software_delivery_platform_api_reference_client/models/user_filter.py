from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_filter_parent_filter import UserFilterParentFilter, check_user_filter_parent_filter
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserFilter")


@_attrs_define
class UserFilter:
    """
    Attributes:
        search_term (str | Unset): This string will be used to filter the results. Details of all the users having this
            string in their name or email address will be filtered.
        identifiers (list[str] | Unset): Filter by User Identifiers
        emails (list[str] | Unset): Filter by User Emails
        parent_filter (UserFilterParentFilter | Unset):
    """

    search_term: str | Unset = UNSET
    identifiers: list[str] | Unset = UNSET
    emails: list[str] | Unset = UNSET
    parent_filter: UserFilterParentFilter | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        search_term = self.search_term

        identifiers: list[str] | Unset = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = self.identifiers

        emails: list[str] | Unset = UNSET
        if not isinstance(self.emails, Unset):
            emails = self.emails

        parent_filter: str | Unset = UNSET
        if not isinstance(self.parent_filter, Unset):
            parent_filter = self.parent_filter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if search_term is not UNSET:
            field_dict["searchTerm"] = search_term
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if emails is not UNSET:
            field_dict["emails"] = emails
        if parent_filter is not UNSET:
            field_dict["parentFilter"] = parent_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        search_term = d.pop("searchTerm", UNSET)

        identifiers = cast(list[str], d.pop("identifiers", UNSET))

        emails = cast(list[str], d.pop("emails", UNSET))

        _parent_filter = d.pop("parentFilter", UNSET)
        parent_filter: UserFilterParentFilter | Unset
        if isinstance(_parent_filter, Unset):
            parent_filter = UNSET
        else:
            parent_filter = check_user_filter_parent_filter(_parent_filter)

        user_filter = cls(
            search_term=search_term,
            identifiers=identifiers,
            emails=emails,
            parent_filter=parent_filter,
        )

        user_filter.additional_properties = d
        return user_filter

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
