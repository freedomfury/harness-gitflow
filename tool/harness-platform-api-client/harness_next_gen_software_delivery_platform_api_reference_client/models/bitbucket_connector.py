from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.bitbucket_connector_type import BitbucketConnectorType, check_bitbucket_connector_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.bitbucket_api_access import BitbucketApiAccess
    from ..models.bitbucket_authentication import BitbucketAuthentication


T = TypeVar("T", bound="BitbucketConnector")


@_attrs_define
class BitbucketConnector:
    """This contains details of Bitbucket connectors

    Attributes:
        connector_type (str):
        url (str):
        authentication (BitbucketAuthentication): This contains details of the information needed for Bitbucket access
        type_ (BitbucketConnectorType):
        validation_repo (str | Unset):
        api_access (BitbucketApiAccess | Unset): This contains details of the information needed for Bitbucket API
            access
        delegate_selectors (list[str] | Unset):
        execute_on_delegate (bool | Unset):
        proxy (bool | Unset):
        ignore_test_connection (bool | Unset):
    """

    connector_type: str
    url: str
    authentication: BitbucketAuthentication
    type_: BitbucketConnectorType
    validation_repo: str | Unset = UNSET
    api_access: BitbucketApiAccess | Unset = UNSET
    delegate_selectors: list[str] | Unset = UNSET
    execute_on_delegate: bool | Unset = UNSET
    proxy: bool | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        url = self.url

        authentication = self.authentication.to_dict()

        type_: str = self.type_

        validation_repo = self.validation_repo

        api_access: dict[str, Any] | Unset = UNSET
        if not isinstance(self.api_access, Unset):
            api_access = self.api_access.to_dict()

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
                "url": url,
                "authentication": authentication,
                "type": type_,
            }
        )
        if validation_repo is not UNSET:
            field_dict["validationRepo"] = validation_repo
        if api_access is not UNSET:
            field_dict["apiAccess"] = api_access
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
        from ..models.bitbucket_api_access import BitbucketApiAccess
        from ..models.bitbucket_authentication import BitbucketAuthentication

        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        url = d.pop("url")

        authentication = BitbucketAuthentication.from_dict(d.pop("authentication"))

        type_ = check_bitbucket_connector_type(d.pop("type"))

        validation_repo = d.pop("validationRepo", UNSET)

        _api_access = d.pop("apiAccess", UNSET)
        api_access: BitbucketApiAccess | Unset
        if isinstance(_api_access, Unset):
            api_access = UNSET
        else:
            api_access = BitbucketApiAccess.from_dict(_api_access)

        delegate_selectors = cast(list[str], d.pop("delegateSelectors", UNSET))

        execute_on_delegate = d.pop("executeOnDelegate", UNSET)

        proxy = d.pop("proxy", UNSET)

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        bitbucket_connector = cls(
            connector_type=connector_type,
            url=url,
            authentication=authentication,
            type_=type_,
            validation_repo=validation_repo,
            api_access=api_access,
            delegate_selectors=delegate_selectors,
            execute_on_delegate=execute_on_delegate,
            proxy=proxy,
            ignore_test_connection=ignore_test_connection,
        )

        bitbucket_connector.additional_properties = d
        return bitbucket_connector

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
