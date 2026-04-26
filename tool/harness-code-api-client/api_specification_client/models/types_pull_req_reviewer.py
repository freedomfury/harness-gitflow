from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_pull_req_review_decision import EnumPullReqReviewDecision
from ..models.enum_pull_req_reviewer_type import EnumPullReqReviewerType
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0


T = TypeVar("T", bound="TypesPullReqReviewer")


@_attrs_define
class TypesPullReqReviewer:
    """
    Attributes:
        added_by (None | TypesPrincipalInfoType0 | Unset):
        created (int | Unset):
        latest_review_id (int | None | Unset):
        review_decision (EnumPullReqReviewDecision | Unset):
        reviewer (None | TypesPrincipalInfoType0 | Unset):
        sha (str | Unset):
        type_ (EnumPullReqReviewerType | Unset):
        updated (int | Unset):
    """

    added_by: None | TypesPrincipalInfoType0 | Unset = UNSET
    created: int | Unset = UNSET
    latest_review_id: int | None | Unset = UNSET
    review_decision: EnumPullReqReviewDecision | Unset = UNSET
    reviewer: None | TypesPrincipalInfoType0 | Unset = UNSET
    sha: str | Unset = UNSET
    type_: EnumPullReqReviewerType | Unset = UNSET
    updated: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0

        added_by: dict[str, Any] | None | Unset
        if isinstance(self.added_by, Unset):
            added_by = UNSET
        elif isinstance(self.added_by, TypesPrincipalInfoType0):
            added_by = self.added_by.to_dict()
        else:
            added_by = self.added_by

        created = self.created

        latest_review_id: int | None | Unset
        if isinstance(self.latest_review_id, Unset):
            latest_review_id = UNSET
        else:
            latest_review_id = self.latest_review_id

        review_decision: str | Unset = UNSET
        if not isinstance(self.review_decision, Unset):
            review_decision = self.review_decision.value

        reviewer: dict[str, Any] | None | Unset
        if isinstance(self.reviewer, Unset):
            reviewer = UNSET
        elif isinstance(self.reviewer, TypesPrincipalInfoType0):
            reviewer = self.reviewer.to_dict()
        else:
            reviewer = self.reviewer

        sha = self.sha

        type_: str | Unset = UNSET
        if not isinstance(self.type_, Unset):
            type_ = self.type_.value

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if added_by is not UNSET:
            field_dict["added_by"] = added_by
        if created is not UNSET:
            field_dict["created"] = created
        if latest_review_id is not UNSET:
            field_dict["latest_review_id"] = latest_review_id
        if review_decision is not UNSET:
            field_dict["review_decision"] = review_decision
        if reviewer is not UNSET:
            field_dict["reviewer"] = reviewer
        if sha is not UNSET:
            field_dict["sha"] = sha
        if type_ is not UNSET:
            field_dict["type"] = type_
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0

        d = dict(src_dict)

        def _parse_added_by(data: object) -> None | TypesPrincipalInfoType0 | Unset:
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

        added_by = _parse_added_by(d.pop("added_by", UNSET))

        created = d.pop("created", UNSET)

        def _parse_latest_review_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        latest_review_id = _parse_latest_review_id(d.pop("latest_review_id", UNSET))

        _review_decision = d.pop("review_decision", UNSET)
        review_decision: EnumPullReqReviewDecision | Unset
        if isinstance(_review_decision, Unset):
            review_decision = UNSET
        else:
            review_decision = EnumPullReqReviewDecision(_review_decision)

        def _parse_reviewer(data: object) -> None | TypesPrincipalInfoType0 | Unset:
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

        reviewer = _parse_reviewer(d.pop("reviewer", UNSET))

        sha = d.pop("sha", UNSET)

        _type_ = d.pop("type", UNSET)
        type_: EnumPullReqReviewerType | Unset
        if isinstance(_type_, Unset):
            type_ = UNSET
        else:
            type_ = EnumPullReqReviewerType(_type_)

        updated = d.pop("updated", UNSET)

        types_pull_req_reviewer = cls(
            added_by=added_by,
            created=created,
            latest_review_id=latest_review_id,
            review_decision=review_decision,
            reviewer=reviewer,
            sha=sha,
            type_=type_,
            updated=updated,
        )

        types_pull_req_reviewer.additional_properties = d
        return types_pull_req_reviewer

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
