from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_info import NodeInfo
    from ..models.template_info import TemplateInfo
    from ..models.template_response import TemplateResponse


T = TypeVar("T", bound="ErrorNodeSummary")


@_attrs_define
class ErrorNodeSummary:
    """
    Attributes:
        node_info (NodeInfo | Unset):
        template_info (TemplateInfo | Unset):
        template_response (TemplateResponse | Unset): This contains details of the Template Response
        children_error_nodes (list[ErrorNodeSummary] | Unset):
    """

    node_info: NodeInfo | Unset = UNSET
    template_info: TemplateInfo | Unset = UNSET
    template_response: TemplateResponse | Unset = UNSET
    children_error_nodes: list[ErrorNodeSummary] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        node_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.node_info, Unset):
            node_info = self.node_info.to_dict()

        template_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template_info, Unset):
            template_info = self.template_info.to_dict()

        template_response: dict[str, Any] | Unset = UNSET
        if not isinstance(self.template_response, Unset):
            template_response = self.template_response.to_dict()

        children_error_nodes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.children_error_nodes, Unset):
            children_error_nodes = []
            for children_error_nodes_item_data in self.children_error_nodes:
                children_error_nodes_item = children_error_nodes_item_data.to_dict()
                children_error_nodes.append(children_error_nodes_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if node_info is not UNSET:
            field_dict["nodeInfo"] = node_info
        if template_info is not UNSET:
            field_dict["templateInfo"] = template_info
        if template_response is not UNSET:
            field_dict["templateResponse"] = template_response
        if children_error_nodes is not UNSET:
            field_dict["childrenErrorNodes"] = children_error_nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_info import NodeInfo
        from ..models.template_info import TemplateInfo
        from ..models.template_response import TemplateResponse

        d = dict(src_dict)
        _node_info = d.pop("nodeInfo", UNSET)
        node_info: NodeInfo | Unset
        if isinstance(_node_info, Unset):
            node_info = UNSET
        else:
            node_info = NodeInfo.from_dict(_node_info)

        _template_info = d.pop("templateInfo", UNSET)
        template_info: TemplateInfo | Unset
        if isinstance(_template_info, Unset):
            template_info = UNSET
        else:
            template_info = TemplateInfo.from_dict(_template_info)

        _template_response = d.pop("templateResponse", UNSET)
        template_response: TemplateResponse | Unset
        if isinstance(_template_response, Unset):
            template_response = UNSET
        else:
            template_response = TemplateResponse.from_dict(_template_response)

        _children_error_nodes = d.pop("childrenErrorNodes", UNSET)
        children_error_nodes: list[ErrorNodeSummary] | Unset = UNSET
        if _children_error_nodes is not UNSET:
            children_error_nodes = []
            for children_error_nodes_item_data in _children_error_nodes:
                children_error_nodes_item = ErrorNodeSummary.from_dict(children_error_nodes_item_data)

                children_error_nodes.append(children_error_nodes_item)

        error_node_summary = cls(
            node_info=node_info,
            template_info=template_info,
            template_response=template_response,
            children_error_nodes=children_error_nodes,
        )

        error_node_summary.additional_properties = d
        return error_node_summary

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
