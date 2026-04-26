from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.notification_setting_config_dto import NotificationSettingConfigDTO
    from ..models.user_basic_info import UserBasicInfo
    from ..models.user_group_response_v2_tags import UserGroupResponseV2Tags


T = TypeVar("T", bound="UserGroupResponseV2")


@_attrs_define
class UserGroupResponseV2:
    """User Group details defined in Harness.

    Attributes:
        identifier (str): Identifier of the UserGroup.
        name (str): Name of the UserGroup.
        account_identifier (str | Unset): Account Identifier for the Entity.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        users (list[UserBasicInfo] | Unset): List of users emails in the UserGroup.
        notification_configs (list[NotificationSettingConfigDTO] | Unset): List of notification settings.
        is_sso_linked (bool | Unset):
        linked_sso_id (str | Unset): Identifier of the linked SSO.
        linked_sso_display_name (str | Unset): Name of the linked SSO.
        sso_group_id (str | Unset): Identifier of the userGroup in SSO.
        sso_group_name (str | Unset): Name of the SSO userGroup.
        linked_sso_type (str | Unset): Type of linked SSO
        externally_managed (bool | Unset): Specifies whether or not the userGroup is externally managed.
        description (str | Unset): Description of the entity
        tags (UserGroupResponseV2Tags | Unset): Tags
        harness_managed (bool | Unset): Specifies whether or not the userGroup is managed by harness.
        sso_linked (bool | Unset):
    """

    identifier: str
    name: str
    account_identifier: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    users: list[UserBasicInfo] | Unset = UNSET
    notification_configs: list[NotificationSettingConfigDTO] | Unset = UNSET
    is_sso_linked: bool | Unset = UNSET
    linked_sso_id: str | Unset = UNSET
    linked_sso_display_name: str | Unset = UNSET
    sso_group_id: str | Unset = UNSET
    sso_group_name: str | Unset = UNSET
    linked_sso_type: str | Unset = UNSET
    externally_managed: bool | Unset = UNSET
    description: str | Unset = UNSET
    tags: UserGroupResponseV2Tags | Unset = UNSET
    harness_managed: bool | Unset = UNSET
    sso_linked: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        identifier = self.identifier

        name = self.name

        account_identifier = self.account_identifier

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        users: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.users, Unset):
            users = []
            for users_item_data in self.users:
                users_item = users_item_data.to_dict()
                users.append(users_item)

        notification_configs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.notification_configs, Unset):
            notification_configs = []
            for notification_configs_item_data in self.notification_configs:
                notification_configs_item = notification_configs_item_data.to_dict()
                notification_configs.append(notification_configs_item)

        is_sso_linked = self.is_sso_linked

        linked_sso_id = self.linked_sso_id

        linked_sso_display_name = self.linked_sso_display_name

        sso_group_id = self.sso_group_id

        sso_group_name = self.sso_group_name

        linked_sso_type = self.linked_sso_type

        externally_managed = self.externally_managed

        description = self.description

        tags: dict[str, Any] | Unset = UNSET
        if not isinstance(self.tags, Unset):
            tags = self.tags.to_dict()

        harness_managed = self.harness_managed

        sso_linked = self.sso_linked

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "identifier": identifier,
                "name": name,
            }
        )
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if users is not UNSET:
            field_dict["users"] = users
        if notification_configs is not UNSET:
            field_dict["notificationConfigs"] = notification_configs
        if is_sso_linked is not UNSET:
            field_dict["isSsoLinked"] = is_sso_linked
        if linked_sso_id is not UNSET:
            field_dict["linkedSsoId"] = linked_sso_id
        if linked_sso_display_name is not UNSET:
            field_dict["linkedSsoDisplayName"] = linked_sso_display_name
        if sso_group_id is not UNSET:
            field_dict["ssoGroupId"] = sso_group_id
        if sso_group_name is not UNSET:
            field_dict["ssoGroupName"] = sso_group_name
        if linked_sso_type is not UNSET:
            field_dict["linkedSsoType"] = linked_sso_type
        if externally_managed is not UNSET:
            field_dict["externallyManaged"] = externally_managed
        if description is not UNSET:
            field_dict["description"] = description
        if tags is not UNSET:
            field_dict["tags"] = tags
        if harness_managed is not UNSET:
            field_dict["harnessManaged"] = harness_managed
        if sso_linked is not UNSET:
            field_dict["ssoLinked"] = sso_linked

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.notification_setting_config_dto import NotificationSettingConfigDTO
        from ..models.user_basic_info import UserBasicInfo
        from ..models.user_group_response_v2_tags import UserGroupResponseV2Tags

        d = dict(src_dict)
        identifier = d.pop("identifier")

        name = d.pop("name")

        account_identifier = d.pop("accountIdentifier", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        _users = d.pop("users", UNSET)
        users: list[UserBasicInfo] | Unset = UNSET
        if _users is not UNSET:
            users = []
            for users_item_data in _users:
                users_item = UserBasicInfo.from_dict(users_item_data)

                users.append(users_item)

        _notification_configs = d.pop("notificationConfigs", UNSET)
        notification_configs: list[NotificationSettingConfigDTO] | Unset = UNSET
        if _notification_configs is not UNSET:
            notification_configs = []
            for notification_configs_item_data in _notification_configs:
                notification_configs_item = NotificationSettingConfigDTO.from_dict(notification_configs_item_data)

                notification_configs.append(notification_configs_item)

        is_sso_linked = d.pop("isSsoLinked", UNSET)

        linked_sso_id = d.pop("linkedSsoId", UNSET)

        linked_sso_display_name = d.pop("linkedSsoDisplayName", UNSET)

        sso_group_id = d.pop("ssoGroupId", UNSET)

        sso_group_name = d.pop("ssoGroupName", UNSET)

        linked_sso_type = d.pop("linkedSsoType", UNSET)

        externally_managed = d.pop("externallyManaged", UNSET)

        description = d.pop("description", UNSET)

        _tags = d.pop("tags", UNSET)
        tags: UserGroupResponseV2Tags | Unset
        if isinstance(_tags, Unset):
            tags = UNSET
        else:
            tags = UserGroupResponseV2Tags.from_dict(_tags)

        harness_managed = d.pop("harnessManaged", UNSET)

        sso_linked = d.pop("ssoLinked", UNSET)

        user_group_response_v2 = cls(
            identifier=identifier,
            name=name,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            users=users,
            notification_configs=notification_configs,
            is_sso_linked=is_sso_linked,
            linked_sso_id=linked_sso_id,
            linked_sso_display_name=linked_sso_display_name,
            sso_group_id=sso_group_id,
            sso_group_name=sso_group_name,
            linked_sso_type=linked_sso_type,
            externally_managed=externally_managed,
            description=description,
            tags=tags,
            harness_managed=harness_managed,
            sso_linked=sso_linked,
        )

        user_group_response_v2.additional_properties = d
        return user_group_response_v2

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
