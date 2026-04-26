from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.artifactory_authentication_type import (
    ArtifactoryAuthenticationType,
    check_artifactory_authentication_type,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.artifactory_auth_credentials import ArtifactoryAuthCredentials


T = TypeVar("T", bound="ArtifactoryAuthentication")


@_attrs_define
class ArtifactoryAuthentication:
    """This entity contains the details for Artifactory Authentication

    Attributes:
        type_ (ArtifactoryAuthenticationType):
        spec (ArtifactoryAuthCredentials | Unset): This entity contains the details of credentials for Artifactory
            Authentication
    """

    type_: ArtifactoryAuthenticationType
    spec: ArtifactoryAuthCredentials | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        spec: dict[str, Any] | Unset = UNSET
        if not isinstance(self.spec, Unset):
            spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
            }
        )
        if spec is not UNSET:
            field_dict["spec"] = spec

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.artifactory_auth_credentials import ArtifactoryAuthCredentials

        d = dict(src_dict)
        type_ = check_artifactory_authentication_type(d.pop("type"))

        _spec = d.pop("spec", UNSET)
        spec: ArtifactoryAuthCredentials | Unset
        if isinstance(_spec, Unset):
            spec = UNSET
        else:
            spec = ArtifactoryAuthCredentials.from_dict(_spec)

        artifactory_authentication = cls(
            type_=type_,
            spec=spec,
        )

        artifactory_authentication.additional_properties = d
        return artifactory_authentication

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
