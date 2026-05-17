from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
  from ..models.operator_recommendation_request_context_type_0 import (
    OperatorRecommendationRequestContextType0,
  )


T = TypeVar("T", bound="OperatorRecommendationRequest")


@_attrs_define
class OperatorRecommendationRequest:
  """Request for operator recommendations.

  Attributes:
      query (str): Query to analyze
      context (None | OperatorRecommendationRequestContextType0 | Unset): Additional context
  """

  query: str
  context: None | OperatorRecommendationRequestContextType0 | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    from ..models.operator_recommendation_request_context_type_0 import (
      OperatorRecommendationRequestContextType0,
    )

    query = self.query

    context: dict[str, Any] | None | Unset
    if isinstance(self.context, Unset):
      context = UNSET
    elif isinstance(self.context, OperatorRecommendationRequestContextType0):
      context = self.context.to_dict()
    else:
      context = self.context

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "query": query,
      }
    )
    if context is not UNSET:
      field_dict["context"] = context

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    from ..models.operator_recommendation_request_context_type_0 import (
      OperatorRecommendationRequestContextType0,
    )

    d = dict(src_dict)
    query = d.pop("query")

    def _parse_context(
      data: object,
    ) -> None | OperatorRecommendationRequestContextType0 | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, dict):
          raise TypeError()
        context_type_0 = OperatorRecommendationRequestContextType0.from_dict(data)

        return context_type_0
      except (TypeError, ValueError, AttributeError, KeyError):
        pass
      return cast(None | OperatorRecommendationRequestContextType0 | Unset, data)

    context = _parse_context(d.pop("context", UNSET))

    operator_recommendation_request = cls(
      query=query,
      context=context,
    )

    operator_recommendation_request.additional_properties = d
    return operator_recommendation_request

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
