from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.freeze_response_freeze_scope import FreezeResponseFreezeScope, check_freeze_response_freeze_scope
from ..models.freeze_response_status import FreezeResponseStatus, check_freeze_response_status
from ..models.freeze_response_type import FreezeResponseType, check_freeze_response_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.freeze_response_tags import FreezeResponseTags
    from ..models.freeze_window import FreezeWindow


T = TypeVar("T", bound="FreezeResponse")


@_attrs_define
class FreezeResponse:
    """This contains details of the Freeze Response

    Attributes:
        account_id (str):
        name (str):
        identifier (str):
        yaml (str):
        type_ (FreezeResponseType | Unset):
        status (FreezeResponseStatus | Unset):
        description (str | Unset):
        tags (FreezeResponseTags | Unset):
        org_identifier (str | Unset):
        project_identifier (str | Unset):
        windows (list[FreezeWindow] | Unset):
        created_at (int | Unset):
        last_updated_at (int | Unset):
        freeze_scope (FreezeResponseFreezeScope | Unset):
    """

    account_id: str
    name: str
    identifier: str
    yaml: str
    type_: FreezeResponseType | Unset = UNSET
    status: FreezeResponseStatus | Unset = UNSET
    description: str | Unset = UNSET
    tags: FreezeResponseTags | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    windows: list[FreezeWindow] | Unset = UNSET
    created_at: int | Unset = UNSET
    last_updated_at: int | Unset = UNSET
    freeze_scope: FreezeResponseFreezeScope | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        account_id = self.account_id

        name = self.name

        identifier = self.identifier

        yaml = self.yaml

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        description = self.description

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        windows: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.windows, Unset):
            windows = []
            for windows_item_data in self.windows:
                windows_item = windows_item_data.to_dict()
                windows.append(windows_item)

        created_at = self.created_at

        last_updated_at = self.last_updated_at

        freeze_scope: str | Unset = UNSET
        if not isinstance(self.freeze_scope, Unset):
            freeze_scope = self.freeze_scope

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "accountId": account_id,
                "name": name,
                "identifier": identifier,
                "yaml": yaml,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if status is not UNSET:
            field_dict["status"] = status
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if windows is not UNSET:
            field_dict["windows"] = windows
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if last_updated_at is not UNSET:
            field_dict["lastUpdatedAt"] = last_updated_at
        if freeze_scope is not UNSET:
            field_dict["freezeScope"] = freeze_scope

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.freeze_response_tags import FreezeResponseTags
        from ..models.freeze_window import FreezeWindow

        d = dict(src_dict)
        account_id = d.pop("accountId")

        name = d.pop("name")

        identifier = d.pop("identifier")

        yaml = d.pop("yaml")

        _type_ = d.pop("type", UNSET)
        type_: FreezeResponseType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_freeze_response_type(_type_)

        _status = d.pop("status", UNSET)
        status: FreezeResponseStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_freeze_response_status(_status)

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: FreezeResponseTags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = FreezeResponseTags.from_dict(_tags)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        _windows = d.pop("windows", UNSET)
        windows: list[FreezeWindow] | Unset = UNSET
        if _windows is not UNSET:
            windows = []
            for windows_item_data in _windows:
                windows_item = FreezeWindow.from_dict(windows_item_data)

                windows.append(windows_item)

        created_at = d.pop("createdAt", UNSET)

        last_updated_at = d.pop("lastUpdatedAt", UNSET)

        _freeze_scope = d.pop("freezeScope", UNSET)
        freeze_scope: FreezeResponseFreezeScope | Unset
        if isinstance(_freeze_scope, Unset):
            freeze_scope = UNSET
        else:
            freeze_scope = check_freeze_response_freeze_scope(_freeze_scope)

        freeze_response = cls(
            account_id=account_id,
            name=name,
            identifier=identifier,
            yaml=yaml,
            type_=type_,
            status=status,
            description=description,
            tags=tags,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            windows=windows,
            created_at=created_at,
            last_updated_at=last_updated_at,
            freeze_scope=freeze_scope,
        )

        freeze_response.additional_properties = d
        return freeze_response

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
