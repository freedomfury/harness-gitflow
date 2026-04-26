from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_check_count_summary import TypesCheckCountSummary
    from ..models.types_commit import TypesCommit
    from ..models.types_commit_divergence import TypesCommitDivergence
    from ..models.types_pull_req import TypesPullReq
    from ..models.types_rule_info import TypesRuleInfo


T = TypeVar("T", bound="TypesBranchExtended")


@_attrs_define
class TypesBranchExtended:
    """
    Attributes:
        check_summary (TypesCheckCountSummary | Unset):
        commit (TypesCommit | Unset):
        commit_divergence (TypesCommitDivergence | Unset):
        is_default (bool | Unset):
        name (str | Unset):
        pull_requests (list[TypesPullReq] | Unset):
        rules (list[TypesRuleInfo] | Unset):
        sha (str | Unset): Git object hash
    """

    check_summary: TypesCheckCountSummary | Unset = UNSET
    commit: TypesCommit | Unset = UNSET
    commit_divergence: TypesCommitDivergence | Unset = UNSET
    is_default: bool | Unset = UNSET
    name: str | Unset = UNSET
    pull_requests: list[TypesPullReq] | Unset = UNSET
    rules: list[TypesRuleInfo] | Unset = UNSET
    sha: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        check_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.check_summary, Unset):
            check_summary = self.check_summary.to_dict()

        commit: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commit, Unset):
            commit = self.commit.to_dict()

        commit_divergence: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commit_divergence, Unset):
            commit_divergence = self.commit_divergence.to_dict()

        is_default = self.is_default

        name = self.name

        pull_requests: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.pull_requests, Unset):
            pull_requests = []
            for pull_requests_item_data in self.pull_requests:
                pull_requests_item = pull_requests_item_data.to_dict()
                pull_requests.append(pull_requests_item)

        rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        sha = self.sha

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if check_summary is not UNSET:
            field_dict["check_summary"] = check_summary
        if commit is not UNSET:
            field_dict["commit"] = commit
        if commit_divergence is not UNSET:
            field_dict["commit_divergence"] = commit_divergence
        if is_default is not UNSET:
            field_dict["is_default"] = is_default
        if name is not UNSET:
            field_dict["name"] = name
        if pull_requests is not UNSET:
            field_dict["pull_requests"] = pull_requests
        if rules is not UNSET:
            field_dict["rules"] = rules
        if sha is not UNSET:
            field_dict["sha"] = sha

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_check_count_summary import TypesCheckCountSummary
        from ..models.types_commit import TypesCommit
        from ..models.types_commit_divergence import TypesCommitDivergence
        from ..models.types_pull_req import TypesPullReq
        from ..models.types_rule_info import TypesRuleInfo

        d = dict(src_dict)
        _check_summary = d.pop("check_summary", UNSET)
        check_summary: TypesCheckCountSummary | Unset
        if isinstance(_check_summary, Unset):
            check_summary = UNSET
        else:
            check_summary = TypesCheckCountSummary.from_dict(_check_summary)

        _commit = d.pop("commit", UNSET)
        commit: TypesCommit | Unset
        if isinstance(_commit, Unset):
            commit = UNSET
        else:
            commit = TypesCommit.from_dict(_commit)

        _commit_divergence = d.pop("commit_divergence", UNSET)
        commit_divergence: TypesCommitDivergence | Unset
        if isinstance(_commit_divergence, Unset):
            commit_divergence = UNSET
        else:
            commit_divergence = TypesCommitDivergence.from_dict(_commit_divergence)

        is_default = d.pop("is_default", UNSET)

        name = d.pop("name", UNSET)

        _pull_requests = d.pop("pull_requests", UNSET)
        pull_requests: list[TypesPullReq] | Unset = UNSET
        if _pull_requests is not UNSET:
            pull_requests = []
            for pull_requests_item_data in _pull_requests:
                pull_requests_item = TypesPullReq.from_dict(pull_requests_item_data)

                pull_requests.append(pull_requests_item)

        _rules = d.pop("rules", UNSET)
        rules: list[TypesRuleInfo] | Unset = UNSET
        if _rules is not UNSET:
            rules = []
            for rules_item_data in _rules:
                rules_item = TypesRuleInfo.from_dict(rules_item_data)

                rules.append(rules_item)

        sha = d.pop("sha", UNSET)

        types_branch_extended = cls(
            check_summary=check_summary,
            commit=commit,
            commit_divergence=commit_divergence,
            is_default=is_default,
            name=name,
            pull_requests=pull_requests,
            rules=rules,
            sha=sha,
        )

        types_branch_extended.additional_properties = d
        return types_branch_extended

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
