from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RecordOwnershipChangeRequest")


@_attrs_define
class RecordOwnershipChangeRequest:
  """The parent buys more of a member from its outside owners, staying on the
  same consolidation method: the share it holds from a month, and what it
  paid. ASC 810 makes it an equity transaction, never a gain or loss.

      Attributes:
          entity_id (str): The member, consolidated in full.
          period (str): The month, as YYYY-MM.
          ownership_pct (float): The parent's share from `period`, as a percentage: above its share the month before, and
              50 or more, so the member stays consolidated in full.
          consideration (int): Cents the parent paid the outside owners for the shares. Its line names them, not the
              member, which is why it is given here.
          basis (str): The purchase agreement, or what sets the price.
  """

  entity_id: str
  period: str
  ownership_pct: float
  consideration: int
  basis: str
  additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

  def to_dict(self) -> dict[str, Any]:
    entity_id = self.entity_id

    period = self.period

    ownership_pct = self.ownership_pct

    consideration = self.consideration

    basis = self.basis

    field_dict: dict[str, Any] = {}
    field_dict.update(self.additional_properties)
    field_dict.update(
      {
        "entity_id": entity_id,
        "period": period,
        "ownership_pct": ownership_pct,
        "consideration": consideration,
        "basis": basis,
      }
    )

    return field_dict

  @classmethod
  def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
    d = dict(src_dict)
    entity_id = d.pop("entity_id")

    period = d.pop("period")

    ownership_pct = d.pop("ownership_pct")

    consideration = d.pop("consideration")

    basis = d.pop("basis")

    record_ownership_change_request = cls(
      entity_id=entity_id,
      period=period,
      ownership_pct=ownership_pct,
      consideration=consideration,
      basis=basis,
    )

    record_ownership_change_request.additional_properties = d
    return record_ownership_change_request

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
