from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_pull_req_check import TypesPullReqCheck


T = TypeVar("T", bound="TypesPullReqChecks")


@_attrs_define
class TypesPullReqChecks:
    """
    Attributes:
        checks (list[TypesPullReqCheck] | None | Unset):
        commit_sha (str | Unset):
    """

    checks: list[TypesPullReqCheck] | None | Unset = UNSET
    commit_sha: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        checks: list[dict[str, Any]] | None | Unset
        if isinstance(self.checks, Unset):
            checks = UNSET
        elif isinstance(self.checks, list):
            checks = []
            for checks_type_0_item_data in self.checks:
                checks_type_0_item = checks_type_0_item_data.to_dict()
                checks.append(checks_type_0_item)

        else:
            checks = self.checks

        commit_sha = self.commit_sha

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if checks is not UNSET:
            field_dict["checks"] = checks
        if commit_sha is not UNSET:
            field_dict["commit_sha"] = commit_sha

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_pull_req_check import TypesPullReqCheck

        d = dict(src_dict)

        def _parse_checks(data: object) -> list[TypesPullReqCheck] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                checks_type_0 = []
                _checks_type_0 = data
                for checks_type_0_item_data in _checks_type_0:
                    checks_type_0_item = TypesPullReqCheck.from_dict(checks_type_0_item_data)

                    checks_type_0.append(checks_type_0_item)

                return checks_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[TypesPullReqCheck] | None | Unset, data)

        checks = _parse_checks(d.pop("checks", UNSET))

        commit_sha = d.pop("commit_sha", UNSET)

        types_pull_req_checks = cls(
            checks=checks,
            commit_sha=commit_sha,
        )

        types_pull_req_checks.additional_properties = d
        return types_pull_req_checks

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
