from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_webhook_execution_result import EnumWebhookExecutionResult
from ..models.enum_webhook_parent import EnumWebhookParent
from ..models.enum_webhook_trigger import EnumWebhookTrigger
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_extra_header import TypesExtraHeader


T = TypeVar("T", bound="OpenapiWebhookType")


@_attrs_define
class OpenapiWebhookType:
    """
    Attributes:
        created (int | Unset):
        created_by (int | Unset):
        description (str | Unset):
        display_name (str | Unset):
        enabled (bool | Unset):
        extra_headers (list[TypesExtraHeader] | Unset):
        has_secret (bool | Unset):
        id (int | Unset):
        identifier (str | Unset):
        insecure (bool | Unset):
        latest_execution_result (EnumWebhookExecutionResult | Unset):
        parent_id (int | Unset):
        parent_type (EnumWebhookParent | Unset):
        scope (int | Unset):
        triggers (list[EnumWebhookTrigger] | None | Unset):
        updated (int | Unset):
        url (str | Unset):
        version (int | Unset):
    """

    created: int | Unset = UNSET
    created_by: int | Unset = UNSET
    description: str | Unset = UNSET
    display_name: str | Unset = UNSET
    enabled: bool | Unset = UNSET
    extra_headers: list[TypesExtraHeader] | Unset = UNSET
    has_secret: bool | Unset = UNSET
    id: int | Unset = UNSET
    identifier: str | Unset = UNSET
    insecure: bool | Unset = UNSET
    latest_execution_result: EnumWebhookExecutionResult | Unset = UNSET
    parent_id: int | Unset = UNSET
    parent_type: EnumWebhookParent | Unset = UNSET
    scope: int | Unset = UNSET
    triggers: list[EnumWebhookTrigger] | None | Unset = UNSET
    updated: int | Unset = UNSET
    url: str | Unset = UNSET
    version: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        created = self.created

        created_by = self.created_by

        description = self.description

        display_name = self.display_name

        enabled = self.enabled

        extra_headers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.extra_headers, Unset):
            extra_headers = []
            for extra_headers_item_data in self.extra_headers:
                extra_headers_item = extra_headers_item_data.to_dict()
                extra_headers.append(extra_headers_item)

        has_secret = self.has_secret

        id = self.id

        identifier = self.identifier

        insecure = self.insecure

        latest_execution_result: str | Unset = UNSET
        if not isinstance(self.latest_execution_result, Unset):
            latest_execution_result = self.latest_execution_result.value

        parent_id = self.parent_id

        parent_type: str | Unset = UNSET
        if not isinstance(self.parent_type, Unset):
            parent_type = self.parent_type.value

        scope = self.scope

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

        updated = self.updated

        url = self.url

        version = self.version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if description is not UNSET:
            field_dict["description"] = description
        if display_name is not UNSET:
            field_dict["display_name"] = display_name
        if enabled is not UNSET:
            field_dict["enabled"] = enabled
        if extra_headers is not UNSET:
            field_dict["extra_headers"] = extra_headers
        if has_secret is not UNSET:
            field_dict["has_secret"] = has_secret
        if id is not UNSET:
            field_dict["id"] = id
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if insecure is not UNSET:
            field_dict["insecure"] = insecure
        if latest_execution_result is not UNSET:
            field_dict["latest_execution_result"] = latest_execution_result
        if parent_id is not UNSET:
            field_dict["parent_id"] = parent_id
        if parent_type is not UNSET:
            field_dict["parent_type"] = parent_type
        if scope is not UNSET:
            field_dict["scope"] = scope
        if triggers is not UNSET:
            field_dict["triggers"] = triggers
        if updated is not UNSET:
            field_dict["updated"] = updated
        if url is not UNSET:
            field_dict["url"] = url
        if version is not UNSET:
            field_dict["version"] = version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_extra_header import TypesExtraHeader

        d = dict(src_dict)
        created = d.pop("created", UNSET)

        created_by = d.pop("created_by", UNSET)

        description = d.pop("description", UNSET)

        display_name = d.pop("display_name", UNSET)

        enabled = d.pop("enabled", UNSET)

        _extra_headers = d.pop("extra_headers", UNSET)
        extra_headers: list[TypesExtraHeader] | Unset = UNSET
        if _extra_headers is not UNSET:
            extra_headers = []
            for extra_headers_item_data in _extra_headers:
                extra_headers_item = TypesExtraHeader.from_dict(extra_headers_item_data)

                extra_headers.append(extra_headers_item)

        has_secret = d.pop("has_secret", UNSET)

        id = d.pop("id", UNSET)

        identifier = d.pop("identifier", UNSET)

        insecure = d.pop("insecure", UNSET)

        _latest_execution_result = d.pop("latest_execution_result", UNSET)
        latest_execution_result: EnumWebhookExecutionResult | Unset
        if isinstance(_latest_execution_result, Unset):
            latest_execution_result = UNSET
        else:
            latest_execution_result = EnumWebhookExecutionResult(_latest_execution_result)

        parent_id = d.pop("parent_id", UNSET)

        _parent_type = d.pop("parent_type", UNSET)
        parent_type: EnumWebhookParent | Unset
        if isinstance(_parent_type, Unset):
            parent_type = UNSET
        else:
            parent_type = EnumWebhookParent(_parent_type)

        scope = d.pop("scope", UNSET)

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

        updated = d.pop("updated", UNSET)

        url = d.pop("url", UNSET)

        version = d.pop("version", UNSET)

        openapi_webhook_type = cls(
            created=created,
            created_by=created_by,
            description=description,
            display_name=display_name,
            enabled=enabled,
            extra_headers=extra_headers,
            has_secret=has_secret,
            id=id,
            identifier=identifier,
            insecure=insecure,
            latest_execution_result=latest_execution_result,
            parent_id=parent_id,
            parent_type=parent_type,
            scope=scope,
            triggers=triggers,
            updated=updated,
            url=url,
            version=version,
        )

        openapi_webhook_type.additional_properties = d
        return openapi_webhook_type

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
