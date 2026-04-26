from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_merge_method import EnumMergeMethod
from ..models.enum_pull_req_state import EnumPullReqState
from ..models.enum_pull_req_sub_state import EnumPullReqSubState
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_check_count_summary import TypesCheckCountSummary
    from ..models.types_label_pull_req_assignment_info import TypesLabelPullReqAssignmentInfo
    from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0
    from ..models.types_pull_req_stats import TypesPullReqStats
    from ..models.types_repository_core import TypesRepositoryCore
    from ..models.types_rule_info import TypesRuleInfo


T = TypeVar("T", bound="TypesPullReq")


@_attrs_define
class TypesPullReq:
    """
    Attributes:
        author (None | TypesPrincipalInfoType0 | Unset):
        check_summary (TypesCheckCountSummary | Unset):
        closed (int | None | Unset):
        created (int | Unset):
        description (str | Unset):
        edited (int | Unset):
        is_draft (bool | Unset):
        labels (list[TypesLabelPullReqAssignmentInfo] | Unset):
        merge_base_sha (str | Unset):
        merge_check_status (str | Unset):
        merge_conflicts (list[str] | Unset):
        merge_method (EnumMergeMethod | Unset):
        merge_target_sha (None | str | Unset):
        merge_violations_bypassed (bool | None | Unset):
        merged (int | None | Unset):
        merger (None | TypesPrincipalInfoType0 | Unset):
        number (int | Unset):
        rebase_check_status (str | Unset):
        rebase_conflicts (list[str] | Unset):
        rules (list[TypesRuleInfo] | Unset):
        source_branch (str | Unset):
        source_repo (TypesRepositoryCore | Unset):
        source_repo_id (int | None | Unset):
        source_sha (str | Unset):
        state (EnumPullReqState | Unset):
        stats (TypesPullReqStats | Unset):
        substate (EnumPullReqSubState | Unset):
        target_branch (str | Unset):
        target_repo_id (int | Unset):
        title (str | Unset):
        updated (int | Unset):
    """

    author: None | TypesPrincipalInfoType0 | Unset = UNSET
    check_summary: TypesCheckCountSummary | Unset = UNSET
    closed: int | None | Unset = UNSET
    created: int | Unset = UNSET
    description: str | Unset = UNSET
    edited: int | Unset = UNSET
    is_draft: bool | Unset = UNSET
    labels: list[TypesLabelPullReqAssignmentInfo] | Unset = UNSET
    merge_base_sha: str | Unset = UNSET
    merge_check_status: str | Unset = UNSET
    merge_conflicts: list[str] | Unset = UNSET
    merge_method: EnumMergeMethod | Unset = UNSET
    merge_target_sha: None | str | Unset = UNSET
    merge_violations_bypassed: bool | None | Unset = UNSET
    merged: int | None | Unset = UNSET
    merger: None | TypesPrincipalInfoType0 | Unset = UNSET
    number: int | Unset = UNSET
    rebase_check_status: str | Unset = UNSET
    rebase_conflicts: list[str] | Unset = UNSET
    rules: list[TypesRuleInfo] | Unset = UNSET
    source_branch: str | Unset = UNSET
    source_repo: TypesRepositoryCore | Unset = UNSET
    source_repo_id: int | None | Unset = UNSET
    source_sha: str | Unset = UNSET
    state: EnumPullReqState | Unset = UNSET
    stats: TypesPullReqStats | Unset = UNSET
    substate: EnumPullReqSubState | Unset = UNSET
    target_branch: str | Unset = UNSET
    target_repo_id: int | Unset = UNSET
    title: str | Unset = UNSET
    updated: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0

        author: dict[str, Any] | None | Unset
        if isinstance(self.author, Unset):
            author = UNSET
        elif isinstance(self.author, TypesPrincipalInfoType0):
            author = self.author.to_dict()
        else:
            author = self.author

        check_summary: dict[str, Any] | Unset = UNSET
        if not isinstance(self.check_summary, Unset):
            check_summary = self.check_summary.to_dict()

        closed: int | None | Unset
        if isinstance(self.closed, Unset):
            closed = UNSET
        else:
            closed = self.closed

        created = self.created

        description = self.description

        edited = self.edited

        is_draft = self.is_draft

        labels: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.labels, Unset):
            labels = []
            for labels_item_data in self.labels:
                labels_item = labels_item_data.to_dict()
                labels.append(labels_item)

        merge_base_sha = self.merge_base_sha

        merge_check_status = self.merge_check_status

        merge_conflicts: list[str] | Unset = UNSET
        if not isinstance(self.merge_conflicts, Unset):
            merge_conflicts = self.merge_conflicts

        merge_method: str | Unset = UNSET
        if not isinstance(self.merge_method, Unset):
            merge_method = self.merge_method.value

        merge_target_sha: None | str | Unset
        if isinstance(self.merge_target_sha, Unset):
            merge_target_sha = UNSET
        else:
            merge_target_sha = self.merge_target_sha

        merge_violations_bypassed: bool | None | Unset
        if isinstance(self.merge_violations_bypassed, Unset):
            merge_violations_bypassed = UNSET
        else:
            merge_violations_bypassed = self.merge_violations_bypassed

        merged: int | None | Unset
        if isinstance(self.merged, Unset):
            merged = UNSET
        else:
            merged = self.merged

        merger: dict[str, Any] | None | Unset
        if isinstance(self.merger, Unset):
            merger = UNSET
        elif isinstance(self.merger, TypesPrincipalInfoType0):
            merger = self.merger.to_dict()
        else:
            merger = self.merger

        number = self.number

        rebase_check_status = self.rebase_check_status

        rebase_conflicts: list[str] | Unset = UNSET
        if not isinstance(self.rebase_conflicts, Unset):
            rebase_conflicts = self.rebase_conflicts

        rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.rules, Unset):
            rules = []
            for rules_item_data in self.rules:
                rules_item = rules_item_data.to_dict()
                rules.append(rules_item)

        source_branch = self.source_branch

        source_repo: dict[str, Any] | Unset = UNSET
        if not isinstance(self.source_repo, Unset):
            source_repo = self.source_repo.to_dict()

        source_repo_id: int | None | Unset
        if isinstance(self.source_repo_id, Unset):
            source_repo_id = UNSET
        else:
            source_repo_id = self.source_repo_id

        source_sha = self.source_sha

        state: str | Unset = UNSET
        if not isinstance(self.state, Unset):
            state = self.state.value

        stats: dict[str, Any] | Unset = UNSET
        if not isinstance(self.stats, Unset):
            stats = self.stats.to_dict()

        substate: str | Unset = UNSET
        if not isinstance(self.substate, Unset):
            substate = self.substate.value

        target_branch = self.target_branch

        target_repo_id = self.target_repo_id

        title = self.title

        updated = self.updated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if author is not UNSET:
            field_dict["author"] = author
        if check_summary is not UNSET:
            field_dict["check_summary"] = check_summary
        if closed is not UNSET:
            field_dict["closed"] = closed
        if created is not UNSET:
            field_dict["created"] = created
        if description is not UNSET:
            field_dict["description"] = description
        if edited is not UNSET:
            field_dict["edited"] = edited
        if is_draft is not UNSET:
            field_dict["is_draft"] = is_draft
        if labels is not UNSET:
            field_dict["labels"] = labels
        if merge_base_sha is not UNSET:
            field_dict["merge_base_sha"] = merge_base_sha
        if merge_check_status is not UNSET:
            field_dict["merge_check_status"] = merge_check_status
        if merge_conflicts is not UNSET:
            field_dict["merge_conflicts"] = merge_conflicts
        if merge_method is not UNSET:
            field_dict["merge_method"] = merge_method
        if merge_target_sha is not UNSET:
            field_dict["merge_target_sha"] = merge_target_sha
        if merge_violations_bypassed is not UNSET:
            field_dict["merge_violations_bypassed"] = merge_violations_bypassed
        if merged is not UNSET:
            field_dict["merged"] = merged
        if merger is not UNSET:
            field_dict["merger"] = merger
        if number is not UNSET:
            field_dict["number"] = number
        if rebase_check_status is not UNSET:
            field_dict["rebase_check_status"] = rebase_check_status
        if rebase_conflicts is not UNSET:
            field_dict["rebase_conflicts"] = rebase_conflicts
        if rules is not UNSET:
            field_dict["rules"] = rules
        if source_branch is not UNSET:
            field_dict["source_branch"] = source_branch
        if source_repo is not UNSET:
            field_dict["source_repo"] = source_repo
        if source_repo_id is not UNSET:
            field_dict["source_repo_id"] = source_repo_id
        if source_sha is not UNSET:
            field_dict["source_sha"] = source_sha
        if state is not UNSET:
            field_dict["state"] = state
        if stats is not UNSET:
            field_dict["stats"] = stats
        if substate is not UNSET:
            field_dict["substate"] = substate
        if target_branch is not UNSET:
            field_dict["target_branch"] = target_branch
        if target_repo_id is not UNSET:
            field_dict["target_repo_id"] = target_repo_id
        if title is not UNSET:
            field_dict["title"] = title
        if updated is not UNSET:
            field_dict["updated"] = updated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_check_count_summary import TypesCheckCountSummary
        from ..models.types_label_pull_req_assignment_info import TypesLabelPullReqAssignmentInfo
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0
        from ..models.types_pull_req_stats import TypesPullReqStats
        from ..models.types_repository_core import TypesRepositoryCore
        from ..models.types_rule_info import TypesRuleInfo

        d = dict(src_dict)

        def _parse_author(data: object) -> None | TypesPrincipalInfoType0 | Unset:
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

        author = _parse_author(d.pop("author", UNSET))

        _check_summary = d.pop("check_summary", UNSET)
        check_summary: TypesCheckCountSummary | Unset
        if isinstance(_check_summary, Unset):
            check_summary = UNSET
        else:
            check_summary = TypesCheckCountSummary.from_dict(_check_summary)

        def _parse_closed(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        closed = _parse_closed(d.pop("closed", UNSET))

        created = d.pop("created", UNSET)

        description = d.pop("description", UNSET)

        edited = d.pop("edited", UNSET)

        is_draft = d.pop("is_draft", UNSET)

        _labels = d.pop("labels", UNSET)
        labels: list[TypesLabelPullReqAssignmentInfo] | Unset = UNSET
        if _labels is not UNSET:
            labels = []
            for labels_item_data in _labels:
                labels_item = TypesLabelPullReqAssignmentInfo.from_dict(labels_item_data)

                labels.append(labels_item)

        merge_base_sha = d.pop("merge_base_sha", UNSET)

        merge_check_status = d.pop("merge_check_status", UNSET)

        merge_conflicts = cast(list[str], d.pop("merge_conflicts", UNSET))

        _merge_method = d.pop("merge_method", UNSET)
        merge_method: EnumMergeMethod | Unset
        if isinstance(_merge_method, Unset):
            merge_method = UNSET
        else:
            merge_method = EnumMergeMethod(_merge_method)

        def _parse_merge_target_sha(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        merge_target_sha = _parse_merge_target_sha(d.pop("merge_target_sha", UNSET))

        def _parse_merge_violations_bypassed(data: object) -> bool | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(bool | None | Unset, data)

        merge_violations_bypassed = _parse_merge_violations_bypassed(d.pop("merge_violations_bypassed", UNSET))

        def _parse_merged(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        merged = _parse_merged(d.pop("merged", UNSET))

        def _parse_merger(data: object) -> None | TypesPrincipalInfoType0 | Unset:
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

        merger = _parse_merger(d.pop("merger", UNSET))

        number = d.pop("number", UNSET)

        rebase_check_status = d.pop("rebase_check_status", UNSET)

        rebase_conflicts = cast(list[str], d.pop("rebase_conflicts", UNSET))

        _rules = d.pop("rules", UNSET)
        rules: list[TypesRuleInfo] | Unset = UNSET
        if _rules is not UNSET:
            rules = []
            for rules_item_data in _rules:
                rules_item = TypesRuleInfo.from_dict(rules_item_data)

                rules.append(rules_item)

        source_branch = d.pop("source_branch", UNSET)

        _source_repo = d.pop("source_repo", UNSET)
        source_repo: TypesRepositoryCore | Unset
        if isinstance(_source_repo, Unset):
            source_repo = UNSET
        else:
            source_repo = TypesRepositoryCore.from_dict(_source_repo)

        def _parse_source_repo_id(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        source_repo_id = _parse_source_repo_id(d.pop("source_repo_id", UNSET))

        source_sha = d.pop("source_sha", UNSET)

        _state = d.pop("state", UNSET)
        state: EnumPullReqState | Unset
        if isinstance(_state, Unset):
            state = UNSET
        else:
            state = EnumPullReqState(_state)

        _stats = d.pop("stats", UNSET)
        stats: TypesPullReqStats | Unset
        if isinstance(_stats, Unset):
            stats = UNSET
        else:
            stats = TypesPullReqStats.from_dict(_stats)

        _substate = d.pop("substate", UNSET)
        substate: EnumPullReqSubState | Unset
        if isinstance(_substate, Unset):
            substate = UNSET
        else:
            substate = EnumPullReqSubState(_substate)

        target_branch = d.pop("target_branch", UNSET)

        target_repo_id = d.pop("target_repo_id", UNSET)

        title = d.pop("title", UNSET)

        updated = d.pop("updated", UNSET)

        types_pull_req = cls(
            author=author,
            check_summary=check_summary,
            closed=closed,
            created=created,
            description=description,
            edited=edited,
            is_draft=is_draft,
            labels=labels,
            merge_base_sha=merge_base_sha,
            merge_check_status=merge_check_status,
            merge_conflicts=merge_conflicts,
            merge_method=merge_method,
            merge_target_sha=merge_target_sha,
            merge_violations_bypassed=merge_violations_bypassed,
            merged=merged,
            merger=merger,
            number=number,
            rebase_check_status=rebase_check_status,
            rebase_conflicts=rebase_conflicts,
            rules=rules,
            source_branch=source_branch,
            source_repo=source_repo,
            source_repo_id=source_repo_id,
            source_sha=source_sha,
            state=state,
            stats=stats,
            substate=substate,
            target_branch=target_branch,
            target_repo_id=target_repo_id,
            title=title,
            updated=updated,
        )

        types_pull_req.additional_properties = d
        return types_pull_req

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
