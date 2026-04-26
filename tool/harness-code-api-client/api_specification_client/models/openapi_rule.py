from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_rule_state import EnumRuleState
from ..models.openapi_rule_type import OpenapiRuleType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.openapi_rule_repositories_type_0 import OpenapiRuleRepositoriesType0
    from ..models.openapi_rule_user_groups_type_0 import OpenapiRuleUserGroupsType0
    from ..models.openapi_rule_users_type_0 import OpenapiRuleUsersType0
    from ..models.protection_branch import ProtectionBranch
    from ..models.protection_pattern_type_0 import ProtectionPatternType0
    from ..models.protection_push import ProtectionPush
    from ..models.protection_repo_target_type_0 import ProtectionRepoTargetType0
    from ..models.protection_tag import ProtectionTag
    from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0


T = TypeVar("T", bound="OpenapiRule")


@_attrs_define
class OpenapiRule:
    """
    Attributes:
        created (int | Unset):
        created_by (None | TypesPrincipalInfoType0 | Unset):
        definition (ProtectionBranch | ProtectionPush | ProtectionTag | Unset):
        description (str | Unset):
        identifier (str | Unset):
        pattern (None | ProtectionPatternType0 | Unset):
        repo_target (None | ProtectionRepoTargetType0 | Unset):
        repositories (None | OpenapiRuleRepositoriesType0 | Unset):
        scope (int | Unset):
        state (EnumRuleState | Unset):
        type_ (OpenapiRuleType | Unset):
        updated (int | Unset):
        user_groups (None | OpenapiRuleUserGroupsType0 | Unset):
        users (None | OpenapiRuleUsersType0 | Unset):
    """

    created: int | Unset = UNSET
    created_by: None | TypesPrincipalInfoType0 | Unset = UNSET
    definition: ProtectionBranch | ProtectionPush | ProtectionTag | Unset = UNSET
    description: str | Unset = UNSET
    identifier: str | Unset = UNSET
    pattern: None | ProtectionPatternType0 | Unset = UNSET
    repo_target: None | ProtectionRepoTargetType0 | Unset = UNSET
    repositories: None | OpenapiRuleRepositoriesType0 | Unset = UNSET
    scope: int | Unset = UNSET
    state: EnumRuleState | Unset = UNSET
    type_: OpenapiRuleType | Unset = UNSET
    updated: int | Unset = UNSET
    user_groups: None | OpenapiRuleUserGroupsType0 | Unset = UNSET
    users: None | OpenapiRuleUsersType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.openapi_rule_repositories_type_0 import OpenapiRuleRepositoriesType0
        from ..models.openapi_rule_user_groups_type_0 import OpenapiRuleUserGroupsType0
        from ..models.openapi_rule_users_type_0 import OpenapiRuleUsersType0
        from ..models.protection_branch import ProtectionBranch
        from ..models.protection_pattern_type_0 import ProtectionPatternType0
        from ..models.protection_repo_target_type_0 import ProtectionRepoTargetType0
        from ..models.protection_tag import ProtectionTag
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0

        created = self.created

        created_by: dict[str, Any] | None | Unset
        if isinstance(self.created_by, Unset):
            created_by = UNSET
        elif isinstance(self.created_by, TypesPrincipalInfoType0):
            created_by = self.created_by.to_dict()
        else:
            created_by = self.created_by

        definition: dict[str, Any] | Unset
        if isinstance(self.definition, Unset):
            definition = UNSET
        elif isinstance(self.definition, ProtectionBranch):
            definition = self.definition.to_dict()
        elif isinstance(self.definition, ProtectionTag):
            definition = self.definition.to_dict()
        else:
            definition = self.definition.to_dict()

        description = self.description

        identifier = self.identifier

        pattern: dict[str, Any] | None | Unset
        if isinstance(self.pattern, Unset):
            pattern = UNSET
        elif isinstance(self.pattern, ProtectionPatternType0):
            pattern = self.pattern.to_dict()
        else:
            pattern = self.pattern

        repo_target: dict[str, Any] | None | Unset
        if isinstance(self.repo_target, Unset):
            repo_target = UNSET
        elif isinstance(self.repo_target, ProtectionRepoTargetType0):
            repo_target = self.repo_target.to_dict()
        else:
            repo_target = self.repo_target

        repositories: dict[str, Any] | None | Unset
        if isinstance(self.repositories, Unset):
            repositories = UNSET
        elif isinstance(self.repositories, OpenapiRuleRepositoriesType0):
            repositories = self.repositories.to_dict()
        else:
            repositories = self.repositories

        scope = self.scope

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated = self.updated

        user_groups: dict[str, Any] | None | Unset
        if isinstance(self.user_groups, Unset):
            user_groups = UNSET
        elif isinstance(self.user_groups, OpenapiRuleUserGroupsType0):
            user_groups = self.user_groups.to_dict()
        else:
            user_groups = self.user_groups

        users: dict[str, Any] | None | Unset
        if isinstance(self.users, Unset):
            users = UNSET
        elif isinstance(self.users, OpenapiRuleUsersType0):
            users = self.users.to_dict()
        else:
            users = self.users

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if created_by is not UNSET:
            field_dict["created_by"] = created_by
        if definition is not UNSET:
            field_dict["definition"] = definition
        if description is not UNSET:
            field_dict["description"] = description
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if pattern is not UNSET:
            field_dict["pattern"] = pattern
        if repo_target is not UNSET:
            field_dict["repo_target"] = repo_target
        if repositories is not UNSET:
            field_dict["repositories"] = repositories
        if scope is not UNSET:
            field_dict["scope"] = scope
        if state is not UNSET:
            field_dict["state"] = state
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated is not UNSET:
            field_dict["updated"] = updated
        if user_groups is not UNSET:
            field_dict["user_groups"] = user_groups
        if users is not UNSET:
            field_dict["users"] = users

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.openapi_rule_repositories_type_0 import OpenapiRuleRepositoriesType0
        from ..models.openapi_rule_user_groups_type_0 import OpenapiRuleUserGroupsType0
        from ..models.openapi_rule_users_type_0 import OpenapiRuleUsersType0
        from ..models.protection_branch import ProtectionBranch
        from ..models.protection_pattern_type_0 import ProtectionPatternType0
        from ..models.protection_push import ProtectionPush
        from ..models.protection_repo_target_type_0 import ProtectionRepoTargetType0
        from ..models.protection_tag import ProtectionTag
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0

        d = dict(src_dict)
        created = d.pop("created", UNSET)

        def _parse_created_by(data: object) -> None | TypesPrincipalInfoType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_types_principal_info_type_0 = TypesPrincipalInfoType0.from_dict(data)

                return componentsschemas_types_principal_info_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | TypesPrincipalInfoType0 | Unset, data)

        created_by = _parse_created_by(d.pop("created_by", UNSET))

        def _parse_definition(data: object) -> ProtectionBranch | ProtectionPush | ProtectionTag | Unset:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_openapi_rule_definition_type_0 = ProtectionBranch.from_dict(data)

                return componentsschemas_openapi_rule_definition_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_openapi_rule_definition_type_1 = ProtectionTag.from_dict(data)

                return componentsschemas_openapi_rule_definition_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            componentsschemas_openapi_rule_definition_type_2 = ProtectionPush.from_dict(data)

            return componentsschemas_openapi_rule_definition_type_2

        definition = _parse_definition(d.pop("definition", UNSET))

        description = d.pop("description", UNSET)

        identifier = d.pop("identifier", UNSET)

        def _parse_pattern(data: object) -> None | ProtectionPatternType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_protection_pattern_type_0 = ProtectionPatternType0.from_dict(data)

                return componentsschemas_protection_pattern_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProtectionPatternType0 | Unset, data)

        pattern = _parse_pattern(d.pop("pattern", UNSET))

        def _parse_repo_target(data: object) -> None | ProtectionRepoTargetType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_protection_repo_target_type_0 = ProtectionRepoTargetType0.from_dict(data)

                return componentsschemas_protection_repo_target_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | ProtectionRepoTargetType0 | Unset, data)

        repo_target = _parse_repo_target(d.pop("repo_target", UNSET))

        def _parse_repositories(data: object) -> None | OpenapiRuleRepositoriesType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                repositories_type_0 = OpenapiRuleRepositoriesType0.from_dict(data)

                return repositories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OpenapiRuleRepositoriesType0 | Unset, data)

        repositories = _parse_repositories(d.pop("repositories", UNSET))

        scope = d.pop("scope", UNSET)

        _state = d.pop("state", UNSET)
        state: EnumRuleState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = EnumRuleState(_state)

        _type_ = d.pop("type", UNSET)
        type_: OpenapiRuleType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = OpenapiRuleType(_type_)

        updated = d.pop("updated", UNSET)

        def _parse_user_groups(data: object) -> None | OpenapiRuleUserGroupsType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_groups_type_0 = OpenapiRuleUserGroupsType0.from_dict(data)

                return user_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OpenapiRuleUserGroupsType0 | Unset, data)

        user_groups = _parse_user_groups(d.pop("user_groups", UNSET))

        def _parse_users(data: object) -> None | OpenapiRuleUsersType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                users_type_0 = OpenapiRuleUsersType0.from_dict(data)

                return users_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | OpenapiRuleUsersType0 | Unset, data)

        users = _parse_users(d.pop("users", UNSET))

        openapi_rule = cls(
            created=created,
            created_by=created_by,
            definition=definition,
            description=description,
            identifier=identifier,
            pattern=pattern,
            repo_target=repo_target,
            repositories=repositories,
            scope=scope,
            state=state,
            type_=type_,
            updated=updated,
            user_groups=user_groups,
            users=users,
        )

        openapi_rule.additional_properties = d
        return openapi_rule

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
