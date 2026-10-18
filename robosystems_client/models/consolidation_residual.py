from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConsolidationResidual")


@_attrs_define
class ConsolidationResidual:
  """A difference the engine cannot eliminate on its own: the parent's
  investment in a member against the parent's share of that member's
  capital. Its entry is withheld until the difference is explained or
  posted by hand with a basis; it is never plugged.

      Attributes:
          entity_id (str): The member.
          entity_name (str): The member's name.
          amount (int): Cents: the parent's investment balance less its share of the member's capital. Positive when the
              parent carries more than its share.
          explanation (str): What the two figures are.
  """

  entity_id: str
  entity_name: str
  amount: int
  explanation: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entity_id = self.entity_id

    entity_name = self.entity_name

    amount = self.amount

    explanation = self.explanation

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entity_id": entity_id,
        "entity_name": entity_name,
        "amount": amount,
        "explanation": explanation,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    entity_id = d.pop("entity_id")

    entity_name = d.pop("entity_name")

    amount = d.pop("amount")

    explanation = d.pop("explanation")

    consolidation_residual = cls(
      entity_id=entity_id,
      entity_name=entity_name,
      amount=amount,
      explanation=explanation,
    )

    consolidation_residual.additional_properties = d
    return consolidation_residual

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
