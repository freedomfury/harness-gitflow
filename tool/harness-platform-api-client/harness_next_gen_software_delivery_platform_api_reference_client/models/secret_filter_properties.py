from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.secret_filter_properties_filter_type import (
    SecretFilterPropertiesFilterType,
    check_secret_filter_properties_filter_type,
)
from ..models.secret_filter_properties_secret_types_item import (
    SecretFilterPropertiesSecretTypesItem,
    check_secret_filter_properties_secret_types_item,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.secret_filter_properties_tags import SecretFilterPropertiesTags


T = TypeVar("T", bound="SecretFilterProperties")


@_attrs_define
class SecretFilterProperties:
    """Properties of the Secret Filter defined in Harness

    Attributes:
        secret_name (str | Unset): This is the secret name on which the filter will be applied.
        secret_identifier (str | Unset): This is the secret identifier on which the filter will be applied.
        secret_types (list[SecretFilterPropertiesSecretTypesItem] | Unset): This is the list of the ENTITY types on
            which the filter will be applied.
        secret_manager_identifiers (list[str] | Unset): secretManagerIdentifiers
        description (str | Unset): Description of filter created.
        search_term (str | Unset): Text to search/filter the Entity.
        tags (SecretFilterPropertiesTags | Unset): Filter tags as a key-value pair.
        filter_type (SecretFilterPropertiesFilterType | Unset):
    """

    secret_name: str | Unset = UNSET
    secret_identifier: str | Unset = UNSET
    secret_types: list[SecretFilterPropertiesSecretTypesItem] | Unset = UNSET
    secret_manager_identifiers: list[str] | Unset = UNSET
    description: str | Unset = UNSET
    search_term: str | Unset = UNSET
    tags: SecretFilterPropertiesTags | Unset = UNSET
    filter_type: SecretFilterPropertiesFilterType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        secret_name = self.secret_name

        secret_identifier = self.secret_identifier

        secret_types: list[str] | Unset = UNSET
        if not isinstance(self.secret_types, Unset):
            secret_types = []
            for secret_types_item_data in self.secret_types:
                secret_types_item: str = secret_types_item_data
                secret_types.append(secret_types_item)

        secret_manager_identifiers: list[str] | Unset = UNSET
        if not isinstance(self.secret_manager_identifiers, Unset):
            secret_manager_identifiers = self.secret_manager_identifiers

        description = self.description

        search_term = self.search_term

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        filter_type: str | Unset = UNSET
        if not isinstance(self.filter_type, Unset):
            filter_type = self.filter_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if secret_name is not UNSET:
            field_dict["secretName"] = secret_name
        if secret_identifier is not UNSET:
            field_dict["secretIdentifier"] = secret_identifier
        if secret_types is not UNSET:
            field_dict["secretTypes"] = secret_types
        if secret_manager_identifiers is not UNSET:
            field_dict["secretManagerIdentifiers"] = secret_manager_identifiers
        if description is not UNSET:
            field_dict["description"] = description
        if search_term is not UNSET:
            field_dict["searchTerm"] = search_term
        if tags is not UNSET:
            field_dict["tags"] = tags
        if filter_type is not UNSET:
            field_dict["filterType"] = filter_type

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.secret_filter_properties_tags import SecretFilterPropertiesTags

        d = dict(src_dict)
        secret_name = d.pop("secretName", UNSET)

        secret_identifier = d.pop("secretIdentifier", UNSET)

        _secret_types = d.pop("secretTypes", UNSET)
        secret_types: list[SecretFilterPropertiesSecretTypesItem] | Unset = UNSET
        if _secret_types is not UNSET:
            secret_types = []
            for secret_types_item_data in _secret_types:
                secret_types_item = check_secret_filter_properties_secret_types_item(secret_types_item_data)

                secret_types.append(secret_types_item)

        secret_manager_identifiers = cast(list[str], d.pop("secretManagerIdentifiers", UNSET))

        description = d.pop("description", UNSET)

        search_term = d.pop("searchTerm", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: SecretFilterPropertiesTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = SecretFilterPropertiesTags.from_dict(_tags)

        _filter_type = d.pop("filterType", UNSET)
        filter_type: SecretFilterPropertiesFilterType | Unset
        if isinstance(_filter_type, Unset):
            filter_type = UNSET
        else:
            filter_type = check_secret_filter_properties_filter_type(_filter_type)

        secret_filter_properties = cls(
            secret_name=secret_name,
            secret_identifier=secret_identifier,
            secret_types=secret_types,
            secret_manager_identifiers=secret_manager_identifiers,
            description=description,
            search_term=search_term,
            tags=tags,
            filter_type=filter_type,
        )

        secret_filter_properties.additional_properties = d
        return secret_filter_properties

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
