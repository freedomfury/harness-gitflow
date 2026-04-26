from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.user_group_filter_filter_type import UserGroupFilterFilterType, check_user_group_filter_filter_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="UserGroupFilter")


@_attrs_define
class UserGroupFilter:
    """This is the view of the UserGroupFilter entity defined in Harness

    Attributes:
        account_identifier (str): Filter by account using account identifier
        database_id_filter (list[str] | Unset): Filter by the internal database ids of user group
        identifier_filter (list[str] | Unset): Filter by the user group identifier
        user_identifier_filter (list[str] | Unset): Filter by the users present in the user group
        org_identifier (str | Unset): Filter by organization using account identifier
        project_identifier (str | Unset): Filter by project using account identifier
        search_term (str | Unset): Filter by search term matching entities by name/identifier
        filter_type (UserGroupFilterFilterType | Unset): Filter by user group filterType
    """

    account_identifier: str
    database_id_filter: list[str] | Unset = UNSET
    identifier_filter: list[str] | Unset = UNSET
    user_identifier_filter: list[str] | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    search_term: str | Unset = UNSET
    filter_type: UserGroupFilterFilterType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_identifier = self.account_identifier

        database_id_filter: list[str] | Unset = UNSET
        if not isinstance(self.database_id_filter, Unset):
            database_id_filter = self.database_id_filter

        identifier_filter: list[str] | Unset = UNSET
        if not isinstance(self.identifier_filter, Unset):
            identifier_filter = self.identifier_filter

        user_identifier_filter: list[str] | Unset = UNSET
        if not isinstance(self.user_identifier_filter, Unset):
            user_identifier_filter = self.user_identifier_filter

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        search_term = self.search_term

        filter_type: str | Unset = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountIdentifier": account_identifier,
            }
        )
        if database_id_filter is not UNSET:
            field_dict["databaseIdFilter"] = database_id_filter
        if identifier_filter is not UNSET:
            field_dict["identifierFilter"] = identifier_filter
        if user_identifier_filter is not UNSET:
            field_dict["userIdentifierFilter"] = user_identifier_filter
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if search_term is not UNSET:
            field_dict["searchTerm"] = search_term
        if filter_type is not UNSET:
            field_dict["filterType"] = filter_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        account_identifier = d.pop("accountIdentifier")

        database_id_filter = cast(list[str], d.pop("databaseIdFilter", UNSET))

        identifier_filter = cast(list[str], d.pop("identifierFilter", UNSET))

        user_identifier_filter = cast(list[str], d.pop("userIdentifierFilter", UNSET))

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        search_term = d.pop("searchTerm", UNSET)

        _filter_type = d.pop("filterType", UNSET)
        filter_type: UserGroupFilterFilterType | Unset
        if isinstance(_filter_type, Unset):
            filter_type = UNSET
        else:
            filter_type = check_user_group_filter_filter_type(_filter_type)

        user_group_filter = cls(
            account_identifier=account_identifier,
            database_id_filter=database_id_filter,
            identifier_filter=identifier_filter,
            user_identifier_filter=user_identifier_filter,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            search_term=search_term,
            filter_type=filter_type,
        )

        user_group_filter.additional_properties = d
        return user_group_filter

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
