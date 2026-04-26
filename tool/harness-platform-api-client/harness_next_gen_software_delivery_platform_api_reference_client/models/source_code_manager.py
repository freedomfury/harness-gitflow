from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.source_code_manager_type import SourceCodeManagerType, check_source_code_manager_type
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.source_code_manager_authentication import SourceCodeManagerAuthentication


T = TypeVar("T", bound="SourceCodeManager")


@_attrs_define
class SourceCodeManager:
    """This contains details of Source Code Manager

    Attributes:
        name (str): Name of Source Code Manager
        id (str | Unset): Source Code Manager Identifier
        user_identifier (str | Unset): Id of the User
        account_identifier (str | Unset): Account Identifier for the Entity.
        created_at (int | Unset): Time at which this Source Code Manager was created
        last_modified_at (int | Unset): Time at which this Source Code Manager was last Updated
        authentication (SourceCodeManagerAuthentication | Unset): Authentication Details of Source Code Manager
        type_ (SourceCodeManagerType | Unset): Type of SCM
    """

    name: str
    id: str | Unset = UNSET
    user_identifier: str | Unset = UNSET
    account_identifier: str | Unset = UNSET
    created_at: int | Unset = UNSET
    last_modified_at: int | Unset = UNSET
    authentication: SourceCodeManagerAuthentication | Unset = UNSET
    type_: SourceCodeManagerType | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        id = self.id

        user_identifier = self.user_identifier

        account_identifier = self.account_identifier

        created_at = self.created_at

        last_modified_at = self.last_modified_at

        authentication: dict[str, Any] | Unset = UNSET
        if not isinstance(self.authentication, Unset):
            authentication = self.authentication.to_dict()

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if id is not UNSET:
            field_dict["id"] = id
        if user_identifier is not UNSET:
            field_dict["userIdentifier"] = user_identifier
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at
        if last_modified_at is not UNSET:
            field_dict["lastModifiedAt"] = last_modified_at
        if authentication is not UNSET:
            field_dict["authentication"] = authentication
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.source_code_manager_authentication import SourceCodeManagerAuthentication

        d = dict(src_dict)
        name = d.pop("name")

        id = d.pop("id", UNSET)

        user_identifier = d.pop("userIdentifier", UNSET)

        account_identifier = d.pop("accountIdentifier", UNSET)

        created_at = d.pop("createdAt", UNSET)

        last_modified_at = d.pop("lastModifiedAt", UNSET)

        _authentication = d.pop("authentication", UNSET)
        authentication: SourceCodeManagerAuthentication | Unset
        if isinstance(_authentication, Unset):
            authentication = UNSET
        else:
            authentication = SourceCodeManagerAuthentication.from_dict(_authentication)

        _type_ = d.pop("type", UNSET)
        type_: SourceCodeManagerType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = check_source_code_manager_type(_type_)

        source_code_manager = cls(
            name=name,
            id=id,
            user_identifier=user_identifier,
            account_identifier=account_identifier,
            created_at=created_at,
            last_modified_at=last_modified_at,
            authentication=authentication,
            type_=type_,
        )

        source_code_manager.additional_properties = d
        return source_code_manager

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
