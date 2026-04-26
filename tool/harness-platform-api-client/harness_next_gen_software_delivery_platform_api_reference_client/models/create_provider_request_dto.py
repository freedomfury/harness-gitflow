from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.provider_request_info import ProviderRequestInfo


T = TypeVar("T", bound="CreateProviderRequestDTO")


@_attrs_define
class CreateProviderRequestDTO:
    """
    Attributes:
        name (str | Unset): Name of the Provider Request.
        identifier (str | Unset): Identifier of the Provider Request.
        description (str | Unset): Description of the entity
        spec (ProviderRequestInfo | Unset): Spec of the Provider
    """

    name: str | Unset = UNSET
    identifier: str | Unset = UNSET
    description: str | Unset = UNSET
    spec: ProviderRequestInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        identifier = self.identifier

        description = self.description

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if description is not UNSET:
            field_dict["description"] = description
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.provider_request_info import ProviderRequestInfo

        d = dict(src_dict)
        name = d.pop("name", UNSET)

        identifier = d.pop("identifier", UNSET)

        description = d.pop("description", UNSET)

        _spec = d.pop("spec", UNSET)
        spec: ProviderRequestInfo | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = ProviderRequestInfo.from_dict(_spec)

        create_provider_request_dto = cls(
            name=name,
            identifier=identifier,
            description=description,
            spec=spec,
        )

        create_provider_request_dto.additional_properties = d
        return create_provider_request_dto

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
