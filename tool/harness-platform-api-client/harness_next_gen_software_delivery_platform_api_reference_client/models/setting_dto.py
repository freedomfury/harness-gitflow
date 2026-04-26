from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.setting_dto_allowed_scopes_item import SettingDTOAllowedScopesItem, check_setting_dto_allowed_scopes_item
from ..models.setting_dto_category import SettingDTOCategory, check_setting_dto_category
from ..models.setting_dto_setting_source import SettingDTOSettingSource, check_setting_dto_setting_source
from ..models.setting_dto_value_type import SettingDTOValueType, check_setting_dto_value_type
from ..types import UNSET, Unset

T = TypeVar("T", bound="SettingDTO")


@_attrs_define
class SettingDTO:
    """
    Attributes:
        identifier (str): Identifier of the Setting.
        name (str): Name of the Setting.
        category (SettingDTOCategory): Category of the Setting.
        group_identifier (str): Group Id of the setting
        value_type (SettingDTOValueType): Type of Value of the Setting.
        allow_overrides (bool): Allow override of the Setting in sub-scopes.
        is_setting_editable (bool): Is the setting editable at the current scope
        allowed_scopes (list[SettingDTOAllowedScopesItem]): List of scopes where the setting is available
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        allowed_values (list[str] | Unset): Set of Values allowed for the Setting.
        value (str | Unset): Value of the setting
        default_value (str | Unset): Default Value of the Setting.
        setting_source (SettingDTOSettingSource | Unset): Source of the setting value
    """

    identifier: str
    name: str
    category: SettingDTOCategory
    group_identifier: str
    value_type: SettingDTOValueType
    allow_overrides: bool
    is_setting_editable: bool
    allowed_scopes: list[SettingDTOAllowedScopesItem]
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    allowed_values: list[str] | Unset = UNSET
    value: str | Unset = UNSET
    default_value: str | Unset = UNSET
    setting_source: SettingDTOSettingSource | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        name = self.name

        category: str = self.category

        group_identifier = self.group_identifier

        value_type: str = self.value_type

        allow_overrides = self.allow_overrides

        is_setting_editable = self.is_setting_editable

        allowed_scopes = []
        for allowed_scopes_item_data in self.allowed_scopes:
            allowed_scopes_item: str = allowed_scopes_item_data
            allowed_scopes.append(allowed_scopes_item)

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        allowed_values: list[str] | Unset = UNSET
        if not isinstance(self.allowed_values, Unset):
            allowed_values = self.allowed_values

        value = self.value

        default_value = self.default_value

        setting_source: str | Unset = UNSET
        if not isinstance(self.setting_source, Unset):
            setting_source = self.setting_source

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "name": name,
                "category": category,
                "groupIdentifier": group_identifier,
                "valueType": value_type,
                "allowOverrides": allow_overrides,
                "isSettingEditable": is_setting_editable,
                "allowedScopes": allowed_scopes,
            }
        )
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if allowed_values is not UNSET:
            field_dict["allowedValues"] = allowed_values
        if value is not UNSET:
            field_dict["value"] = value
        if default_value is not UNSET:
            field_dict["defaultValue"] = default_value
        if setting_source is not UNSET:
            field_dict["settingSource"] = setting_source

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        identifier = d.pop("identifier")

        name = d.pop("name")

        category = check_setting_dto_category(d.pop("category"))

        group_identifier = d.pop("groupIdentifier")

        value_type = check_setting_dto_value_type(d.pop("valueType"))

        allow_overrides = d.pop("allowOverrides")

        is_setting_editable = d.pop("isSettingEditable")

        allowed_scopes = []
        _allowed_scopes = d.pop("allowedScopes")
        for allowed_scopes_item_data in _allowed_scopes:
            allowed_scopes_item = check_setting_dto_allowed_scopes_item(allowed_scopes_item_data)

            allowed_scopes.append(allowed_scopes_item)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        allowed_values = cast(list[str], d.pop("allowedValues", UNSET))

        value = d.pop("value", UNSET)

        default_value = d.pop("defaultValue", UNSET)

        _setting_source = d.pop("settingSource", UNSET)
        setting_source: SettingDTOSettingSource | Unset
        if isinstance(_setting_source, Unset):
            setting_source = UNSET
        else:
            setting_source = check_setting_dto_setting_source(_setting_source)

        setting_dto = cls(
            identifier=identifier,
            name=name,
            category=category,
            group_identifier=group_identifier,
            value_type=value_type,
            allow_overrides=allow_overrides,
            is_setting_editable=is_setting_editable,
            allowed_scopes=allowed_scopes,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            allowed_values=allowed_values,
            value=value,
            default_value=default_value,
            setting_source=setting_source,
        )

        setting_dto.additional_properties = d
        return setting_dto

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
