from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_pull_req_review_decision import EnumPullReqReviewDecision
from ..types import UNSET, Unset

T = TypeVar("T", bound="OpenapiReviewSubmitPullReqRequest")


@_attrs_define
class OpenapiReviewSubmitPullReqRequest:
    """
    Attributes:
        commit_sha (str | Unset):
        decision (EnumPullReqReviewDecision | Unset):
    """

    commit_sha: str | Unset = UNSET
    decision: EnumPullReqReviewDecision | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        commit_sha = self.commit_sha

        decision: str | Unset = UNSET
        if not isinstance(self.decision, Unset):
            decision = self.decision.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if commit_sha is not UNSET:
            field_dict["commit_sha"] = commit_sha
        if decision is not UNSET:
            field_dict["decision"] = decision

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        commit_sha = d.pop("commit_sha", UNSET)

        _decision = d.pop("decision", UNSET)
        decision: EnumPullReqReviewDecision | Unset
        if isinstance(_decision, Unset):
            decision = UNSET
        else:
            decision = EnumPullReqReviewDecision(_decision)

        openapi_review_submit_pull_req_request = cls(
            commit_sha=commit_sha,
            decision=decision,
        )

        openapi_review_submit_pull_req_request.additional_properties = d
        return openapi_review_submit_pull_req_request

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
