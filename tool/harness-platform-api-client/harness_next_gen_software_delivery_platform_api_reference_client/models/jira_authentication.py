from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.jira_authentication_type import JiraAuthenticationType, check_jira_authentication_type

if TYPE_CHECKING:
    from ..models.jira_auth_credentials import JiraAuthCredentials


T = TypeVar("T", bound="JiraAuthentication")


@_attrs_define
class JiraAuthentication:
    """This entity contains the details for Jira Authentication

    Attributes:
        type_ (JiraAuthenticationType):
        spec (JiraAuthCredentials): This contains details of credentials for Jira Authentication
    """

    type_: JiraAuthenticationType
    spec: JiraAuthCredentials
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_: str = self.type_

        spec = self.spec.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "spec": spec,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.jira_auth_credentials import JiraAuthCredentials

        d = dict(src_dict)
        type_ = check_jira_authentication_type(d.pop("type"))

        spec = JiraAuthCredentials.from_dict(d.pop("spec"))

        jira_authentication = cls(
            type_=type_,
            spec=spec,
        )

        jira_authentication.additional_properties = d
        return jira_authentication

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
