from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.slack_connector_api_access_type import SlackConnectorApiAccessType, check_slack_connector_api_access_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="SlackConnector")


@_attrs_define
class SlackConnector:
    """Slack Connector details.

    Attributes:
        connector_type (str):
        api_access_type (SlackConnectorApiAccessType):
        bot_user_token_ref (str | Unset):
        access_token_ref (str | Unset):
        refresh_token_ref (str | Unset):
        ignore_test_connection (bool | Unset):
    """

    connector_type: str
    api_access_type: SlackConnectorApiAccessType
    bot_user_token_ref: str | Unset = UNSET
    access_token_ref: str | Unset = UNSET
    refresh_token_ref: str | Unset = UNSET
    ignore_test_connection: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        connector_type = self.connector_type

        api_access_type: str = self.api_access_type

        bot_user_token_ref = self.bot_user_token_ref

        access_token_ref = self.access_token_ref

        refresh_token_ref = self.refresh_token_ref

        ignore_test_connection = self.ignore_test_connection

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "connectorType": connector_type,
                "apiAccessType": api_access_type,
            }
        )
        if bot_user_token_ref is not UNSET:
            field_dict["botUserTokenRef"] = bot_user_token_ref
        if access_token_ref is not UNSET:
            field_dict["accessTokenRef"] = access_token_ref
        if refresh_token_ref is not UNSET:
            field_dict["refreshTokenRef"] = refresh_token_ref
        if ignore_test_connection is not UNSET:
            field_dict["ignoreTestConnection"] = ignore_test_connection

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        connector_type = d.pop("connectorType")

        api_access_type = check_slack_connector_api_access_type(d.pop("apiAccessType"))

        bot_user_token_ref = d.pop("botUserTokenRef", UNSET)

        access_token_ref = d.pop("accessTokenRef", UNSET)

        refresh_token_ref = d.pop("refreshTokenRef", UNSET)

        ignore_test_connection = d.pop("ignoreTestConnection", UNSET)

        slack_connector = cls(
            connector_type=connector_type,
            api_access_type=api_access_type,
            bot_user_token_ref=bot_user_token_ref,
            access_token_ref=access_token_ref,
            refresh_token_ref=refresh_token_ref,
            ignore_test_connection=ignore_test_connection,
        )

        slack_connector.additional_properties = d
        return slack_connector

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
