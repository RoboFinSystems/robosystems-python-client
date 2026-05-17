from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="OperatorRecommendation")


@_attrs_define
class OperatorRecommendation:
  """Single operator recommendation.

  Attributes:
      operator_type (str): Operator type identifier
      operator_name (str): Operator display name
      confidence (float): Confidence score (0-1)
      capabilities (list[str]): Operator capabilities
      reason (None | str | Unset): Reason for recommendation
  """

  operator_type: str
  operator_name: str
  confidence: float
  capabilities: list[str]
  reason: None | str | Unset = UNSET
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    operator_type = self.operator_type

    operator_name = self.operator_name

    confidence = self.confidence

    capabilities = self.capabilities

    reason: None | str | Unset
    if isinstance(self.reason, Unset):
      reason = UNSET
    else:
      reason = self.reason

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "operator_type": operator_type,
        "operator_name": operator_name,
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
    operator_type = d.pop("operator_type")

    operator_name = d.pop("operator_name")

    confidence = d.pop("confidence")

    capabilities = cast(list[str], d.pop("capabilities"))

    def _parse_reason(data: object) -> None | str | Unset:
      if data is None:
        return data
      if isinstance(data, Unset):
        return data
      return cast(None | str | Unset, data)

    reason = _parse_reason(d.pop("reason", UNSET))

    operator_recommendation = cls(
      operator_type=operator_type,
      operator_name=operator_name,
      confidence=confidence,
      capabilities=capabilities,
      reason=reason,
    )

    operator_recommendation.additional_properties = d
    return operator_recommendation

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
