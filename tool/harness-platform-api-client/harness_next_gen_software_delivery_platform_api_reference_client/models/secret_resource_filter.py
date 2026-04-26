from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.secret_resource_filter_secret_types_item import (
    SecretResourceFilterSecretTypesItem,
    check_secret_resource_filter_secret_types_item,
)
from ..models.secret_resource_filter_source_category import (
    SecretResourceFilterSourceCategory,
    check_secret_resource_filter_source_category,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="SecretResourceFilter")


@_attrs_define
class SecretResourceFilter:
    """This has the filter information for the Secret in Harness.

    Attributes:
        identifiers (list[str] | Unset): This is the list of Entity Identifiers on which the filter will be applied.
        search_term (str | Unset): Text to search/filter the Entity.
        secret_types (list[SecretResourceFilterSecretTypesItem] | Unset): This is the list of the ENTITY types on which
            the filter will be applied.
        source_category (SecretResourceFilterSourceCategory | Unset): Specifies the connector category.
        include_secrets_from_every_sub_scope (bool | Unset): This is true if secrets are filtered at each subsequent
            scope.
        include_all_secrets_accessible_at_scope (bool | Unset): This is true if secrets are filtered from all super
            scopes.
    """

    identifiers: list[str] | Unset = UNSET
    search_term: str | Unset = UNSET
    secret_types: list[SecretResourceFilterSecretTypesItem] | Unset = UNSET
    source_category: SecretResourceFilterSourceCategory | Unset = UNSET
    include_secrets_from_every_sub_scope: bool | Unset = UNSET
    include_all_secrets_accessible_at_scope: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifiers: list[str] | Unset = UNSET
        if not isinstance(self.identifiers, Unset):
            identifiers = self.identifiers

        search_term = self.search_term

        secret_types: list[str] | Unset = UNSET
        if not isinstance(self.secret_types, Unset):
            secret_types = []
            for secret_types_item_data in self.secret_types:
                secret_types_item: str = secret_types_item_data
                secret_types.append(secret_types_item)

        source_category: str | Unset = UNSET
        if not isinstance(self.source_category, Unset):
            source_category = self.source_category

        include_secrets_from_every_sub_scope = self.include_secrets_from_every_sub_scope

        include_all_secrets_accessible_at_scope = self.include_all_secrets_accessible_at_scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if search_term is not UNSET:
            field_dict["searchTerm"] = search_term
        if secret_types is not UNSET:
            field_dict["secretTypes"] = secret_types
        if source_category is not UNSET:
            field_dict["sourceCategory"] = source_category
        if include_secrets_from_every_sub_scope is not UNSET:
            field_dict["includeSecretsFromEverySubScope"] = include_secrets_from_every_sub_scope
        if include_all_secrets_accessible_at_scope is not UNSET:
            field_dict["includeAllSecretsAccessibleAtScope"] = include_all_secrets_accessible_at_scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifiers = cast(list[str], d.pop("identifiers", UNSET))

        search_term = d.pop("searchTerm", UNSET)

        _secret_types = d.pop("secretTypes", UNSET)
        secret_types: list[SecretResourceFilterSecretTypesItem] | Unset = UNSET
        if _secret_types is not UNSET:
            secret_types = []
            for secret_types_item_data in _secret_types:
                secret_types_item = check_secret_resource_filter_secret_types_item(secret_types_item_data)

                secret_types.append(secret_types_item)

        _source_category = d.pop("sourceCategory", UNSET)
        source_category: SecretResourceFilterSourceCategory | Unset
        if isinstance(_source_category, Unset):
            source_category = UNSET
        else:
            source_category = check_secret_resource_filter_source_category(_source_category)

        include_secrets_from_every_sub_scope = d.pop("includeSecretsFromEverySubScope", UNSET)

        include_all_secrets_accessible_at_scope = d.pop("includeAllSecretsAccessibleAtScope", UNSET)

        secret_resource_filter = cls(
            identifiers=identifiers,
            search_term=search_term,
            secret_types=secret_types,
            source_category=source_category,
            include_secrets_from_every_sub_scope=include_secrets_from_every_sub_scope,
            include_all_secrets_accessible_at_scope=include_all_secrets_accessible_at_scope,
        )

        secret_resource_filter.additional_properties = d
        return secret_resource_filter

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
