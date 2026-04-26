from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_pull_req_review_decision import EnumPullReqReviewDecision
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0
    from ..models.types_reviewer_evaluation import TypesReviewerEvaluation
    from ..models.types_user_group_info import TypesUserGroupInfo


T = TypeVar("T", bound="TypesUserGroupReviewer")


@_attrs_define
class TypesUserGroupReviewer:
    """
    Attributes:
        added_by (None | TypesPrincipalInfoType0 | Unset):
        created (int | Unset):
        decision (EnumPullReqReviewDecision | Unset):
        sha (str | Unset):
        updated (int | Unset):
        user_decisions (list[TypesReviewerEvaluation] | Unset):
        user_group (TypesUserGroupInfo | Unset):
    """

    added_by: None | TypesPrincipalInfoType0 | Unset = UNSET
    created: int | Unset = UNSET
    decision: EnumPullReqReviewDecision | Unset = UNSET
    sha: str | Unset = UNSET
    updated: int | Unset = UNSET
    user_decisions: list[TypesReviewerEvaluation] | Unset = UNSET
    user_group: TypesUserGroupInfo | Unset = UNSET
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

        decision: str | Unset = UNSET
        if not isinstance(self.decision, Unset):
            decision = self.decision.value

        sha = self.sha

        updated = self.updated

        user_decisions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.user_decisions, Unset):
            user_decisions = []
            for user_decisions_item_data in self.user_decisions:
                user_decisions_item = user_decisions_item_data.to_dict()
                user_decisions.append(user_decisions_item)

        user_group: dict[str, Any] | Unset = UNSET
        if not isinstance(self.user_group, Unset):
            user_group = self.user_group.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if added_by is not UNSET:
            field_dict["added_by"] = added_by
        if created is not UNSET:
            field_dict["created"] = created
        if decision is not UNSET:
            field_dict["decision"] = decision
        if sha is not UNSET:
            field_dict["sha"] = sha
        if updated is not UNSET:
            field_dict["updated"] = updated
        if user_decisions is not UNSET:
            field_dict["user_decisions"] = user_decisions
        if user_group is not UNSET:
            field_dict["user_group"] = user_group

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0
        from ..models.types_reviewer_evaluation import TypesReviewerEvaluation
        from ..models.types_user_group_info import TypesUserGroupInfo

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

        _decision = d.pop("decision", UNSET)
        decision: EnumPullReqReviewDecision | Unset
        if isinstance(_decision, Unset):
            decision = UNSET
        else:
            decision = EnumPullReqReviewDecision(_decision)

        sha = d.pop("sha", UNSET)

        updated = d.pop("updated", UNSET)

        _user_decisions = d.pop("user_decisions", UNSET)
        user_decisions: list[TypesReviewerEvaluation] | Unset = UNSET
        if _user_decisions is not UNSET:
            user_decisions = []
            for user_decisions_item_data in _user_decisions:
                user_decisions_item = TypesReviewerEvaluation.from_dict(user_decisions_item_data)

                user_decisions.append(user_decisions_item)

        _user_group = d.pop("user_group", UNSET)
        user_group: TypesUserGroupInfo | Unset
        if isinstance(_user_group, Unset):
            user_group = UNSET
        else:
            user_group = TypesUserGroupInfo.from_dict(_user_group)

        types_user_group_reviewer = cls(
            added_by=added_by,
            created=created,
            decision=decision,
            sha=sha,
            updated=updated,
            user_decisions=user_decisions,
            user_group=user_group,
        )

        types_user_group_reviewer.additional_properties = d
        return types_user_group_reviewer

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
