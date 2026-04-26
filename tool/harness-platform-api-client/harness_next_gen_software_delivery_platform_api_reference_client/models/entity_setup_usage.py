from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_detail import EntityDetail
    from ..models.setup_usage_detail import SetupUsageDetail


T = TypeVar("T", bound="EntitySetupUsage")


@_attrs_define
class EntitySetupUsage:
    """This is the view of the Entity Setup Usage defined in Harness

    Attributes:
        referred_by_entity (EntityDetail):
        account_identifier (str | Unset):
        referred_entity (EntityDetail | Unset):
        detail (SetupUsageDetail | Unset):
        created_at (int | Unset):
    """

    referred_by_entity: EntityDetail
    account_identifier: str | Unset = UNSET
    referred_entity: EntityDetail | Unset = UNSET
    detail: SetupUsageDetail | Unset = UNSET
    created_at: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        referred_by_entity = self.referred_by_entity.to_dict()

        account_identifier = self.account_identifier

        referred_entity: dict[str, Any] | Unset = UNSET
        if not isinstance(self.referred_entity, Unset):
            referred_entity = self.referred_entity.to_dict()

        detail: dict[str, Any] | Unset = UNSET
        if not isinstance(self.detail, Unset):
            detail = self.detail.to_dict()

        created_at = self.created_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "referredByEntity": referred_by_entity,
            }
        )
        if account_identifier is not UNSET:
            field_dict["accountIdentifier"] = account_identifier
        if referred_entity is not UNSET:
            field_dict["referredEntity"] = referred_entity
        if detail is not UNSET:
            field_dict["detail"] = detail
        if created_at is not UNSET:
            field_dict["createdAt"] = created_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.entity_detail import EntityDetail
        from ..models.setup_usage_detail import SetupUsageDetail

        d = dict(src_dict)
        referred_by_entity = EntityDetail.from_dict(d.pop("referredByEntity"))

        account_identifier = d.pop("accountIdentifier", UNSET)

        _referred_entity = d.pop("referredEntity", UNSET)
        referred_entity: EntityDetail | Unset
        if isinstance(_referred_entity, Unset):
            referred_entity = UNSET
        else:
            referred_entity = EntityDetail.from_dict(_referred_entity)

        _detail = d.pop("detail", UNSET)
        detail: SetupUsageDetail | Unset
        if isinstance(_detail, Unset):
            detail = UNSET
        else:
            detail = SetupUsageDetail.from_dict(_detail)

        created_at = d.pop("createdAt", UNSET)

        entity_setup_usage = cls(
            referred_by_entity=referred_by_entity,
            account_identifier=account_identifier,
            referred_entity=referred_entity,
            detail=detail,
            created_at=created_at,
        )

        entity_setup_usage.additional_properties = d
        return entity_setup_usage

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
