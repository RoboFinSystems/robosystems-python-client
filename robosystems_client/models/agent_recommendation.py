from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="AgentRecommendation")


@_attrs_define
class AgentRecommendation:
  """Single agent recommendation.

  Attributes:
      agent_type (str): Agent type identifier
      agent_name (str): Agent display name
      confidence (float): Confidence score (0-1)
      capabilities (list[str]): Agent capabilities
      reason (Union[None, Unset, str]): Reason for recommendation
  """

  agent_type: str
  agent_name: str
  confidence: float
  capabilities: list[str]
  reason: Union[None, Unset, str] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    agent_type = self.agent_type

    agent_name = self.agent_name

    confidence = self.confidence

    capabilities = self.capabilities

    reason: Union[None, Unset, str]
    if isinstance(self.reason, Unset):
      reason = UNSET
    else:
      reason = self.reason

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "agent_type": agent_type,
        "agent_name": agent_name,
        "confidence": confidence,
        "capabilities": capabilities,
      }
    )
    if reason is not UNSET:
      field_dict["reason"] = reason

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    agent_type = d.pop("agent_type")

    agent_name = d.pop("agent_name")

    confidence = d.pop("confidence")

    capabilities = cast(list[str], d.pop("capabilities"))

    def _parse_reason(data: object) -> Union[None, Unset, str]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(Union[None, Unset, str], data)

    reason = _parse_reason(d.pop("reason", UNSET))

    agent_recommendation = cls(
      agent_type=agent_type,
      agent_name=agent_name,
      confidence=confidence,
      capabilities=capabilities,
      reason=reason,
    )

    agent_recommendation.additional_properties = d
    return agent_recommendation

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
