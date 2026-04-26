from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.enum_merge_method import EnumMergeMethod
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.types_merge_response import TypesMergeResponse
    from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0


T = TypeVar("T", bound="TypesAutoMergeResponse")


@_attrs_define
class TypesAutoMergeResponse:
    """
    Attributes:
        created (int | Unset):
        delete_branch (bool | Unset):
        merge_method (EnumMergeMethod | Unset):
        merge_response (TypesMergeResponse | Unset):
        message (str | Unset):
        requested_by (None | TypesPrincipalInfoType0 | Unset):
        title (str | Unset):
    """

    created: int | Unset = UNSET
    delete_branch: bool | Unset = UNSET
    merge_method: EnumMergeMethod | Unset = UNSET
    merge_response: TypesMergeResponse | Unset = UNSET
    message: str | Unset = UNSET
    requested_by: None | TypesPrincipalInfoType0 | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0

        created = self.created

        delete_branch = self.delete_branch

        merge_method: str | Unset = UNSET
        if not isinstance(self.merge_method, Unset):
            merge_method = self.merge_method.value

        merge_response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.merge_response, Unset):
            merge_response = self.merge_response.to_dict()

        message = self.message

        requested_by: dict[str, Any] | None | Unset
        if isinstance(self.requested_by, Unset):
            requested_by = UNSET
        elif isinstance(self.requested_by, TypesPrincipalInfoType0):
            requested_by = self.requested_by.to_dict()
        else:
            requested_by = self.requested_by

        title = self.title

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if created is not UNSET:
            field_dict["created"] = created
        if delete_branch is not UNSET:
            field_dict["delete_branch"] = delete_branch
        if merge_method is not UNSET:
            field_dict["merge_method"] = merge_method
        if merge_response is not UNSET:
            field_dict["merge_response"] = merge_response
        if message is not UNSET:
            field_dict["message"] = message
        if requested_by is not UNSET:
            field_dict["requested_by"] = requested_by
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.types_merge_response import TypesMergeResponse
        from ..models.types_principal_info_type_0 import TypesPrincipalInfoType0

        d = dict(src_dict)
        created = d.pop("created", UNSET)

        delete_branch = d.pop("delete_branch", UNSET)

        _merge_method = d.pop("merge_method", UNSET)
        merge_method: EnumMergeMethod | Unset
        if isinstance(_merge_method, Unset):
            merge_method = UNSET
        else:
            merge_method = EnumMergeMethod(_merge_method)

        _merge_response = d.pop("merge_response", UNSET)
        merge_response: TypesMergeResponse | Unset
        if isinstance(_merge_response, Unset):
            merge_response = UNSET
        else:
            merge_response = TypesMergeResponse.from_dict(_merge_response)

        message = d.pop("message", UNSET)

        def _parse_requested_by(data: object) -> None | TypesPrincipalInfoType0 | Unset:
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

        requested_by = _parse_requested_by(d.pop("requested_by", UNSET))

        title = d.pop("title", UNSET)

        types_auto_merge_response = cls(
            created=created,
            delete_branch=delete_branch,
            merge_method=merge_method,
            merge_response=merge_response,
            message=message,
            requested_by=requested_by,
            title=title,
        )

        types_auto_merge_response.additional_properties = d
        return types_auto_merge_response

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
