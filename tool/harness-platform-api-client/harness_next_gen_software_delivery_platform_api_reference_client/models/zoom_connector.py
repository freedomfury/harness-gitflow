from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.zoom_connector_api_access_type import ZoomConnectorApiAccessType, check_zoom_connector_api_access_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="ZoomConnector")


@_attrs_define
class ZoomConnector:
    """Zoom Connector details.

    Attributes:
        connector_type (str):
        api_access_type (ZoomConnectorApiAccessType):
        zoom_account_id (str | Unset):
        client_id (str | Unset):
        zoom_user_id (str | Unset):
        client_secret_ref (str | Unset):
        access_token_ref (str | Unset):
        refresh_token_ref (str | Unset):
        token_expiration_time (int | Unset):
        ignore_test_connection (bool | Unset):
    """

    connector_type: str
    api_access_type: ZoomConnectorApiAccessType
    zoom_account_id: str | Unset = UNSET
    client_id: str | Unset = UNSET
    zoom_user_id: str | Unset = UNSET
    client_secret_ref: str | Unset = UNSET
    access_token_ref: str | Unset = UNSET
    refresh_token_ref: str | Unset = UNSET
    token_expiration_time: int | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        api_access_type: str = self.api_access_type

        zoom_account_id = self.zoom_account_id

        client_id = self.client_id

        zoom_user_id = self.zoom_user_id

        client_secret_ref = self.client_secret_ref

        access_token_ref = self.access_token_ref

        refresh_token_ref = self.refresh_token_ref

        token_expiration_time = self.token_expiration_time

        ignore_test_connection = self.ignore_test_connection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "apiAccessType": api_access_type,
            }
        )
        if zoom_account_id is not UNSET:
            field_dict["zoomAccountId"] = zoom_account_id
        if client_id is not UNSET:
            field_dict["clientId"] = client_id
        if zoom_user_id is not UNSET:
            field_dict["zoomUserId"] = zoom_user_id
        if client_secret_ref is not UNSET:
            field_dict["clientSecretRef"] = client_secret_ref
        if access_token_ref is not UNSET:
            field_dict["accessTokenRef"] = access_token_ref
        if refresh_token_ref is not UNSET:
            field_dict["refreshTokenRef"] = refresh_token_ref
        if token_expiration_time is not UNSET:
            field_dict["tokenExpirationTime"] = token_expiration_time
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        api_access_type = check_zoom_connector_api_access_type(d.pop("apiAccessType"))

        zoom_account_id = d.pop("zoomAccountId", UNSET)

        client_id = d.pop("clientId", UNSET)

        zoom_user_id = d.pop("zoomUserId", UNSET)

        client_secret_ref = d.pop("clientSecretRef", UNSET)

        access_token_ref = d.pop("accessTokenRef", UNSET)

        refresh_token_ref = d.pop("refreshTokenRef", UNSET)

        token_expiration_time = d.pop("tokenExpirationTime", UNSET)

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        zoom_connector = cls(
            connector_type=connector_type,
            api_access_type=api_access_type,
            zoom_account_id=zoom_account_id,
            client_id=client_id,
            zoom_user_id=zoom_user_id,
            client_secret_ref=client_secret_ref,
            access_token_ref=access_token_ref,
            refresh_token_ref=refresh_token_ref,
            token_expiration_time=token_expiration_time,
            ignore_test_connection=ignore_test_connection,
        )

        zoom_connector.additional_properties = d
        return zoom_connector

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
