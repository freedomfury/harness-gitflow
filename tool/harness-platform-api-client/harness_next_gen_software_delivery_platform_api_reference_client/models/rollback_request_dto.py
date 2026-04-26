from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.rollback_request_dto_environment_type import (
    RollbackRequestDTOEnvironmentType,
    check_rollback_request_dto_environment_type,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="RollbackRequestDTO")


@_attrs_define
class RollbackRequestDTO:
    """
    Attributes:
        service_identifier (str):
        env_identifier (str):
        environment_type (RollbackRequestDTOEnvironmentType | Unset):
        infra_identifier (str | Unset):
        artifact (str | Unset):
        chart_version (str | Unset):
    """

    service_identifier: str
    env_identifier: str
    environment_type: RollbackRequestDTOEnvironmentType | Unset = UNSET
    infra_identifier: str | Unset = UNSET
    artifact: str | Unset = UNSET
    chart_version: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        service_identifier = self.service_identifier

        env_identifier = self.env_identifier

        environment_type: str | Unset = UNSET
        if not isinstance(self.environment_type, Unset):
            environment_type = self.environment_type

        infra_identifier = self.infra_identifier

        artifact = self.artifact

        chart_version = self.chart_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "serviceIdentifier": service_identifier,
                "envIdentifier": env_identifier,
            }
        )
        if environment_type is not UNSET:
            field_dict["environmentType"] = environment_type
        if infra_identifier is not UNSET:
            field_dict["infraIdentifier"] = infra_identifier
        if artifact is not UNSET:
            field_dict["artifact"] = artifact
        if chart_version is not UNSET:
            field_dict["chartVersion"] = chart_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        service_identifier = d.pop("serviceIdentifier")

        env_identifier = d.pop("envIdentifier")

        _environment_type = d.pop("environmentType", UNSET)
        environment_type: RollbackRequestDTOEnvironmentType | Unset
        if isinstance(_environment_type, Unset):
            environment_type = UNSET
        else:
            environment_type = check_rollback_request_dto_environment_type(_environment_type)

        infra_identifier = d.pop("infraIdentifier", UNSET)

        artifact = d.pop("artifact", UNSET)

        chart_version = d.pop("chartVersion", UNSET)

        rollback_request_dto = cls(
            service_identifier=service_identifier,
            env_identifier=env_identifier,
            environment_type=environment_type,
            infra_identifier=infra_identifier,
            artifact=artifact,
            chart_version=chart_version,
        )

        rollback_request_dto.additional_properties = d
        return rollback_request_dto

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
