from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AwsCurAttributes")


@_attrs_define
class AwsCurAttributes:
    """This contains AWS cost and usage reports attributes

    Attributes:
        report_name (str):
        s_3_bucket_name (str):
        region (str | Unset):
        s_3_prefix (str | Unset):
    """

    report_name: str
    s_3_bucket_name: str
    region: str | Unset = UNSET
    s_3_prefix: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        report_name = self.report_name

        s_3_bucket_name = self.s_3_bucket_name

        region = self.region

        s_3_prefix = self.s_3_prefix

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "reportName": report_name,
                "s3BucketName": s_3_bucket_name,
            }
        )
        if region is not UNSET:
            field_dict["region"] = region
        if s_3_prefix is not UNSET:
            field_dict["s3Prefix"] = s_3_prefix

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        report_name = d.pop("reportName")

        s_3_bucket_name = d.pop("s3BucketName")

        region = d.pop("region", UNSET)

        s_3_prefix = d.pop("s3Prefix", UNSET)

        aws_cur_attributes = cls(
            report_name=report_name,
            s_3_bucket_name=s_3_bucket_name,
            region=region,
            s_3_prefix=s_3_prefix,
        )

        aws_cur_attributes.additional_properties = d
        return aws_cur_attributes

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
