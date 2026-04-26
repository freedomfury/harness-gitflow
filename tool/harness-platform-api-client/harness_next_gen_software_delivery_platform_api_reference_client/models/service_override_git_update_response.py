from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.service_override_git_update_response_type import (
    ServiceOverrideGitUpdateResponseType,
    check_service_override_git_update_response_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="ServiceOverrideGitUpdateResponse")


@_attrs_define
class ServiceOverrideGitUpdateResponse:
    """Contains info about ServiceOverride that is updated.

    Attributes:
        environment_ref (str): Environment Reference for the Entity.
        type_ (ServiceOverrideGitUpdateResponseType): Type of the override which is based on source of overrides
        identifier (str | Unset): Contains the ServiceOverrideIdentifier of the successfully moved config.
        service_ref (str | Unset): Service Reference for Entity
        infra_identifier (str | Unset): infraIdentifier
    """

    environment_ref: str
    type_: ServiceOverrideGitUpdateResponseType
    identifier: str | Unset = UNSET
    service_ref: str | Unset = UNSET
    infra_identifier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        environment_ref = self.environment_ref

        type_: str = self.type_

        identifier = self.identifier

        service_ref = self.service_ref

        infra_identifier = self.infra_identifier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "environmentRef": environment_ref,
                "type": type_,
            }
        )
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if service_ref is not UNSET:
            field_dict["serviceRef"] = service_ref
        if infra_identifier is not UNSET:
            field_dict["infraIdentifier"] = infra_identifier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        environment_ref = d.pop("environmentRef")

        type_ = check_service_override_git_update_response_type(d.pop("type"))

        identifier = d.pop("identifier", UNSET)

        service_ref = d.pop("serviceRef", UNSET)

        infra_identifier = d.pop("infraIdentifier", UNSET)

        service_override_git_update_response = cls(
            environment_ref=environment_ref,
            type_=type_,
            identifier=identifier,
            service_ref=service_ref,
            infra_identifier=infra_identifier,
        )

        service_override_git_update_response.additional_properties = d
        return service_override_git_update_response

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
