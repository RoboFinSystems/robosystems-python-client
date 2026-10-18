from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ConsolidationReconcilingItem")


@_attrs_define
class ConsolidationReconcilingItem:
  """Two of the group's entities whose intercompany figures do not agree.
  The lower amount is eliminated where one side matches the other; what is
  left stays in the consolidated statements until the books agree.

      Attributes:
          entity_ids (list[str]): The two entities.
          concept (str): The rs-gaap concept left uneliminated.
          entity_id (str): The entity whose figure is left.
          amount (int): Cents left uneliminated, debit-positive.
          description (str): What does not agree.
  """

  entity_ids: list[str]
  concept: str
  entity_id: str
  amount: int
  description: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entity_ids = self.entity_ids

    concept = self.concept

    entity_id = self.entity_id

    amount = self.amount

    description = self.description

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entity_ids": entity_ids,
        "concept": concept,
        "entity_id": entity_id,
        "amount": amount,
        "description": description,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    entity_ids = cast(list[str], d.pop("entity_ids"))

    concept = d.pop("concept")

    entity_id = d.pop("entity_id")

    amount = d.pop("amount")

    description = d.pop("description")

    consolidation_reconciling_item = cls(
      entity_ids=entity_ids,
      concept=concept,
      entity_id=entity_id,
      amount=amount,
      description=description,
    )

    consolidation_reconciling_item.additional_properties = d
    return consolidation_reconciling_item

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
