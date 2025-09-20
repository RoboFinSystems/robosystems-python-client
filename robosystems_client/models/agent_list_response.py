from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.agent_list_response_agents import AgentListResponseAgents


T = TypeVar("T", bound="AgentListResponse")


@_attrs_define
class AgentListResponse:
  """Response for listing available agents.

  Attributes:
      agents (AgentListResponseAgents): Dictionary of available agents with metadata
      total (int): Total number of agents
  """

  agents: "AgentListResponseAgents"
  total: int
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    agents = self.agents.to_dict()

    total = self.total

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "agents": agents,
        "total": total,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.agent_list_response_agents import AgentListResponseAgents

    d = dict(src_dict)
    agents = AgentListResponseAgents.from_dict(d.pop("agents"))

    total = d.pop("total")

    agent_list_response = cls(
      agents=agents,
      total=total,
    )

    agent_list_response.additional_properties = d
    return agent_list_response

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
