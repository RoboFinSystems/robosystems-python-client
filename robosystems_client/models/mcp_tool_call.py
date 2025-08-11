from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.mcp_tool_call_arguments import MCPToolCallArguments


T = TypeVar("T", bound="MCPToolCall")


@_attrs_define
class MCPToolCall:
  """Request model for MCP tool execution.

  Attributes:
      name (str): Name of the MCP tool to execute
      arguments (Union[Unset, MCPToolCallArguments]): Arguments to pass to the tool
  """

  name: str
  arguments: Union[Unset, "MCPToolCallArguments"] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    name = self.name

    arguments: Union[Unset, dict[str, Any]] = UNSET
    if not isinstance(self.arguments, Unset):
      arguments = self.arguments.to_dict()

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "name": name,
      }
    )
    if arguments is not UNSET:
      field_dict["arguments"] = arguments

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.mcp_tool_call_arguments import MCPToolCallArguments

    d = dict(src_dict)
    name = d.pop("name")

    _arguments = d.pop("arguments", UNSET)
    arguments: Union[Unset, MCPToolCallArguments]
    if isinstance(_arguments, Unset):
      arguments = UNSET
    else:
      arguments = MCPToolCallArguments.from_dict(_arguments)

    mcp_tool_call = cls(
      name=name,
      arguments=arguments,
    )

    mcp_tool_call.additional_properties = d
    return mcp_tool_call

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
