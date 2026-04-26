from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_pull_req_review_decision import EnumPullReqReviewDecision
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0


T = TypeVar("T", bound="TypesReviewerEvaluation")


@_attrs_define
class TypesReviewerEvaluation:
    """
    Attributes:
        decision (EnumPullReqReviewDecision | Unset):
        reviewer (None | TypesPrincipalInfoType0 | Unset):
        sha (str | Unset):
        updated (int | Unset):
    """

    decision: EnumPullReqReviewDecision | Unset = UNSET
    reviewer: None | TypesPrincipalInfoType0 | Unset = UNSET
    sha: str | Unset = UNSET
    updated: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0

        decision: str | Unset = UNSET
        if not isinstance(self.decision, Unset):
            decision = self.decision.value

        reviewer: dict[str, Any] | None | Unset
        if isinstance(self.reviewer, Unset):
            reviewer = UNSET
        elif isinstance(self.reviewer, TypesPrincipalInfoType0):
            reviewer = self.reviewer.to_dict()
        else:
            reviewer = self.reviewer

        sha = self.sha

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if decision is not UNSET:
            field_dict["decision"] = decision
        if reviewer is not UNSET:
            field_dict["reviewer"] = reviewer
        if sha is not UNSET:
            field_dict["sha"] = sha
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0

        d = dict(src_dict)
        _decision = d.pop("decision", UNSET)
        decision: EnumPullReqReviewDecision | Unset
        if isinstance(_decision, Unset):
            decision = UNSET
        else:
            decision = EnumPullReqReviewDecision(_decision)

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

        updated = d.pop("updated", UNSET)

        types_reviewer_evaluation = cls(
            decision=decision,
            reviewer=reviewer,
            sha=sha,
            updated=updated,
        )

        types_reviewer_evaluation.additional_properties = d
        return types_reviewer_evaluation

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
