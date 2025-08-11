from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StorageLimitResponse")


@_attrs_define
class StorageLimitResponse:
  """Storage limit information response.

  Attributes:
      graph_id (str):
      current_storage_gb (float):
      effective_limit_gb (float):
      usage_percentage (float):
      within_limit (bool):
      approaching_limit (bool):
      needs_warning (bool):
      has_override (bool):
      recommendations (Union[None, Unset, list[str]]):
  """

  graph_id: str
  current_storage_gb: float
  effective_limit_gb: float
  usage_percentage: float
  within_limit: bool
  approaching_limit: bool
  needs_warning: bool
  has_override: bool
  recommendations: Union[None, Unset, list[str]] = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    graph_id = self.graph_id

    current_storage_gb = self.current_storage_gb

    effective_limit_gb = self.effective_limit_gb

    usage_percentage = self.usage_percentage

    within_limit = self.within_limit

    approaching_limit = self.approaching_limit

    needs_warning = self.needs_warning

    has_override = self.has_override

    recommendations: Union[None, Unset, list[str]]
    if isinstance(self.recommendations, Unset):
      recommendations = UNSET
    elif isinstance(self.recommendations, list):
      recommendations = self.recommendations

    else:
      recommendations = self.recommendations

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "graph_id": graph_id,
        "current_storage_gb": current_storage_gb,
        "effective_limit_gb": effective_limit_gb,
        "usage_percentage": usage_percentage,
        "within_limit": within_limit,
        "approaching_limit": approaching_limit,
        "needs_warning": needs_warning,
        "has_override": has_override,
      }
    )
    if recommendations is not UNSET:
      field_dict["recommendations"] = recommendations

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    graph_id = d.pop("graph_id")

    current_storage_gb = d.pop("current_storage_gb")

    effective_limit_gb = d.pop("effective_limit_gb")

    usage_percentage = d.pop("usage_percentage")

    within_limit = d.pop("within_limit")

    approaching_limit = d.pop("approaching_limit")

    needs_warning = d.pop("needs_warning")

    has_override = d.pop("has_override")

    def _parse_recommendations(data: object) -> Union[None, Unset, list[str]]:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      try:
        if not isinstance(data, list):
          raise TypeError()
        recommendations_type_0 = cast(list[str], data)

        return recommendations_type_0
      except:  # noqa: E722
        pass
      return cast(Union[None, Unset, list[str]], data)

    recommendations = _parse_recommendations(d.pop("recommendations", UNSET))

    storage_limit_response = cls(
      graph_id=graph_id,
      current_storage_gb=current_storage_gb,
      effective_limit_gb=effective_limit_gb,
      usage_percentage=usage_percentage,
      within_limit=within_limit,
      approaching_limit=approaching_limit,
      needs_warning=needs_warning,
      has_override=has_override,
      recommendations=recommendations,
    )

    storage_limit_response.additional_properties = d
    return storage_limit_response

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
