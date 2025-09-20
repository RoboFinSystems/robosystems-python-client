from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.agent_mode import AgentMode
from ..types import UNSET, Unset

T = TypeVar("T", bound="SelectionCriteria")


@_attrs_define
class SelectionCriteria:
  """Criteria for agent selection.

  Attributes:
      min_confidence (Union[Unset, float]): Minimum confidence score Default: 0.3.
      required_capabilities (Union[Unset, list[str]]): Required agent capabilities
      preferred_mode (Union[AgentMode, None, Unset]): Preferred execution mode
      max_response_time (Union[Unset, float]): Maximum response time in seconds Default: 60.0.
      excluded_agents (Union[Unset, list[str]]): Agents to exclude from selection
  """

  min_confidence: Union[Unset, float] = 0.3
  required_capabilities: Union[Unset, list[str]] = UNSET
  preferred_mode: Union[AgentMode, None, Unset] = UNSET
  max_response_time: Union[Unset, float] = 60.0
  excluded_agents: Union[Unset, list[str]] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    min_confidence = self.min_confidence

    required_capabilities: Union[Unset, list[str]] = UNSET
    if not isinstance(self.required_capabilities, Unset):
      required_capabilities = self.required_capabilities

    preferred_mode: Union[None, Unset, str]
    if isinstance(self.preferred_mode, Unset):
      preferred_mode = UNSET
    elif isinstance(self.preferred_mode, AgentMode):
      preferred_mode = self.preferred_mode.value
    else:
      preferred_mode = self.preferred_mode

    max_response_time = self.max_response_time

    excluded_agents: Union[Unset, list[str]] = UNSET
    if not isinstance(self.excluded_agents, Unset):
      excluded_agents = self.excluded_agents

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update({})
    if min_confidence is not UNSET:
      field_dict["min_confidence"] = min_confidence
    if required_capabilities is not UNSET:
      field_dict["required_capabilities"] = required_capabilities
    if preferred_mode is not UNSET:
      field_dict["preferred_mode"] = preferred_mode
    if max_response_time is not UNSET:
      field_dict["max_response_time"] = max_response_time
    if excluded_agents is not UNSET:
      field_dict["excluded_agents"] = excluded_agents

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    min_confidence = d.pop("min_confidence", UNSET)

    required_capabilities = cast(list[str], d.pop("required_capabilities", UNSET))

    def _parse_preferred_mode(data: object) -> Union[AgentMode, None, Unset]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, str):
          raise TypeError()
        preferred_mode_type_0 = AgentMode(data)

        return preferred_mode_type_0
      except:  # noqa: E722
        pass
      return cast(Union[AgentMode, None, Unset], data)

    preferred_mode = _parse_preferred_mode(d.pop("preferred_mode", UNSET))

    max_response_time = d.pop("max_response_time", UNSET)

    excluded_agents = cast(list[str], d.pop("excluded_agents", UNSET))

    selection_criteria = cls(
      min_confidence=min_confidence,
      required_capabilities=required_capabilities,
      preferred_mode=preferred_mode,
      max_response_time=max_response_time,
      excluded_agents=excluded_agents,
    )

    selection_criteria.additional_properties = d
    return selection_criteria

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
