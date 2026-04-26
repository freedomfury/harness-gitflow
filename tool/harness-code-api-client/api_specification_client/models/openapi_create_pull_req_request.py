from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_pull_req_label_assign_input import TypesPullReqLabelAssignInput


T = TypeVar("T", bound="OpenapiCreatePullReqRequest")


@_attrs_define
class OpenapiCreatePullReqRequest:
    """
    Attributes:
        bypass_rules (bool | Unset):
        description (str | Unset):
        is_draft (bool | Unset):
        labels (list[TypesPullReqLabelAssignInput] | None | Unset):
        reviewer_ids (list[int] | None | Unset):
        source_branch (str | Unset):
        source_repo_ref (str | Unset):
        target_branch (str | Unset):
        title (str | Unset):
        user_group_reviewer_ids (list[int] | None | Unset):
    """

    bypass_rules: bool | Unset = UNSET
    description: str | Unset = UNSET
    is_draft: bool | Unset = UNSET
    labels: list[TypesPullReqLabelAssignInput] | None | Unset = UNSET
    reviewer_ids: list[int] | None | Unset = UNSET
    source_branch: str | Unset = UNSET
    source_repo_ref: str | Unset = UNSET
    target_branch: str | Unset = UNSET
    title: str | Unset = UNSET
    user_group_reviewer_ids: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        bypass_rules = self.bypass_rules

        description = self.description

        is_draft = self.is_draft

        labels: list[dict[str, Any]] | None | Unset
        if isinstance(self.labels, Unset):
            labels = UNSET
        elif isinstance(self.labels, list):
            labels = []
            for labels_type_0_item_data in self.labels:
                labels_type_0_item = labels_type_0_item_data.to_dict()
                labels.append(labels_type_0_item)

        else:
            labels = self.labels

        reviewer_ids: list[int] | None | Unset
        if isinstance(self.reviewer_ids, Unset):
            reviewer_ids = UNSET
        elif isinstance(self.reviewer_ids, list):
            reviewer_ids = self.reviewer_ids

        else:
            reviewer_ids = self.reviewer_ids

        source_branch = self.source_branch

        source_repo_ref = self.source_repo_ref

        target_branch = self.target_branch

        title = self.title

        user_group_reviewer_ids: list[int] | None | Unset
        if isinstance(self.user_group_reviewer_ids, Unset):
            user_group_reviewer_ids = UNSET
        elif isinstance(self.user_group_reviewer_ids, list):
            user_group_reviewer_ids = self.user_group_reviewer_ids

        else:
            user_group_reviewer_ids = self.user_group_reviewer_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if bypass_rules is not UNSET:
            field_dict["bypass_rules"] = bypass_rules
        if description is not UNSET:
            field_dict["description"] = description
        if is_draft is not UNSET:
            field_dict["is_draft"] = is_draft
        if labels is not UNSET:
            field_dict["labels"] = labels
        if reviewer_ids is not UNSET:
            field_dict["reviewer_ids"] = reviewer_ids
        if source_branch is not UNSET:
            field_dict["source_branch"] = source_branch
        if source_repo_ref is not UNSET:
            field_dict["source_repo_ref"] = source_repo_ref
        if target_branch is not UNSET:
            field_dict["target_branch"] = target_branch
        if title is not UNSET:
            field_dict["title"] = title
        if user_group_reviewer_ids is not UNSET:
            field_dict["user_group_reviewer_ids"] = user_group_reviewer_ids

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_pull_req_label_assign_input import TypesPullReqLabelAssignInput

        d = dict(src_dict)
        bypass_rules = d.pop("bypass_rules", UNSET)

        description = d.pop("description", UNSET)

        is_draft = d.pop("is_draft", UNSET)

        def _parse_labels(data: object) -> list[TypesPullReqLabelAssignInput] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                labels_type_0 = []
                _labels_type_0 = data
                for labels_type_0_item_data in _labels_type_0:
                    labels_type_0_item = TypesPullReqLabelAssignInput.from_dict(labels_type_0_item_data)

                    labels_type_0.append(labels_type_0_item)

                return labels_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TypesPullReqLabelAssignInput] | None | Unset, data)

        labels = _parse_labels(d.pop("labels", UNSET))

        def _parse_reviewer_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                reviewer_ids_type_0 = cast(list[int], data)

                return reviewer_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        reviewer_ids = _parse_reviewer_ids(d.pop("reviewer_ids", UNSET))

        source_branch = d.pop("source_branch", UNSET)

        source_repo_ref = d.pop("source_repo_ref", UNSET)

        target_branch = d.pop("target_branch", UNSET)

        title = d.pop("title", UNSET)

        def _parse_user_group_reviewer_ids(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_group_reviewer_ids_type_0 = cast(list[int], data)

                return user_group_reviewer_ids_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        user_group_reviewer_ids = _parse_user_group_reviewer_ids(d.pop("user_group_reviewer_ids", UNSET))

        openapi_create_pull_req_request = cls(
            bypass_rules=bypass_rules,
            description=description,
            is_draft=is_draft,
            labels=labels,
            reviewer_ids=reviewer_ids,
            source_branch=source_branch,
            source_repo_ref=source_repo_ref,
            target_branch=target_branch,
            title=title,
            user_group_reviewer_ids=user_group_reviewer_ids,
        )

        openapi_create_pull_req_request.additional_properties = d
        return openapi_create_pull_req_request

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
