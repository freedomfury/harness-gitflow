from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.invite_invite_type import InviteInviteType, check_invite_invite_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.role_binding import RoleBinding


T = TypeVar("T", bound="Invite")


@_attrs_define
class Invite:
    """This is the view of the Invite entity defined in Harness

    Attributes:
        email (str): Email Id associated with the user to be invited.
        invite_type (InviteInviteType): Specifies the invite type.
        id (str | Unset): Identifier of the Invite.
        name (str | Unset): Name of the Invite.
        account_identifier (str | Unset): Account Identifier for the Entity.
        org_identifier (str | Unset): Organization Identifier for the Entity.
        project_identifier (str | Unset): Project Identifier for the Entity.
        role_bindings (list[RoleBinding] | Unset): Role bindings to be associated with the invited users.
        user_groups (list[str] | Unset): List of the userGroups in the invite.
        approved (bool | Unset): Specifies whether or not the invite is approved. By default this value is set to false.
    """

    email: str
    invite_type: InviteInviteType
    id: str | Unset = UNSET
    name: str | Unset = UNSET
    account_identifier: str | Unset = UNSET
    org_identifier: str | Unset = UNSET
    project_identifier: str | Unset = UNSET
    role_bindings: list[RoleBinding] | Unset = UNSET
    user_groups: list[str] | Unset = UNSET
    approved: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        email = self.email

        invite_type: str = self.invite_type

        id = self.id

        name = self.name

        account_identifier = self.account_identifier

        org_identifier = self.org_identifier

        project_identifier = self.project_identifier

        role_bindings: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.role_bindings, Unset):
            role_bindings = []
            for role_bindings_item_data in self.role_bindings:
                role_bindings_item = role_bindings_item_data.to_dict()
                role_bindings.append(role_bindings_item)

        user_groups: list[str] | Unset = UNSET
        if not isinstance(self.user_groups, Unset):
            user_groups = self.user_groups

        approved = self.approved

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
                "inviteType": invite_type,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if org_identifier is not UNSET:
            field_dict["orgIdentifier"] = org_identifier
        if project_identifier is not UNSET:
            field_dict["projectIdentifier"] = project_identifier
        if role_bindings is not UNSET:
            field_dict["roleBindings"] = role_bindings
        if user_groups is not UNSET:
            field_dict["userGroups"] = user_groups
        if approved is not UNSET:
            field_dict["approved"] = approved

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.role_binding import RoleBinding

        d = dict(src_dict)
        email = d.pop("email")

        invite_type = check_invite_invite_type(d.pop("inviteType"))

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        account_identifier = d.pop("accountIdentifier", UNSET)

        org_identifier = d.pop("orgIdentifier", UNSET)

        project_identifier = d.pop("projectIdentifier", UNSET)

        _role_bindings = d.pop("roleBindings", UNSET)
        role_bindings: list[RoleBinding] | Unset = UNSET
        if _role_bindings is not UNSET:
            role_bindings = []
            for role_bindings_item_data in _role_bindings:
                role_bindings_item = RoleBinding.from_dict(role_bindings_item_data)

                role_bindings.append(role_bindings_item)

        user_groups = cast(list[str], d.pop("userGroups", UNSET))

        approved = d.pop("approved", UNSET)

        invite = cls(
            email=email,
            invite_type=invite_type,
            id=id,
            name=name,
            account_identifier=account_identifier,
            org_identifier=org_identifier,
            project_identifier=project_identifier,
            role_bindings=role_bindings,
            user_groups=user_groups,
            approved=approved,
        )

        invite.additional_properties = d
        return invite

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
