from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.docker_connector_provider_type import DockerConnectorProviderType, check_docker_connector_provider_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.docker_authentication import DockerAuthentication


T = TypeVar("T", bound="DockerConnector")


@_attrs_define
class DockerConnector:
    """Docker Connector details.

    Attributes:
        connector_type (str):
        docker_registry_url (str):
        provider_type (DockerConnectorProviderType): This entity contains the details of the Docker Registry
        auth (DockerAuthentication | Unset): This entity contains the details for Docker Authentication
        delegate_selectors (list[str] | Unset):
        execute_on_delegate (bool | Unset):
        proxy (bool | Unset):
        ignore_test_connection (bool | Unset):
    """

    connector_type: str
    docker_registry_url: str
    provider_type: DockerConnectorProviderType
    auth: DockerAuthentication | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    execute_on_delegate: bool | Unset = UNSET
    proxy: bool | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        docker_registry_url = self.docker_registry_url

        provider_type: str = self.provider_type

        auth: dict[str, Any] | Unset = UNSET
        if not isinstance(self.auth, Unset):
            auth = self.auth.to_dict()

        delegate_selectors: list[str] | Unset = UNSET
        if not isinstance(self.delegate_selectors, Unset):
            delegate_selectors = self.delegate_selectors

        execute_on_delegate = self.execute_on_delegate

        proxy = self.proxy

        ignore_test_connection = self.ignore_test_connection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "dockerRegistryUrl": docker_registry_url,
                "providerType": provider_type,
            }
        )
        if auth is not UNSET:
            field_dict["auth"] = auth
        if delegate_selectors is not UNSET:
            field_dict["delegateSelectors"] = delegate_selectors
        if execute_on_delegate is not UNSET:
            field_dict["executeOnDelegate"] = execute_on_delegate
        if proxy is not UNSET:
            field_dict["proxy"] = proxy
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.docker_authentication import DockerAuthentication

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        docker_registry_url = d.pop("dockerRegistryUrl")

        provider_type = check_docker_connector_provider_type(d.pop("providerType"))

        _auth = d.pop("auth", UNSET)
        auth: DockerAuthentication | Unset
        if isinstance(_auth, Unset):
            auth = UNSET
        else:
            auth = DockerAuthentication.from_dict(_auth)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        execute_on_delegate = d.pop("executeOnDelegate", UNSET)

        proxy = d.pop("proxy", UNSET)

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        docker_connector = cls(
            connector_type=connector_type,
            docker_registry_url=docker_registry_url,
            provider_type=provider_type,
            auth=auth,
            delegate_selectors=delegate_selectors,
            execute_on_delegate=execute_on_delegate,
            proxy=proxy,
            ignore_test_connection=ignore_test_connection,
        )

        docker_connector.additional_properties = d
        return docker_connector

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
