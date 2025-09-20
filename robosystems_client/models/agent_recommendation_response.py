from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.agent_recommendation import AgentRecommendation


T = TypeVar("T", bound="AgentRecommendationResponse")


@_attrs_define
class AgentRecommendationResponse:
  """Response for agent recommendations.

  Attributes:
      recommendations (list['AgentRecommendation']): List of agent recommendations sorted by confidence
      query (str): The analyzed query
  """

  recommendations: list["AgentRecommendation"]
  query: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    recommendations = []
    for recommendations_item_data in self.recommendations:
      recommendations_item = recommendations_item_data.to_dict()
      recommendations.append(recommendations_item)

    query = self.query

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "recommendations": recommendations,
        "query": query,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.agent_recommendation import AgentRecommendation

    d = dict(src_dict)
    recommendations = []
    _recommendations = d.pop("recommendations")
    for recommendations_item_data in _recommendations:
      recommendations_item = AgentRecommendation.from_dict(recommendations_item_data)

      recommendations.append(recommendations_item)

    query = d.pop("query")

    agent_recommendation_response = cls(
      recommendations=recommendations,
      query=query,
    )

    agent_recommendation_response.additional_properties = d
    return agent_recommendation_response

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
