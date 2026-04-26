from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_webhook_trigger import EnumWebhookTrigger
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_extra_header import TypesExtraHeader


T = TypeVar("T", bound="OpenapiUpdateSpaceWebhookRequest")


@_attrs_define
class OpenapiUpdateSpaceWebhookRequest:
    """
    Attributes:
        description (None | str | Unset):
        display_name (None | str | Unset):
        enabled (bool | None | Unset):
        extra_headers (list[TypesExtraHeader] | Unset):
        identifier (None | str | Unset):
        insecure (bool | None | Unset):
        secret (None | str | Unset):
        triggers (list[EnumWebhookTrigger] | None | Unset):
        uid (None | str | Unset):
        url (None | str | Unset):
    """

    description: None | str | Unset = UNSET
    display_name: None | str | Unset = UNSET
    enabled: bool | None | Unset = UNSET
    extra_headers: list[TypesExtraHeader] | Unset = UNSET
    identifier: None | str | Unset = UNSET
    insecure: bool | None | Unset = UNSET
    secret: None | str | Unset = UNSET
    triggers: list[EnumWebhookTrigger] | None | Unset = UNSET
    uid: None | str | Unset = UNSET
    url: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        display_name: None | str | Unset
        if isinstance(self.display_name, Unset):
            display_name = UNSET
        else:
            display_name = self.display_name

        enabled: bool | None | Unset
        if isinstance(self.enabled, Unset):
            enabled = UNSET
        else:
            enabled = self.enabled

        extra_headers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.extra_headers, Unset):
            extra_headers = []
            for extra_headers_item_data in self.extra_headers:
                extra_headers_item = extra_headers_item_data.to_dict()
                extra_headers.append(extra_headers_item)

        identifier: None | str | Unset
        if isinstance(self.identifier, Unset):
            identifier = UNSET
        else:
            identifier = self.identifier

        insecure: bool | None | Unset
        if isinstance(self.insecure, Unset):
            insecure = UNSET
        else:
            insecure = self.insecure

        secret: None | str | Unset
        if isinstance(self.secret, Unset):
            secret = UNSET
        else:
            secret = self.secret

        triggers: list[str] | None | Unset
        if isinstance(self.triggers, Unset):
            triggers = UNSET
        elif isinstance(self.triggers, list):
            triggers = []
            for triggers_type_0_item_data in self.triggers:
                triggers_type_0_item = triggers_type_0_item_data.value
                triggers.append(triggers_type_0_item)

        else:
            triggers = self.triggers

        uid: None | str | Unset
        if isinstance(self.uid, Unset):
            uid = UNSET
        else:
            uid = self.uid

        url: None | str | Unset
        if isinstance(self.url, Unset):
            url = UNSET
        else:
            url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if extra_headers is not UNSET:
            field_dict["extra_headers"] = extra_headers
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if insecure is not UNSET:
            field_dict["insecure"] = insecure
        if secret is not UNSET:
            field_dict["secret"] = secret
        if triggers is not UNSET:
            field_dict["triggers"] = triggers
        if uid is not UNSET:
            field_dict["uid"] = uid
        if url is not UNSET:
            field_dict["url"] = url

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_extra_header import TypesExtraHeader

        d = dict(src_dict)

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))

        def _parse_display_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        display_name = _parse_display_name(d.pop("display_name", UNSET))

        def _parse_enabled(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        enabled = _parse_enabled(d.pop("enabled", UNSET))

        _extra_headers = d.pop("extra_headers", UNSET)
        extra_headers: list[TypesExtraHeader] | Unset = UNSET
        if _extra_headers is not UNSET:
            extra_headers = []
            for extra_headers_item_data in _extra_headers:
                extra_headers_item = TypesExtraHeader.from_dict(extra_headers_item_data)

                extra_headers.append(extra_headers_item)

        def _parse_identifier(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        identifier = _parse_identifier(d.pop("identifier", UNSET))

        def _parse_insecure(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        insecure = _parse_insecure(d.pop("insecure", UNSET))

        def _parse_secret(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        secret = _parse_secret(d.pop("secret", UNSET))

        def _parse_triggers(data: object) -> list[EnumWebhookTrigger] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                triggers_type_0 = []
                _triggers_type_0 = data
                for triggers_type_0_item_data in _triggers_type_0:
                    triggers_type_0_item = EnumWebhookTrigger(triggers_type_0_item_data)

                    triggers_type_0.append(triggers_type_0_item)

                return triggers_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[EnumWebhookTrigger] | None | Unset, data)

        triggers = _parse_triggers(d.pop("triggers", UNSET))

        def _parse_uid(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        uid = _parse_uid(d.pop("uid", UNSET))

        def _parse_url(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        url = _parse_url(d.pop("url", UNSET))

        openapi_update_space_webhook_request = cls(
            description=description,
            display_name=display_name,
            enabled=enabled,
            extra_headers=extra_headers,
            identifier=identifier,
            insecure=insecure,
            secret=secret,
            triggers=triggers,
            uid=uid,
            url=url,
        )

        openapi_update_space_webhook_request.additional_properties = d
        return openapi_update_space_webhook_request

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
