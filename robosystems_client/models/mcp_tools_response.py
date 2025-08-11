from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.mcp_tools_response_tools_item import MCPToolsResponseToolsItem


T = TypeVar("T", bound="MCPToolsResponse")


@_attrs_define
class MCPToolsResponse:
  """Response model for MCP tools listing.

  Attributes:
      tools (list['MCPToolsResponseToolsItem']): List of available MCP tools with their schemas
  """

  tools: list["MCPToolsResponseToolsItem"]
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    tools = []
    for tools_item_data in self.tools:
      tools_item = tools_item_data.to_dict()
      tools.append(tools_item)

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "tools": tools,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.mcp_tools_response_tools_item import MCPToolsResponseToolsItem

    d = dict(src_dict)
    tools = []
    _tools = d.pop("tools")
    for tools_item_data in _tools:
      tools_item = MCPToolsResponseToolsItem.from_dict(tools_item_data)

      tools.append(tools_item)

    mcp_tools_response = cls(
      tools=tools,
    )

    mcp_tools_response.additional_properties = d
    return mcp_tools_response

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
