from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.post_prod_rollback_swim_lane_info import PostProdRollbackSwimLaneInfo


T = TypeVar("T", bound="PostProdRollbackCheckDTO")


@_attrs_define
class PostProdRollbackCheckDTO:
    """
    Attributes:
        is_rollback_allowed (bool | Unset):
        message (str | Unset):
        swim_lane_info (PostProdRollbackSwimLaneInfo | Unset):
        rollback_allowed (bool | Unset):
    """

    is_rollback_allowed: bool | Unset = UNSET
    message: str | Unset = UNSET
    swim_lane_info: PostProdRollbackSwimLaneInfo | Unset = UNSET
    rollback_allowed: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        is_rollback_allowed = self.is_rollback_allowed

        message = self.message

        swim_lane_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.swim_lane_info, Unset):
            swim_lane_info = self.swim_lane_info.to_dict()

        rollback_allowed = self.rollback_allowed

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if is_rollback_allowed is not UNSET:
            field_dict["isRollbackAllowed"] = is_rollback_allowed
        if message is not UNSET:
            field_dict["message"] = message
        if swim_lane_info is not UNSET:
            field_dict["swimLaneInfo"] = swim_lane_info
        if rollback_allowed is not UNSET:
            field_dict["rollbackAllowed"] = rollback_allowed

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.post_prod_rollback_swim_lane_info import PostProdRollbackSwimLaneInfo

        d = dict(src_dict)
        is_rollback_allowed = d.pop("isRollbackAllowed", UNSET)

        message = d.pop("message", UNSET)

        _swim_lane_info = d.pop("swimLaneInfo", UNSET)
        swim_lane_info: PostProdRollbackSwimLaneInfo | Unset
        if isinstance(_swim_lane_info, Unset):
            swim_lane_info = UNSET
        else:
            swim_lane_info = PostProdRollbackSwimLaneInfo.from_dict(_swim_lane_info)

        rollback_allowed = d.pop("rollbackAllowed", UNSET)

        post_prod_rollback_check_dto = cls(
            is_rollback_allowed=is_rollback_allowed,
            message=message,
            swim_lane_info=swim_lane_info,
            rollback_allowed=rollback_allowed,
        )

        post_prod_rollback_check_dto.additional_properties = d
        return post_prod_rollback_check_dto

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
