from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.connector_info_type import ConnectorInfoType, check_connector_info_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.connector_config import ConnectorConfig
    from ..models.connector_info_tags import ConnectorInfoTags


T = TypeVar("T", bound="ConnectorInfo")


@_attrs_define
class ConnectorInfo:
    """This has the Connector details defined in Harness

    Attributes:
        name (str): Name of the Connector.
        identifier (str): Identifier of the Connector.
        type_ (ConnectorInfoType): Type of the Connector.
        spec (ConnectorConfig): This is the view of the ConnectorConfig entity defined in Harness
        description (str | Unset): Description of the entity
        account_identifier (str | Unset): Account Identifier for the Entity.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        tags (ConnectorInfoTags | Unset): Tags
    """

    name: str
    identifier: str
    type_: ConnectorInfoType
    spec: ConnectorConfig
    description: str | Unset = UNSET
    account_identifier: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    tags: ConnectorInfoTags | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        identifier = self.identifier

        type_: str = self.type_

        spec = self.spec.to_dict()

        description = self.description

        account_identifier = self.account_identifier

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
                "identifier": identifier,
                "type": type_,
                "spec": spec,
            }
        )
        if description is not UNSET:
            field_dict["description"] = description
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if tags is not UNSET:
            field_dict["tags"] = tags

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.connector_config import ConnectorConfig
        from ..models.connector_info_tags import ConnectorInfoTags

        d = dict(src_dict)
        name = d.pop("name")

        identifier = d.pop("identifier")

        type_ = check_connector_info_type(d.pop("type"))

        spec = ConnectorConfig.from_dict(d.pop("spec"))

        description = d.pop("description", UNSET)

        account_identifier = d.pop("accountIdentifier", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: ConnectorInfoTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = ConnectorInfoTags.from_dict(_tags)

        connector_info = cls(
            name=name,
            identifier=identifier,
            type_=type_,
            spec=spec,
            description=description,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            tags=tags,
        )

        connector_info.additional_properties = d
        return connector_info

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
