from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.importer_pipeline_option import ImporterPipelineOption
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.importer_provider import ImporterProvider


T = TypeVar("T", bound="ImportRepositoryBody")


@_attrs_define
class ImportRepositoryBody:
    """
    Attributes:
        description (str | Unset):
        identifier (str | Unset):
        parent_ref (str | Unset):
        pipelines (ImporterPipelineOption | Unset):
        provider (ImporterProvider | Unset):
        provider_repo (str | Unset):
        uid (str | Unset):
    """

    description: str | Unset = UNSET
    identifier: str | Unset = UNSET
    parent_ref: str | Unset = UNSET
    pipelines: ImporterPipelineOption | Unset = UNSET
    provider: ImporterProvider | Unset = UNSET
    provider_repo: str | Unset = UNSET
    uid: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        description = self.description

        identifier = self.identifier

        parent_ref = self.parent_ref

        pipelines: str | Unset = UNSET
        if not isinstance(self.pipelines, Unset):
            pipelines = self.pipelines.value

        provider: dict[str, Any] | Unset = UNSET
        if not isinstance(self.provider, Unset):
            provider = self.provider.to_dict()

        provider_repo = self.provider_repo

        uid = self.uid

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if identifier is not UNSET:
            field_dict["identifier"] = identifier
        if parent_ref is not UNSET:
            field_dict["parent_ref"] = parent_ref
        if pipelines is not UNSET:
            field_dict["pipelines"] = pipelines
        if provider is not UNSET:
            field_dict["provider"] = provider
        if provider_repo is not UNSET:
            field_dict["provider_repo"] = provider_repo
        if uid is not UNSET:
            field_dict["uid"] = uid

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.importer_provider import ImporterProvider

        d = dict(src_dict)
        description = d.pop("description", UNSET)

        identifier = d.pop("identifier", UNSET)

        parent_ref = d.pop("parent_ref", UNSET)

        _pipelines = d.pop("pipelines", UNSET)
        pipelines: ImporterPipelineOption | Unset
        if isinstance(_pipelines, Unset):
            pipelines = UNSET
        else:
            pipelines = ImporterPipelineOption(_pipelines)

        _provider = d.pop("provider", UNSET)
        provider: ImporterProvider | Unset
        if isinstance(_provider, Unset):
            provider = UNSET
        else:
            provider = ImporterProvider.from_dict(_provider)

        provider_repo = d.pop("provider_repo", UNSET)

        uid = d.pop("uid", UNSET)

        import_repository_body = cls(
            description=description,
            identifier=identifier,
            parent_ref=parent_ref,
            pipelines=pipelines,
            provider=provider,
            provider_repo=provider_repo,
            uid=uid,
        )

        import_repository_body.additional_properties = d
        return import_repository_body

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
