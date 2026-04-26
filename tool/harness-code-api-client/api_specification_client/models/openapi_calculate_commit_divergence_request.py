from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.repo_commit_divergence_request import RepoCommitDivergenceRequest


T = TypeVar("T", bound="OpenapiCalculateCommitDivergenceRequest")


@_attrs_define
class OpenapiCalculateCommitDivergenceRequest:
    """
    Attributes:
        max_count (int | Unset):
        requests (list[RepoCommitDivergenceRequest] | None | Unset):
    """

    max_count: int | Unset = UNSET
    requests: list[RepoCommitDivergenceRequest] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        max_count = self.max_count

        requests: list[dict[str, Any]] | None | Unset
        if isinstance(self.requests, Unset):
            requests = UNSET
        elif isinstance(self.requests, list):
            requests = []
            for requests_type_0_item_data in self.requests:
                requests_type_0_item = requests_type_0_item_data.to_dict()
                requests.append(requests_type_0_item)

        else:
            requests = self.requests

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if max_count is not UNSET:
            field_dict["max_count"] = max_count
        if requests is not UNSET:
            field_dict["requests"] = requests

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.repo_commit_divergence_request import RepoCommitDivergenceRequest

        d = dict(src_dict)
        max_count = d.pop("max_count", UNSET)

        def _parse_requests(data: object) -> list[RepoCommitDivergenceRequest] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                requests_type_0 = []
                _requests_type_0 = data
                for requests_type_0_item_data in _requests_type_0:
                    requests_type_0_item = RepoCommitDivergenceRequest.from_dict(requests_type_0_item_data)

                    requests_type_0.append(requests_type_0_item)

                return requests_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[RepoCommitDivergenceRequest] | None | Unset, data)

        requests = _parse_requests(d.pop("requests", UNSET))

        openapi_calculate_commit_divergence_request = cls(
            max_count=max_count,
            requests=requests,
        )

        openapi_calculate_commit_divergence_request.additional_properties = d
        return openapi_calculate_commit_divergence_request

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
