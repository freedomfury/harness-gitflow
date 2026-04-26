from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.importer_connector_def import ImporterConnectorDef


T = TypeVar("T", bound="LinkedCreateBody")


@_attrs_define
class LinkedCreateBody:
    """
    Attributes:
        connector (ImporterConnectorDef | Unset):
        description (str | Unset):
        identifier (str | Unset):
        is_public (bool | Unset):
        parent_ref (str | Unset):
    """

    connector: ImporterConnectorDef | Unset = UNSET
    description: str | Unset = UNSET
    identifier: str | Unset = UNSET
    is_public: bool | Unset = UNSET
    parent_ref: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector: dict[str, Any] | Unset = UNSET
        if not isinstance(self.connector, Unset):
            connector = self.connector.to_dict()

        description = self.description

        identifier = self.identifier

        is_public = self.is_public

        parent_ref = self.parent_ref

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if connector is not UNSET:
            field_dict["connector"] = connector
        if description is not UNSET:
            field_dict["description"] = description
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if is_public is not UNSET:
            field_dict["is_public"] = is_public
        if parent_ref is not UNSET:
            field_dict["parent_ref"] = parent_ref

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.importer_connector_def import ImporterConnectorDef

        d = dict(src_dict)
        _connector = d.pop("connector", UNSET)
        connector: ImporterConnectorDef | Unset
        if isinstance(_connector, Unset):
            connector = UNSET
        else:
            connector = ImporterConnectorDef.from_dict(_connector)

        description = d.pop("description", UNSET)

        identifier = d.pop("identifier", UNSET)

        is_public = d.pop("is_public", UNSET)

        parent_ref = d.pop("parent_ref", UNSET)

        linked_create_body = cls(
            connector=connector,
            description=description,
            identifier=identifier,
            is_public=is_public,
            parent_ref=parent_ref,
        )

        linked_create_body.additional_properties = d
        return linked_create_body

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
