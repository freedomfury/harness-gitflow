from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.oci_helm_authentication import OciHelmAuthentication


T = TypeVar("T", bound="OciHelmConnector")


@_attrs_define
class OciHelmConnector:
    """This contains Oci helm connector details

    Attributes:
        connector_type (str):
        helm_repo_url (str):
        auth (OciHelmAuthentication | Unset): This contains oci helm authentication details
        delegate_selectors (list[str] | Unset):
        ignore_test_connection (bool | Unset):
    """

    connector_type: str
    helm_repo_url: str
    auth: OciHelmAuthentication | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        helm_repo_url = self.helm_repo_url

        auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth, Unset):
            auth = self.auth.to_dict()

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        ignore_test_connection = self.ignore_test_connection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "helmRepoUrl": helm_repo_url,
            }
        )
        if auth is not UNSET:
            field_dict["auth"] = auth
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.oci_helm_authentication import OciHelmAuthentication

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        helm_repo_url = d.pop("helmRepoUrl")

        _auth = d.pop("auth", UNSET)
        auth: OciHelmAuthentication | Unset
        if isinstance(_auth, Unset):
            auth = UNSET
        else:
            auth = OciHelmAuthentication.from_dict(_auth)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        oci_helm_connector = cls(
            connector_type=connector_type,
            helm_repo_url=helm_repo_url,
            auth=auth,
            delegate_selectors=delegate_selectors,
            ignore_test_connection=ignore_test_connection,
        )

        oci_helm_connector.additional_properties = d
        return oci_helm_connector

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
