from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.delegate_token_details_status import DelegateTokenDetailsStatus, check_delegate_token_details_status
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.embedded_user import EmbeddedUser
    from ..models.principal import Principal


T = TypeVar("T", bound="DelegateTokenDetails")


@_attrs_define
class DelegateTokenDetails:
    """
    Attributes:
        uuid (str | Unset):
        account_id (str | Unset):
        name (str | Unset):
        created_by (EmbeddedUser | Unset):
        created_by_ng_user (Principal | Unset):
        created_at (int | Unset):
        status (DelegateTokenDetailsStatus | Unset):
        value (str | Unset): Value of delegate token. This is only populated when fetching delegate token by name or the
            user has edit delegate permission.
        owner_identifier (str | Unset):
        parent_unique_id (str | Unset):
        revoke_after (int | Unset):
    """

    uuid: str | Unset = UNSET
    account_id: str | Unset = UNSET
    name: str | Unset = UNSET
    created_by: EmbeddedUser | Unset = UNSET
    created_by_ng_user: Principal | Unset = UNSET
    created_at: int | Unset = UNSET
    status: DelegateTokenDetailsStatus | Unset = UNSET
    value: str | Unset = UNSET
    owner_identifier: str | Unset = UNSET
    parent_unique_id: str | Unset = UNSET
    revoke_after: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        uuid = self.uuid

        account_id = self.account_id

        name = self.name

        created_by: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        created_by_ng_user: dict[str, Any] | Unset = UNSET
        if not isinstance(self.created_by_ng_user, Unset):
            created_by_ng_user = self.created_by_ng_user.to_dict()

        created_at = self.created_at

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status

        value = self.value

        owner_identifier = self.owner_identifier

        parent_unique_id = self.parent_unique_id

        revoke_after = self.revoke_after

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if uuid is not UNSET:
            field_dict["uuid"] = uuid
        if account_id is not UNSET:
            field_dict["accountId"] = account_id
        if name is not UNSET:
            field_dict["name"] = name
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if created_by_ng_user is not UNSET:
            field_dict["createdByNgUser"] = created_by_ng_user
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if status is not UNSET:
            field_dict["status"] = status
        if value is not UNSET:
            field_dict["value"] = value
        if owner_identifier is not UNSET:
            field_dict["ownerIdentifier"] = owner_identifier
        if parent_unique_id is not UNSET:
            field_dict["parentUniqueId"] = parent_unique_id
        if revoke_after is not UNSET:
            field_dict["revokeAfter"] = revoke_after

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.embedded_user import EmbeddedUser
        from ..models.principal import Principal

        d = dict(src_dict)
        uuid = d.pop("uuid", UNSET)

        account_id = d.pop("accountId", UNSET)

        name = d.pop("name", UNSET)

        _created_by = d.pop("createdBy", UNSET)
        created_by: EmbeddedUser | Unset
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = EmbeddedUser.from_dict(_created_by)

        _created_by_ng_user = d.pop("createdByNgUser", UNSET)
        created_by_ng_user: Principal | Unset
        if isinstance(_created_by_ng_user, Unset):
            created_by_ng_user = UNSET
        else:
            created_by_ng_user = Principal.from_dict(_created_by_ng_user)

        created_at = d.pop("createdAt", UNSET)

        _status = d.pop("status", UNSET)
        status: DelegateTokenDetailsStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = check_delegate_token_details_status(_status)

        value = d.pop("value", UNSET)

        owner_identifier = d.pop("ownerIdentifier", UNSET)

        parent_unique_id = d.pop("parentUniqueId", UNSET)

        revoke_after = d.pop("revokeAfter", UNSET)

        delegate_token_details = cls(
            uuid=uuid,
            account_id=account_id,
            name=name,
            created_by=created_by,
            created_by_ng_user=created_by_ng_user,
            created_at=created_at,
            status=status,
            value=value,
            owner_identifier=owner_identifier,
            parent_unique_id=parent_unique_id,
            revoke_after=revoke_after,
        )

        delegate_token_details.additional_properties = d
        return delegate_token_details

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
