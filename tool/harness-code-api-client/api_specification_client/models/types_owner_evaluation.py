from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_pull_req_review_decision import EnumPullReqReviewDecision
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0


T = TypeVar("T", bound="TypesOwnerEvaluation")


@_attrs_define
class TypesOwnerEvaluation:
    """
    Attributes:
        owner (None | TypesPrincipalInfoType0 | Unset):
        review_decision (EnumPullReqReviewDecision | Unset):
        review_sha (str | Unset):
    """

    owner: None | TypesPrincipalInfoType0 | Unset = UNSET
    review_decision: EnumPullReqReviewDecision | Unset = UNSET
    review_sha: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0

        owner: dict[str, Any] | None | Unset
        if isinstance(self.owner, Unset):
            owner = UNSET
        elif isinstance(self.owner, TypesPrincipalInfoType0):
            owner = self.owner.to_dict()
        else:
            owner = self.owner

        review_decision: str | Unset = UNSET
        if not isinstance(self.review_decision, Unset):
            review_decision = self.review_decision.value

        review_sha = self.review_sha

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if owner is not UNSET:
            field_dict["owner"] = owner
        if review_decision is not UNSET:
            field_dict["review_decision"] = review_decision
        if review_sha is not UNSET:
            field_dict["review_sha"] = review_sha

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0

        d = dict(src_dict)

        def _parse_owner(data: object) -> None | TypesPrincipalInfoType0 | Unset:
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

        owner = _parse_owner(d.pop("owner", UNSET))

        _review_decision = d.pop("review_decision", UNSET)
        review_decision: EnumPullReqReviewDecision | Unset
        if isinstance(_review_decision, Unset):
            review_decision = UNSET
        else:
            review_decision = EnumPullReqReviewDecision(_review_decision)

        review_sha = d.pop("review_sha", UNSET)

        types_owner_evaluation = cls(
            owner=owner,
            review_decision=review_decision,
            review_sha=review_sha,
        )

        types_owner_evaluation.additional_properties = d
        return types_owner_evaluation

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
