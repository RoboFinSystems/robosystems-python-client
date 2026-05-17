from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
  from ..models.operator_recommendation import OperatorRecommendation


T = TypeVar("T", bound="OperatorRecommendationResponse")


@_attrs_define
class OperatorRecommendationResponse:
  """Response for operator recommendations.

  Attributes:
      recommendations (list[OperatorRecommendation]): List of operator recommendations sorted by confidence
      query (str): The analyzed query
  """

  recommendations: list[OperatorRecommendation]
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
    from ..models.operator_recommendation import OperatorRecommendation

    d = dict(src_dict)
    recommendations = []
    _recommendations = d.pop("recommendations")
    for recommendations_item_data in _recommendations:
      recommendations_item = OperatorRecommendation.from_dict(recommendations_item_data)

      recommendations.append(recommendations_item)

    query = d.pop("query")

    operator_recommendation_response = cls(
      recommendations=recommendations,
      query=query,
    )

    operator_recommendation_response.additional_properties = d
    return operator_recommendation_response

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
