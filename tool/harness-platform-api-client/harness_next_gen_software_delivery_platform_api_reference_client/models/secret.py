from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.secret_type import SecretType, check_secret_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.secret_spec import SecretSpec
    from ..models.secret_tags import SecretTags


T = TypeVar("T", bound="Secret")


@_attrs_define
class Secret:
    """This is details of the secret entity defined in Harness.

    Attributes:
        type_ (SecretType): This specifies the type of secret
        name (str): Name of the Secret
        identifier (str): Identifier of the Secret
        spec (SecretSpec): This has details of the Secret defined in Harness.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        tags (SecretTags | Unset): Tags
        description (str | Unset): Description of the Secret
    """

    type_: SecretType
    name: str
    identifier: str
    spec: SecretSpec
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    tags: SecretTags | Unset = UNSET
    description: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        name = self.name

        identifier = self.identifier

        spec = self.spec.to_dict()

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        description = self.description

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "name": name,
                "identifier": identifier,
                "spec": spec,
            }
        )
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if tags is not UNSET:
            field_dict["tags"] = tags
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.secret_spec import SecretSpec
        from ..models.secret_tags import SecretTags

        d = dict(src_dict)
        type_ = check_secret_type(d.pop("type"))

        name = d.pop("name")

        identifier = d.pop("identifier")

        spec = SecretSpec.from_dict(d.pop("spec"))

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: SecretTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = SecretTags.from_dict(_tags)

        description = d.pop("description", UNSET)

        secret = cls(
            type_=type_,
            name=name,
            identifier=identifier,
            spec=spec,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            tags=tags,
            description=description,
        )

        secret.additional_properties = d
        return secret

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
