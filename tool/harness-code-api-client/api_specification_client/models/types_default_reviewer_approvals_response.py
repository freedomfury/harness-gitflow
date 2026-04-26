from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0
    from ..models.types_reviewer_evaluation import TypesReviewerEvaluation
    from ..models.types_user_group_info import TypesUserGroupInfo


T = TypeVar("T", bound="TypesDefaultReviewerApprovalsResponse")


@_attrs_define
class TypesDefaultReviewerApprovalsResponse:
    """
    Attributes:
        current_count (int | Unset):
        evaluations (list[TypesReviewerEvaluation] | None | Unset):
        minimum_required_count (int | Unset):
        minimum_required_count_latest (int | Unset):
        principals (list[None | TypesPrincipalInfoType0] | None | Unset):
        user_groups (list[TypesUserGroupInfo] | None | Unset):
    """

    current_count: int | Unset = UNSET
    evaluations: list[TypesReviewerEvaluation] | None | Unset = UNSET
    minimum_required_count: int | Unset = UNSET
    minimum_required_count_latest: int | Unset = UNSET
    principals: list[None | TypesPrincipalInfoType0] | None | Unset = UNSET
    user_groups: list[TypesUserGroupInfo] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0

        current_count = self.current_count

        evaluations: list[dict[str, Any]] | None | Unset
        if isinstance(self.evaluations, Unset):
            evaluations = UNSET
        elif isinstance(self.evaluations, list):
            evaluations = []
            for evaluations_type_0_item_data in self.evaluations:
                evaluations_type_0_item = evaluations_type_0_item_data.to_dict()
                evaluations.append(evaluations_type_0_item)

        else:
            evaluations = self.evaluations

        minimum_required_count = self.minimum_required_count

        minimum_required_count_latest = self.minimum_required_count_latest

        principals: list[dict[str, Any] | None] | None | Unset
        if isinstance(self.principals, Unset):
            principals = UNSET
        elif isinstance(self.principals, list):
            principals = []
            for principals_type_0_item_data in self.principals:
                principals_type_0_item: dict[str, Any] | None
                if isinstance(principals_type_0_item_data, TypesPrincipalInfoType0):
                    principals_type_0_item = principals_type_0_item_data.to_dict()
                else:
                    principals_type_0_item = principals_type_0_item_data
                principals.append(principals_type_0_item)

        else:
            principals = self.principals

        user_groups: list[dict[str, Any]] | None | Unset
        if isinstance(self.user_groups, Unset):
            user_groups = UNSET
        elif isinstance(self.user_groups, list):
            user_groups = []
            for user_groups_type_0_item_data in self.user_groups:
                user_groups_type_0_item = user_groups_type_0_item_data.to_dict()
                user_groups.append(user_groups_type_0_item)

        else:
            user_groups = self.user_groups

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if current_count is not UNSET:
            field_dict["current_count"] = current_count
        if evaluations is not UNSET:
            field_dict["evaluations"] = evaluations
        if minimum_required_count is not UNSET:
            field_dict["minimum_required_count"] = minimum_required_count
        if minimum_required_count_latest is not UNSET:
            field_dict["minimum_required_count_latest"] = minimum_required_count_latest
        if principals is not UNSET:
            field_dict["principals"] = principals
        if user_groups is not UNSET:
            field_dict["user_groups"] = user_groups

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0
        from ..models.types_reviewer_evaluation import TypesReviewerEvaluation
        from ..models.types_user_group_info import TypesUserGroupInfo

        d = dict(src_dict)
        current_count = d.pop("current_count", UNSET)

        def _parse_evaluations(data: object) -> list[TypesReviewerEvaluation] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                evaluations_type_0 = []
                _evaluations_type_0 = data
                for evaluations_type_0_item_data in _evaluations_type_0:
                    evaluations_type_0_item = TypesReviewerEvaluation.from_dict(evaluations_type_0_item_data)

                    evaluations_type_0.append(evaluations_type_0_item)

                return evaluations_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TypesReviewerEvaluation] | None | Unset, data)

        evaluations = _parse_evaluations(d.pop("evaluations", UNSET))

        minimum_required_count = d.pop("minimum_required_count", UNSET)

        minimum_required_count_latest = d.pop("minimum_required_count_latest", UNSET)

        def _parse_principals(data: object) -> list[None | TypesPrincipalInfoType0] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                principals_type_0 = []
                _principals_type_0 = data
                for principals_type_0_item_data in _principals_type_0:

                    def _parse_principals_type_0_item(data: object) -> None | TypesPrincipalInfoType0:
                        if data is None:
                            return data
                        try:
                            if not isinstance(data, dict):
                                raise TypeError()
                            componentsschemas_types_principal_info_type_0 = TypesPrincipalInfoType0.from_dict(data)

                            return componentsschemas_types_principal_info_type_0
                        except (TypeError, ValueError, AttributeError, KeyError):
                            pass
                        return cast(None | TypesPrincipalInfoType0, data)

                    principals_type_0_item = _parse_principals_type_0_item(principals_type_0_item_data)

                    principals_type_0.append(principals_type_0_item)

                return principals_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[None | TypesPrincipalInfoType0] | None | Unset, data)

        principals = _parse_principals(d.pop("principals", UNSET))

        def _parse_user_groups(data: object) -> list[TypesUserGroupInfo] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                user_groups_type_0 = []
                _user_groups_type_0 = data
                for user_groups_type_0_item_data in _user_groups_type_0:
                    user_groups_type_0_item = TypesUserGroupInfo.from_dict(user_groups_type_0_item_data)

                    user_groups_type_0.append(user_groups_type_0_item)

                return user_groups_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TypesUserGroupInfo] | None | Unset, data)

        user_groups = _parse_user_groups(d.pop("user_groups", UNSET))

        types_default_reviewer_approvals_response = cls(
            current_count=current_count,
            evaluations=evaluations,
            minimum_required_count=minimum_required_count,
            minimum_required_count_latest=minimum_required_count_latest,
            principals=principals,
            user_groups=user_groups,
        )

        types_default_reviewer_approvals_response.additional_properties = d
        return types_default_reviewer_approvals_response

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
