from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_pull_req_reviewer import TypesPullReqReviewer
    from ..models.types_user_group_reviewer import TypesUserGroupReviewer


T = TypeVar("T", bound="PullreqCombinedListResponse")


@_attrs_define
class PullreqCombinedListResponse:
    """
    Attributes:
        reviewers (list[TypesPullReqReviewer] | Unset):
        user_group_reviewers (list[TypesUserGroupReviewer] | Unset):
    """

    reviewers: list[TypesPullReqReviewer] | Unset = UNSET
    user_group_reviewers: list[TypesUserGroupReviewer] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        reviewers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.reviewers, Unset):
            reviewers = []
            for reviewers_item_data in self.reviewers:
                reviewers_item = reviewers_item_data.to_dict()
                reviewers.append(reviewers_item)

        user_group_reviewers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user_group_reviewers, Unset):
            user_group_reviewers = []
            for user_group_reviewers_item_data in self.user_group_reviewers:
                user_group_reviewers_item = user_group_reviewers_item_data.to_dict()
                user_group_reviewers.append(user_group_reviewers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reviewers is not UNSET:
            field_dict["reviewers"] = reviewers
        if user_group_reviewers is not UNSET:
            field_dict["user_group_reviewers"] = user_group_reviewers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_pull_req_reviewer import TypesPullReqReviewer
        from ..models.types_user_group_reviewer import TypesUserGroupReviewer

        d = dict(src_dict)
        _reviewers = d.pop("reviewers", UNSET)
        reviewers: list[TypesPullReqReviewer] | Unset = UNSET
        if _reviewers is not UNSET:
            reviewers = []
            for reviewers_item_data in _reviewers:
                reviewers_item = TypesPullReqReviewer.from_dict(reviewers_item_data)

                reviewers.append(reviewers_item)

        _user_group_reviewers = d.pop("user_group_reviewers", UNSET)
        user_group_reviewers: list[TypesUserGroupReviewer] | Unset = UNSET
        if _user_group_reviewers is not UNSET:
            user_group_reviewers = []
            for user_group_reviewers_item_data in _user_group_reviewers:
                user_group_reviewers_item = TypesUserGroupReviewer.from_dict(user_group_reviewers_item_data)

                user_group_reviewers.append(user_group_reviewers_item)

        pullreq_combined_list_response = cls(
            reviewers=reviewers,
            user_group_reviewers=user_group_reviewers,
        )

        pullreq_combined_list_response.additional_properties = d
        return pullreq_combined_list_response

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
